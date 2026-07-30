Use only lightweight vanilla animation solutions.

Priority:
1. CSS transitions/animations
2. Intersection Observer API
3. Web Animations API
4. Motion One only when needed

Avoid:
- GSAP
- ScrollTrigger
- scroll-based animations
- parallax
- continuous animations
- heavy effects

Animations must never cause:
- re-renders
- layout shifts
- image reloads
- scroll lag
- hydration issues

Prefer one-time reveal animations and GPU-friendly transforms.