import React from 'react';
import { ServiceDetail } from '../../components/ServiceDetail';

export const BlockchainPage: React.FC = () => {
    const serviceData = {
        title: 'Blockchain Development',
        subtitle: 'Build decentralized applications and solutions for the future of technology',
        description: 'Harness the power of blockchain technology to create transparent, secure, and decentralized solutions. From smart contracts to NFT marketplaces and DeFi platforms, we develop innovative blockchain applications that transform how businesses operate.',
        image: 'https://images.unsplash.com/photo-1639762681485-074b7f938ba0?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&w=1080&q=80',
        features: [
            'Smart contract development',
            'DApp (Decentralized App) development',
            'NFT marketplace development',
            'DeFi platform development',
            'Token creation (ERC-20, ERC-721)',
            'Blockchain consulting',
            'Private blockchain solutions',
            'Crypto wallet development',
            'Smart contract auditing',
            'Web3 integration',
            'Blockchain analytics & monitoring',
            'Cross-chain development',
        ],
        benefits: [
            'Enhanced security and transparency',
            'Eliminate intermediaries and reduce costs',
            'Immutable and tamper-proof records',
            'Automated processes through smart contracts',
            'New revenue streams through tokenization',
            'Future-proof your business with Web3',
        ],
        process: [
            { title: 'Consult', description: 'Understand your use case and determine blockchain viability' },
            { title: 'Architect', description: 'Design the blockchain solution and smart contract logic' },
            { title: 'Develop', description: 'Build, test, and audit the blockchain application' },
            { title: 'Launch', description: 'Deploy to mainnet and provide ongoing support' },
        ],
        packages: [
            {
                name: 'Smart Contract',
                price: '$8,000',
                features: [
                    'Smart contract development',
                    'Solidity/Rust programming',
                    'Testnet deployment',
                    'Basic security audit',
                    'Documentation',
                    'Mainnet deployment',
                    '30 days support',
                ],
            },
            {
                name: 'DApp Development',
                price: '$25,000',
                popular: true,
                features: [
                    'Everything in Smart Contract',
                    'Full DApp development',
                    'Web3 frontend',
                    'Wallet integration',
                    'Token creation',
                    'Admin dashboard',
                    'Comprehensive audit',
                    '90 days support',
                    'Multi-chain support',
                ],
            },
            {
                name: 'Enterprise Blockchain',
                price: 'Custom',
                features: [
                    'Full-scale blockchain solution',
                    'Private/consortium blockchain',
                    'Multiple smart contracts',
                    'Custom token economics',
                    'Advanced security audit',
                    'Compliance support',
                    'Dedicated development team',
                    'Ongoing maintenance',
                    '24/7 support',
                    'Custom integrations',
                ],
            },
        ],
        faqs: [
            {
                question: 'What blockchain platforms do you work with?',
                answer: 'We work with Ethereum, Polygon, Solana, Binance Smart Chain, Avalanche, and other major platforms. We recommend the best platform based on your specific requirements for speed, cost, and functionality.',
            },
            {
                question: 'How secure are smart contracts?',
                answer: 'Smart contracts are highly secure when properly developed and audited. We follow security best practices and conduct thorough audits to identify and fix vulnerabilities before deployment.',
            },
            {
                question: 'What is the cost of deploying to mainnet?',
                answer: 'Gas fees vary by network and market conditions. Ethereum can be expensive during high activity, while Layer 2 solutions like Polygon offer much lower fees. We help you choose the most cost-effective option.',
            },
            {
                question: 'Do I need cryptocurrency knowledge to use your services?',
                answer: 'No, we guide you through the entire process. We explain concepts in simple terms and handle all technical aspects. You just need a clear idea of what you want to achieve.',
            },
            {
                question: 'Can you tokenize real-world assets?',
                answer: 'Yes, we can help tokenize real estate, art, commodities, and other assets. This includes creating the token, smart contracts for ownership transfer, and ensuring regulatory compliance.',
            },
        ],
    };

    return <ServiceDetail {...serviceData} />;
};
