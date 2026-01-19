import React from 'react';
import { ServiceDetail } from '../../components/ServiceDetail';

export const SocialMediaPage: React.FC = () => {
    const serviceData = {
        title: 'Social Media Marketing',
        subtitle: 'Build your brand presence and engage with your audience across social platforms',
        description: 'Connect with your target audience where they spend their time. Our social media marketing services help you build brand awareness, foster community engagement, and drive meaningful conversions through strategic content and paid social campaigns.',
        image: 'https://images.unsplash.com/photo-1611162617474-5b21e879e113?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&w=1080&q=80',
        features: [
            'Social media strategy development',
            'Content creation & curation',
            'Community management',
            'Paid social advertising',
            'Influencer marketing',
            'Social media analytics',
            'Brand monitoring & reputation management',
            'Platform-specific optimization',
            'Hashtag research & strategy',
            'Social media calendar management',
            'User-generated content campaigns',
            'Crisis management',
        ],
        benefits: [
            'Increase brand awareness and reach',
            'Build a loyal community around your brand',
            'Drive targeted traffic to your website',
            'Generate leads and conversions',
            'Improve customer satisfaction and loyalty',
            'Gain valuable insights into your audience',
        ],
        process: [
            { title: 'Audit', description: 'Analyze your current social presence and competitor landscape' },
            { title: 'Strategy', description: 'Develop a tailored social media strategy for each platform' },
            { title: 'Create', description: 'Produce engaging content that resonates with your audience' },
            { title: 'Grow', description: 'Execute campaigns and continuously optimize for growth' },
        ],
        packages: [
            {
                name: 'Social Starter',
                price: '$699',
                features: [
                    '2 social platforms',
                    '12 posts per month',
                    'Basic graphic design',
                    'Community management',
                    'Monthly analytics report',
                    'Content calendar',
                    'Email support',
                ],
            },
            {
                name: 'Social Pro',
                price: '$1,499',
                popular: true,
                features: [
                    '4 social platforms',
                    '24 posts per month',
                    'Custom graphics & videos',
                    'Stories & Reels content',
                    'Paid ad management (up to $1k)',
                    'Influencer outreach',
                    'Bi-weekly reports & strategy calls',
                    'Hashtag research',
                    'Priority support',
                ],
            },
            {
                name: 'Social Enterprise',
                price: '$2,999',
                features: [
                    'Unlimited platforms',
                    'Daily posting',
                    'Premium content production',
                    'Video content creation',
                    'Paid ad management (unlimited)',
                    'Influencer partnerships',
                    'Dedicated social media manager',
                    'Real-time monitoring',
                    'Crisis management',
                    'Weekly strategy calls',
                ],
            },
        ],
        faqs: [
            {
                question: 'Which social media platforms should my business be on?',
                answer: 'It depends on your target audience. We analyze where your customers are most active and focus efforts there. For most B2C businesses, Instagram, Facebook, and TikTok are key. For B2B, LinkedIn is essential.',
            },
            {
                question: 'How often should we post on social media?',
                answer: 'Consistency matters more than frequency. We recommend at least 3-5 posts per week on most platforms, but we tailor this to each platform\'s best practices and your audience behavior.',
            },
            {
                question: 'Do you create all the content?',
                answer: 'Yes, we handle content creation including graphics, captions, and short-form videos. We also curate relevant industry content and can repurpose your existing content for social.',
            },
            {
                question: 'How do you measure social media success?',
                answer: 'We track engagement rates, follower growth, reach, impressions, website traffic from social, and conversions. We provide detailed monthly reports with insights and recommendations.',
            },
            {
                question: 'Can you help with paid social advertising?',
                answer: 'Absolutely! Paid social is included in our Pro and Enterprise packages. We create and manage campaigns on Facebook, Instagram, LinkedIn, TikTok, and other platforms.',
            },
        ],
    };

    return <ServiceDetail {...serviceData} />;
};
