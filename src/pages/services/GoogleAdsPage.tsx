import React from 'react';
import { ServiceDetail } from '../../components/ServiceDetail';

export const GoogleAdsPage: React.FC = () => {
    const serviceData = {
        title: 'Google Ads (PPC)',
        subtitle: 'Drive instant traffic and maximize ROI with targeted pay-per-click advertising',
        description: 'Reach your ideal customers at the exact moment they\'re searching for your products or services. Our expert Google Ads management delivers high-converting campaigns that maximize your advertising budget and generate measurable results.',
        image: 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&w=1080&q=80',
        features: [
            'Google Search Ads campaigns',
            'Google Display Network advertising',
            'YouTube video ads',
            'Google Shopping campaigns',
            'Remarketing & retargeting',
            'Keyword research & optimization',
            'Ad copywriting & A/B testing',
            'Landing page optimization',
            'Conversion tracking setup',
            'Bid management & optimization',
            'Quality score improvement',
            'Competitor analysis',
        ],
        benefits: [
            'Instant visibility on Google search results',
            'Precise targeting based on keywords and demographics',
            'Complete control over your advertising budget',
            'Measurable results with detailed analytics',
            'Higher conversion rates than organic traffic',
            'Scalable campaigns that grow with your business',
        ],
        process: [
            { title: 'Research', description: 'Analyze your market, competitors, and identify high-value keywords' },
            { title: 'Strategy', description: 'Develop a custom PPC strategy aligned with your business goals' },
            { title: 'Launch', description: 'Create and launch optimized ad campaigns across Google platforms' },
            { title: 'Optimize', description: 'Continuously monitor, test, and improve campaign performance' },
        ],
        packages: [
            {
                name: 'Starter PPC',
                price: '$599',
                features: [
                    'Up to $2,000 ad spend management',
                    'Google Search Ads setup',
                    'Keyword research (50 keywords)',
                    'Ad copywriting (5 ads)',
                    'Basic conversion tracking',
                    'Monthly performance report',
                    'Email support',
                ],
            },
            {
                name: 'Growth PPC',
                price: '$1,299',
                popular: true,
                features: [
                    'Up to $10,000 ad spend management',
                    'Search + Display campaigns',
                    'Keyword research (150 keywords)',
                    'Ad copywriting (15 ads)',
                    'Advanced conversion tracking',
                    'Remarketing campaigns',
                    'Landing page recommendations',
                    'Bi-weekly reports & calls',
                    'Priority support',
                ],
            },
            {
                name: 'Enterprise PPC',
                price: '$2,499',
                features: [
                    'Unlimited ad spend management',
                    'Full Google Ads suite',
                    'Unlimited keywords',
                    'Unlimited ad variations',
                    'YouTube advertising',
                    'Shopping campaigns',
                    'Custom landing pages',
                    'Dedicated account manager',
                    'Weekly strategy calls',
                    'Real-time reporting dashboard',
                ],
            },
        ],
        faqs: [
            {
                question: 'How quickly will I see results from Google Ads?',
                answer: 'Unlike SEO, Google Ads provides immediate visibility. You can start seeing traffic within hours of launching your campaign. However, optimization for best ROI typically takes 2-4 weeks.',
            },
            {
                question: 'What is a good budget to start with Google Ads?',
                answer: 'We recommend starting with at least $1,000-$2,000/month for meaningful data and results. The ideal budget depends on your industry competition and goals.',
            },
            {
                question: 'How do you measure success in PPC campaigns?',
                answer: 'We track key metrics including click-through rate (CTR), cost per click (CPC), conversion rate, cost per acquisition (CPA), and return on ad spend (ROAS).',
            },
            {
                question: 'Do I own my Google Ads account?',
                answer: 'Absolutely. You retain full ownership of your Google Ads account. We simply manage it on your behalf, and you can access it anytime.',
            },
            {
                question: 'Can you work with my existing Google Ads account?',
                answer: 'Yes, we can audit and optimize your existing campaigns or build new ones from scratch based on what will perform best for your business.',
            },
        ],
    };

    return <ServiceDetail {...serviceData} />;
};
