import React from 'react';
import { ServiceDetail } from '../../components/ServiceDetail';

export const SoftwareDevelopmentPage: React.FC = () => {
    const serviceData = {
        title: 'Software Development',
        subtitle: 'Custom software solutions tailored to your unique business needs',
        description: 'Transform your business operations with custom software development. From enterprise applications to specialized tools, we design and build scalable, secure, and intuitive software solutions that streamline your workflows and drive efficiency.',
        image: 'https://images.unsplash.com/photo-1555066931-4365d14bab8c?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&w=1080&q=80',
        features: [
            'Custom enterprise applications',
            'SaaS product development',
            'API development & integration',
            'Database design & optimization',
            'Legacy system modernization',
            'Cloud-native applications',
            'Microservices architecture',
            'DevOps & CI/CD implementation',
            'Quality assurance & testing',
            'System architecture design',
            'Third-party integrations',
            'Maintenance & support',
        ],
        benefits: [
            'Software built specifically for your workflows',
            'Improved operational efficiency and automation',
            'Seamless integration with existing systems',
            'Scalable solutions that grow with your business',
            'Enhanced data security and compliance',
            'Competitive advantage through innovation',
        ],
        process: [
            { title: 'Discovery', description: 'Understand your requirements, challenges, and business objectives' },
            { title: 'Design', description: 'Create detailed specifications and system architecture' },
            { title: 'Develop', description: 'Build your software using agile methodology with regular updates' },
            { title: 'Deploy', description: 'Launch, test, and provide ongoing support and maintenance' },
        ],
        packages: [
            {
                name: 'MVP Development',
                price: '$15,000',
                features: [
                    'Requirements analysis',
                    'UI/UX design',
                    'Core feature development',
                    'Basic integrations',
                    'Testing & QA',
                    'Deployment',
                    '30 days support',
                    '8-12 weeks timeline',
                ],
            },
            {
                name: 'Full Product',
                price: '$45,000',
                popular: true,
                features: [
                    'Everything in MVP',
                    'Advanced features',
                    'Complex integrations',
                    'Admin dashboard',
                    'Analytics & reporting',
                    'Mobile-responsive design',
                    'API documentation',
                    '90 days support',
                    '4-6 months timeline',
                ],
            },
            {
                name: 'Enterprise Solution',
                price: 'Custom',
                features: [
                    'Full-scale enterprise development',
                    'Multi-platform support',
                    'Advanced security features',
                    'Compliance (HIPAA, GDPR, etc.)',
                    'Performance optimization',
                    'Dedicated development team',
                    'Ongoing maintenance',
                    'SLA guarantees',
                    '24/7 support',
                    'Custom timeline',
                ],
            },
        ],
        faqs: [
            {
                question: 'How long does custom software development take?',
                answer: 'Timeline varies based on complexity. An MVP typically takes 8-12 weeks, while full-scale enterprise solutions may take 6-12 months or more. We provide detailed timelines after requirements analysis.',
            },
            {
                question: 'What technologies do you use?',
                answer: 'We work with modern technologies including React, Node.js, Python, .NET, Java, AWS, Azure, PostgreSQL, MongoDB, and more. We choose the best stack based on your specific requirements.',
            },
            {
                question: 'Do you provide ongoing maintenance?',
                answer: 'Yes, we offer maintenance and support packages to ensure your software stays updated, secure, and performing optimally. This includes bug fixes, updates, and feature enhancements.',
            },
            {
                question: 'Can you work with our existing development team?',
                answer: 'Absolutely. We can augment your existing team with our developers or work alongside them. We\'re flexible and adapt to your preferred collaboration model.',
            },
            {
                question: 'How do you ensure software quality?',
                answer: 'We follow industry best practices including code reviews, automated testing, CI/CD pipelines, and rigorous QA processes. Every feature is thoroughly tested before deployment.',
            },
        ],
    };

    return <ServiceDetail {...serviceData} />;
};
