# 002 - Hero Slider Implementation

**Date:** 2025-12-25  
**Status:** ✅ Completed  

---

## User Request

Redesign the Hero section of `src/pages/Home.tsx` to be a dynamic slider/carousel similar to the provided reference image. Features: full-width slides, background images, text overlays, navigation arrows, and dot indicators.

---

## Specification

### Technical Approach
- **Component:** Existing Embla Carousel from `src/components/ui/carousel.tsx`
- **State Management:** React useState for carousel API and current slide tracking
- **Styling:** Custom CSS with `!important` rules to force single-slide display

### Design Choices
1. **Full-width slides** with 600px/700px height (mobile/desktop)
2. **Gradient overlay** (`from-black/60 via-black/40 to-transparent`) for text readability
3. **Left-aligned content** with max-width constraint
4. **Clickable dot indicators** with active state animation
5. **Navigation arrows** positioned on left/right edges with blur backdrop

---

## Prompt Used

```
"I need to redesign the Hero section of my src/pages/Home.tsx file to look like a slider/carousel, similar to the reference image I have.

Requirements:
- Import Carousel, CarouselContent, CarouselItem, CarouselNext, CarouselPrevious
- Create heroSlides array with 3 slides (id, image, title, subtitle, ctaText, ctaLink)
- Full width carousel with background images
- Overlay text with gradient for readability
- Use Tailwind CSS, fully responsive"
```

---

## Implementation Details

### Files Modified

| File | Changes |
|------|---------|
| `src/pages/Home.tsx` | Added Carousel imports, heroSlides data, carousel state, replaced Hero section |
| `src/index.css` | Added `.hero-carousel` CSS rules for single-slide display |

### Key Code Changes

**Home.tsx - Imports:**
```tsx
import {
  Carousel, CarouselContent, CarouselItem,
  CarouselNext, CarouselPrevious, type CarouselApi,
} from '../components/ui/carousel';
```

**Home.tsx - State:**
```tsx
const [carouselApi, setCarouselApi] = React.useState<CarouselApi>();
const [currentSlide, setCurrentSlide] = React.useState(0);
```

**index.css - Fix for single-slide display:**
```css
.hero-carousel [data-slot="carousel-item"] {
  flex: 0 0 100% !important;
  min-width: 0 !important;
  padding-left: 0 !important;
}
```

### Slide Data Structure
```typescript
const heroSlides = [
  { id: 1, image: "...", title: "Transform Your Digital Presence", ... },
  { id: 2, image: "...", title: "Innovative Web Solutions", ... },
  { id: 3, image: "...", title: "Scale Your Business", ... },
];
```

---

## Future Considerations

### Enhancements to Consider
1. **Auto-play:** Add Embla Autoplay plugin for automatic slide transitions
2. **Pause on hover:** Stop auto-play when user hovers
3. **Swipe gestures:** Already supported by Embla, test on mobile
4. **Dynamic slides:** Load from CMS/API
5. **Lazy loading:** Add lazy loading for slide images

### Important Notes
- The `hero-carousel` class is required for the CSS fix to work
- If carousel shows multiple slides, check that the CSS was applied
- The `[data-slot="carousel-item"]` selector targets Embla's internal structure

### Known Issues Fixed
- **Multiple slides visible:** Fixed by adding `flex: 0 0 100% !important`
- **Slides overlapping:** Fixed by adding `overflow-hidden` to wrapper

---

*Last reviewed: 2025-12-25*
