"""
Website scraper for comprehensive data ingestion.
Crawls the entire NexGenTeck website and extracts ALL content for the knowledge base.
This is the ONLY source of information for the chatbot.
"""

import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Set
from urllib.parse import urljoin, urlparse
import logging
import time

from config import config
from utils import clean_text, chunk_text

logger = logging.getLogger(__name__)


class WebsiteScraper:
    """
    Comprehensive website scraper for building the chatbot's knowledge base.
    Extracts ALL content from the website - this is the source of truth.
    """
    
    def __init__(self, base_url: str = None):
        """
        Initialize the scraper.
        
        Args:
            base_url: Base URL to scrape (defaults to config.WEBSITE_URL)
        """
        self.base_url = base_url or config.WEBSITE_URL
        self.visited_urls: Set[str] = set()
        self.documents: List[Dict[str, str]] = []
        
    def scrape(self, max_pages: int = 100) -> List[Dict[str, str]]:
        """
        Scrape the ENTIRE website and extract ALL content.
        For local development, uses translation files directly.
        For production, scrapes the live website.
        
        Args:
            max_pages: Maximum number of pages to scrape
            
        Returns:
            List of documents with 'content' and 'metadata' keys
        """
        logger.info(f"Starting comprehensive scrape of {self.base_url}")
        
        # For local development, use translation extractor to get ACTUAL content
        # This avoids the issue of reading t('key') instead of real text
        if 'localhost' in self.base_url or '127.0.0.1' in self.base_url:
            logger.info("Local development detected - using translation extractor")
            try:
                from translation_extractor import get_translation_based_content
                self.documents = get_translation_based_content()
                logger.info(f"Loaded {len(self.documents)} documents from translations")
                return self.documents
            except Exception as e:
                logger.warning(f"Translation extractor failed: {e}, falling back to source scraping")
        
        # known routes for the React app (since crawler can't always find links in JS)
        known_routes = [
            '/',
            '/about',
            '/services',
            '/portfolio', 
            '/pricing',
            '/blog',
            '/contact',
            '/services/web-development',
            '/services/mobile-app-development', 
            '/services/ecommerce',
            '/services/seo',
            '/services/social-media-marketing',
            '/services/software-development',
            '/services/3d-graphics',
            '/services/video-editing'
        ]
        
        # Add all known routes to the visit queue
        for route in known_routes:
            full_url = urljoin(self.base_url, route)
            try:
                self._crawl_page(full_url, max_pages)
            except Exception as e:
                logger.error(f"Failed to scrape {full_url}: {e}")
                
        logger.info(f"Scraped {len(self.visited_urls)} pages, created {len(self.documents)} documents")
        return self.documents
    
    def _crawl_page(self, url: str, max_pages: int):
        """
        Crawl a page. For local dev (SPA), we fallback to reading source files
        because scraping localhost React often returns empty HTML.
        """
        if len(self.visited_urls) >= max_pages:
            return
            
        self.visited_urls.add(url)
        logger.info(f"Processing: {url}")
        
        # 1. Try to map the URL to a local source file
        # This is much more reliable for a local React app than scraping
        parsed = urlparse(url)
        path = parsed.path.strip('/')
        
        # Map URL path to file path
        # Example: services/ecommerce -> src/pages/services/EcommercePage.tsx
        source_content = self._read_local_source_file(path)
        
        if source_content:
            logger.info(f"Found local source file for {url}")
            self._process_content(source_content, url, f"Page: {path or 'Home'}")
            return

        # 2. Fallback to HTTP scraping (for external links or if file not found)
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'lxml')
                self._extract_all_content(soup, url)
        except Exception as e:
            logger.warning(f"Failed to fetch {url}: {e}")

    def _read_local_source_file(self, url_path: str) -> str:
        """
        Read the content of fem corresponding React component file.
        Adjusts path mapping based on project structure.
        """
        import os
        
        # Base directory for pages
        # Assuming script runs from Chatbot/, we go up -> src/pages
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'pages'))
        
        if not url_path:
            # Home page
            target_files = [os.path.join(base_dir, 'Home.tsx')]
        else:
            # Convert URL path to PascalCase for filename match
            # e.g. services/web-development -> Services/WebDevelopmentPage.tsx or similar
            parts = url_path.split('/')
            
            # Simple heuristic mapping
            if len(parts) == 1:
                # Top level pages: about -> About.tsx
                name = parts[0].capitalize()
                target_files = [os.path.join(base_dir, f"{name}.tsx")]
            elif parts[0] == 'services':
                # Service pages: services/web-development -> services/WebDevelopmentPage.tsx
                # Need to convert kebab-case to PascalCase
                service_name = ''.join(word.capitalize() for word in parts[1].split('-'))
                target_files = [
                    os.path.join(base_dir, 'services', f"{service_name}Page.tsx"),
                    os.path.join(base_dir, 'services', f"{service_name}.tsx")
                ]
            else:
                target_files = []

        for fpath in target_files:
            if os.path.exists(fpath):
                try:
                    with open(fpath, 'r', encoding='utf-8') as f:
                        return f.read()
                except Exception as e:
                    logger.error(f"Error reading file {fpath}: {e}")
        
        return None

    def _process_content(self, raw_text: str, url: str, title: str):
        """Process raw text (source code or HTML text) into chunks."""
        # Simple cleanup to remove import statements and noisy code syntax
        # We want to keep the text content primarily
        lines = []
        for line in raw_text.split('\n'):
            line = line.strip()
            # Skip imports and pure code lines roughly
            if line.startswith('import ') or line.startswith('export ') or line == '}' or line == '{':
                continue
            if len(line) > 5:
                lines.append(line)
        
        clean_content = '\n'.join(lines)
        
        chunks = chunk_text(clean_content, chunk_size=800, overlap=100)
        for i, chunk in enumerate(chunks):
            self.documents.append({
                'content': chunk,
                'metadata': {
                    'source': url,
                    'title': title,
                    'chunk_index': i
                }
            })
    
    def _extract_all_content(self, soup: BeautifulSoup, url: str):
        """
        Extract ALL relevant content from a page.
        This is comprehensive - we want all the website information.
        
        Args:
            soup: BeautifulSoup object
            url: URL of the page
        """
        # Remove elements that don't contain useful content
        for element in soup(['script', 'style', 'noscript', 'iframe']):
            element.decompose()
        
        # Extract page title
        title = soup.find('title')
        title_text = clean_text(title.get_text()) if title else ""
        
        # Extract meta description
        meta_desc = soup.find('meta', {'name': 'description'})
        meta_desc_text = meta_desc.get('content', '') if meta_desc else ''
        
        # Extract all headings
        headings = []
        for h in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
            text = clean_text(h.get_text())
            if text and len(text) > 2:
                level = h.name  # h1, h2, etc.
                headings.append(f"[{level.upper()}] {text}")
        
        # Extract all paragraphs
        paragraphs = []
        for p in soup.find_all('p'):
            text = clean_text(p.get_text())
            if text and len(text) > 15:  # Skip very short paragraphs
                paragraphs.append(text)
        
        # Extract list items (services, features, benefits, etc.)
        list_items = []
        for li in soup.find_all('li'):
            text = clean_text(li.get_text())
            if text and len(text) > 10:
                list_items.append(f"• {text}")
        
        # Extract spans and divs with substantial text (for modern websites)
        other_content = []
        for elem in soup.find_all(['span', 'div', 'section', 'article']):
            # Only direct text, not nested
            direct_text = elem.find(string=True, recursive=False)
            if direct_text:
                text = clean_text(str(direct_text))
                if text and len(text) > 30:
                    other_content.append(text)
        
        # Extract table content
        tables = []
        for table in soup.find_all('table'):
            rows = []
            for tr in table.find_all('tr'):
                cells = [clean_text(td.get_text()) for td in tr.find_all(['td', 'th'])]
                if cells:
                    rows.append(' | '.join(cells))
            if rows:
                tables.append('\n'.join(rows))
        
        # Build comprehensive document for this page
        content_parts = []
        
        # Page identification
        content_parts.append(f"PAGE: {title_text}")
        content_parts.append(f"URL: {url}")
        
        if meta_desc_text:
            content_parts.append(f"DESCRIPTION: {meta_desc_text}")
        
        # All headings provide structure
        if headings:
            content_parts.append("SECTIONS:")
            content_parts.extend(headings)
        
        # Main content
        if paragraphs:
            content_parts.append("CONTENT:")
            content_parts.extend(paragraphs)
        
        # Lists contain important features/services
        if list_items:
            content_parts.append("FEATURES/ITEMS:")
            content_parts.extend(list_items[:30])  # Limit to prevent too much
        
        # Other content
        if other_content:
            unique_other = list(set(other_content))[:20]
            content_parts.extend(unique_other)
        
        # Tables
        if tables:
            content_parts.append("TABLE DATA:")
            content_parts.extend(tables[:5])
        
        # Combine all content
        full_content = "\n\n".join(content_parts)
        
        if full_content and len(full_content) > 50:
            # Chunk the content for better retrieval
            chunks = chunk_text(full_content, chunk_size=800, overlap=100)
            
            for i, chunk in enumerate(chunks):
                self.documents.append({
                    'content': chunk,
                    'metadata': {
                        'source': url,
                        'title': title_text,
                        'chunk_index': i,
                        'total_chunks': len(chunks)
                    }
                })
    
    def _get_fallback_content(self) -> List[Dict[str, str]]:
        """
        Return fallback content if scraping fails completely.
        This ensures the chatbot has basic knowledge.
        """
        fallback = [
            {
                'content': """PAGE: NexGenTeck - Digital Solutions Company
URL: https://nexgenteck.com

NexGenTeck is a leading technology company specializing in comprehensive digital solutions. 
We help businesses transform and grow through innovative technology.

OUR COMPLETE SERVICES LIST (8 SERVICES):
1. Web Development - Custom websites, web applications, responsive design
2. Mobile App Development - iOS and Android apps, cross-platform solutions
3. E-commerce Solutions - Online stores, payment integration, inventory management
4. SEO Services - Search engine optimization, content strategy, analytics
5. Social Media Marketing - Brand management, content creation, advertising
6. Software Development - Custom software, enterprise solutions, SaaS platforms
7. 3D Graphics Designing - 3D modeling, animation, product visualization, architectural renders
8. Video Editing - Professional video editing, motion graphics, promotional videos

We use modern technologies including React, Next.js, TypeScript, Node.js, Python, and more.

Contact us for a free consultation to discuss your project requirements.""",
                'metadata': {'source': 'fallback', 'title': 'About NexGenTeck'}
            },
            {
                'content': """PAGE: Our Services
URL: https://nexgenteck.com/services

WEB DEVELOPMENT
We build modern, responsive websites using the latest technologies:
• Custom website design and development
• React and Next.js applications
• E-commerce platforms, Content management systems
• Progressive web apps, Website maintenance and support

MOBILE APP DEVELOPMENT
Native and cross-platform mobile applications for iOS and Android:
• React Native and Flutter development
• Native iOS (Swift) and Android (Kotlin)
• App store optimization, Mobile UI/UX design

E-COMMERCE SOLUTIONS
Complete online store solutions:
• Shopify and WooCommerce development
• Custom e-commerce platforms
• Payment gateway integration, Inventory management

SEO SERVICES
Search engine optimization to boost your online visibility:
• On-page and off-page SEO
• Keyword research and content optimization
• Technical SEO audits, Analytics and reporting

SOCIAL MEDIA MARKETING
Grow your brand presence across social platforms:
• Social media strategy and management
• Content creation and scheduling
• Paid advertising campaigns, Analytics

SOFTWARE DEVELOPMENT
Custom software solutions for your business:
• Enterprise software development
• SaaS platforms and applications
• API development and integration
• Cloud solutions and deployment

3D GRAPHICS DESIGNING
Professional 3D visualization and design:
• 3D modeling and animation
• Product visualization and renders
• Architectural visualization
• Character design and animation

VIDEO EDITING
Professional video production services:
• Video editing and post-production
• Motion graphics and animations
• Promotional and marketing videos
• Social media video content""",
                'metadata': {'source': 'fallback', 'title': 'Services Overview'}
            },
            {
                'content': """PAGE: Contact NexGenTeck
URL: https://nexgenteck.com/contact

Get in touch with our team for your digital transformation needs.

CONTACT INFORMATION:
• Email: info@nexgenteck.com
• Phone: Available on request
• Location: Serving clients globally

HOW WE WORK:
1. Initial Consultation - We discuss your requirements and goals
2. Proposal & Planning - Detailed project plan and timeline
3. Development - Agile development with regular updates
4. Testing & QA - Thorough testing before launch
5. Launch & Support - Deployment and ongoing maintenance

We offer competitive pricing and flexible engagement models.
Contact us today for a free consultation!""",
                'metadata': {'source': 'fallback', 'title': 'Contact Information'}
            }
        ]
        
        logger.info("Using fallback content")
        return fallback
