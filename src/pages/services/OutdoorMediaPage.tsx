import React from 'react';
import { ServiceDetail } from '../../components/ServiceDetail';

export const OutdoorMediaPage: React.FC = () => {
    const serviceData = {
        title: 'Outdoor Media',
        subtitle: 'Make a big impact with strategic outdoor advertising and digital displays',
        description: 'Capture attention in the physical world with impactful outdoor advertising. From billboards and transit ads to digital displays and experiential marketing, we create outdoor campaigns that reach your audience where they live, work, and travel.',
        image: 'https://images.unsplash.com/photo-1504384308090-c894fdcc538d?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&w=1080&q=80',
        features: [
            'Billboard advertising',
            'Digital out-of-home (DOOH)',
            'Transit advertising',
            'Street furniture ads',
            'Airport & mall advertising',
            'Experiential marketing',
            'Event branding',
            'Vehicle wraps',
            'Shop signage & branding',
            'Location analysis & targeting',
            'Creative design services',
            'Campaign measurement',
        ],
        benefits: [
            'Massive reach and visibility in high-traffic areas',
            'Build brand awareness at scale',
            'Reach audiences when they\'re out and active',
            'Complement your digital marketing efforts',
            'Create memorable brand impressions',
            'Target specific geographic locations',
        ],
        process: [
            { title: 'Strategy', description: 'Identify target locations and develop campaign concept' },
            { title: 'Creative', description: 'Design impactful visuals optimized for outdoor viewing' },
            { title: 'Placement', description: 'Secure premium advertising locations and install' },
            { title: 'Measure', description: 'Track campaign performance and audience reach' },
        ],
        packages: [
            {
                name: 'Local Impact',
                price: '$2,500',
                features: [
                    'Local market analysis',
                    '1 billboard location',
                    'Creative design (1 concept)',
                    '30-day campaign',
                    'Installation included',
                    'Basic reach reporting',
                    'Campaign consultation',
                ],
            },
            {
                name: 'Regional Reach',
                price: '$7,500',
                popular: true,
                features: [
                    'Regional market analysis',
                    '3-5 billboard locations',
                    'Creative design (3 concepts)',
                    'Digital billboard options',
                    '60-day campaign',
                    'Transit advertising add-on',
                    'Detailed analytics',
                    'Strategy consultation',
                    'A/B creative testing',
                ],
            },
            {
                name: 'National Campaign',
                price: 'Custom',
                features: [
                    'National market strategy',
                    'Premium nationwide locations',
                    'Full creative suite',
                    'Digital DOOH integration',
                    'Custom campaign duration',
                    'Multi-format advertising',
                    'Experiential activations',
                    'Dedicated account team',
                    'Real-time performance dashboard',
                    'Integrated digital retargeting',
                ],
            },
        ],
        faqs: [
            {
                question: 'How effective is outdoor advertising in the digital age?',
                answer: 'Outdoor advertising remains highly effective, with studies showing 71% of consumers consciously look at billboard messages. When combined with digital campaigns, outdoor ads can boost online engagement by 46%.',
            },
            {
                question: 'How do you measure outdoor advertising success?',
                answer: 'We use traffic data, mobile location analytics, brand lift studies, and website traffic correlation to measure campaign effectiveness. Digital billboards also provide impression data.',
            },
            {
                question: 'What makes a good outdoor advertisement?',
                answer: 'Effective outdoor ads have bold visuals, minimal text (7 words or less), high contrast, and a clear call-to-action. Our creative team specializes in designs optimized for outdoor viewing.',
            },
            {
                question: 'How long should an outdoor campaign run?',
                answer: 'We recommend a minimum of 4 weeks for billboard campaigns to build frequency. Most effective campaigns run 2-3 months, with longer durations for brand awareness goals.',
            },
            {
                question: 'Can you target specific demographics with outdoor ads?',
                answer: 'Yes! We use demographic data, traffic patterns, and location intelligence to place ads in areas where your target audience is most likely to see them.',
            },
        ],
    };

    return <ServiceDetail {...serviceData} />;
};
