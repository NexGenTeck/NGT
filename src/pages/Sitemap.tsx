import React from 'react';
import { Link } from 'react-router';
import { AnimatedSection } from '../components/AnimatedSection';
import { useLanguage } from '../contexts/LanguageContext';
import { sitemapSections } from '../data/sitemapData';

export const Sitemap: React.FC = () => {
  const { t } = useLanguage();

  return (
    <div className="min-h-screen pt-20">
      <section className="relative hero-dark text-white py-20">
        <div className="hero-network"></div>
        <div className="hero-glow-lines"></div>
        <div className="hero-particles"></div>
        <div className="container mx-auto px-4 relative z-10">
          <AnimatedSection className="text-center max-w-4xl mx-auto">
            <h1 className="text-5xl lg:text-6xl font-bold mb-6">{t('sitemap.title')}</h1>
            <p className="text-xl text-white/90">{t('sitemap.subtitle')}</p>
          </AnimatedSection>
        </div>
      </section>

      <section className="py-20 bg-gray-50">
        <div className="container mx-auto px-4">
          <div className="grid gap-10 md:grid-cols-2 lg:grid-cols-3 max-w-6xl mx-auto">
            {sitemapSections.map((section, sectionIndex) => (
              <AnimatedSection key={section.titleKey} delay={sectionIndex * 0.1}>
                <div className="bg-white rounded-2xl shadow-lg p-8 h-full">
                  <h2 className="text-2xl font-bold text-gray-900 mb-6 border-b border-orange-100 pb-3">
                    {t(section.titleKey)}
                  </h2>
                  <ul className="space-y-3">
                    {section.links.map((link) => (
                      <li key={link.path}>
                        <Link
                          to={link.path}
                          className="text-gray-700 hover:text-orange-500 transition-colors"
                        >
                          {link.labelKey ? t(link.labelKey) : link.label}
                        </Link>
                      </li>
                    ))}
                  </ul>
                </div>
              </AnimatedSection>
            ))}
          </div>
        </div>
      </section>
    </div>
  );
};
