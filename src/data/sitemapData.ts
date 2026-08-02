export const SITE_URL = 'https://nexgenteck.com';

export interface SitemapLink {
  path: string;
  labelKey?: string;
  label?: string;
}

export interface SitemapSection {
  titleKey: string;
  links: SitemapLink[];
}

export const sitemapSections: SitemapSection[] = [
  {
    titleKey: 'sitemap.mainPages',
    links: [
      { path: '/', labelKey: 'nav.home' },
      { path: '/about', labelKey: 'nav.about' },
      { path: '/services', labelKey: 'nav.services' },
      { path: '/portfolio', labelKey: 'nav.portfolio' },
      { path: '/pricing', labelKey: 'nav.pricing' },
      { path: '/contact', labelKey: 'nav.contact' },
    ],
  },
  {
    titleKey: 'sitemap.services',
    links: [
      { path: '/services/ecommerce', labelKey: 'services.ecommerce' },
      { path: '/services/web-development', labelKey: 'services.web' },
      { path: '/services/seo', labelKey: 'services.seo' },
      { path: '/services/mobile-app', labelKey: 'services.mobile' },
      { path: '/services/social-media', labelKey: 'services.social' },
      { path: '/services/software', labelKey: 'services.software' },
      { path: '/services/3d-graphics', labelKey: 'services.3dgraphics' },
      { path: '/services/video-editing', labelKey: 'services.videoediting' },
      { path: '/services/artificial-intelligence', labelKey: 'services.ai' },
    ],
  },
  {
    titleKey: 'sitemap.portfolio',
    links: [
      { path: '/portfolio/trackit', label: 'TrackIT' },
      { path: '/portfolio/swift-translate-pro', label: 'Swift Translate Pro' },
      { path: '/portfolio/tiktok-downloader', label: 'TikTok Downloader' },
      { path: '/portfolio/t-downloader-app', label: 'T Downloader App' },
      { path: '/portfolio/ai-property-booking-concierge', label: 'AI Property Booking Concierge' },
      { path: '/portfolio/digital-campaign', labelKey: 'portfolio.projects.digital-campaign.title' },
    ],
  },
];

export function getAllSitemapPaths(): string[] {
  return sitemapSections.flatMap((section) => section.links.map((link) => link.path));
}
