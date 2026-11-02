import { useEffect, useRef } from 'react';

const BASE = 'https://motionsites.ai/assets';

const row1Images = [
  'hero-space-voyage-preview-eECLH3Yc',
  'hero-codenest-preview-Cgppc2qV',
  'hero-vex-ventures-preview-BczMFIiw',
  'hero-stellar-ai-v2-preview-DjvxjG3C',
  'hero-asme-preview-B_nGDnTP',
  'hero-transform-data-preview-Cx5OU29N',
  'hero-vitara-preview-Cjz2QYyU',
  'hero-terra-preview-BFjrCr7T',
  'hero-skyelite-preview-DHaZIgUv',
  'hero-aethera-preview-DknSlcTa',
  'hero-designpro-preview-D8c5_een',
];

const row2Images = [
  'hero-stellar-ai-preview-D3HL6bw1',
  'hero-xportfolio-preview-D4A8maiC',
  'hero-orbit-web3-preview-BXt4OttD',
  'hero-nexora-preview-cx5HmUgo',
  'hero-evr-ventures-preview-DZxeVFEX',
  'hero-planet-orbit-preview-DWAP8Z1P',
  'hero-new-era-preview-CocuDUm9',
  'hero-wealth-preview-B70idl_u',
  'hero-luminex-preview-CxOP7ce6',
  'hero-celestia-preview-0yO3jXO8',
];

function MarqueeRow({
  images,
  rowRef,
  className = '',
}: {
  images: string[];
  rowRef: React.RefObject<HTMLDivElement | null>;
  className?: string;
}) {
  const tripled = [...images, ...images, ...images];
  return (
    <div className={`overflow-visible ${className}`}>
      <div ref={rowRef} className="flex gap-3" style={{ willChange: 'transform' }}>
        {tripled.map((name, i) => (
          <img
            key={`${name}-${i}`}
            src={`${BASE}/${name}.gif`}
            alt="Selected 3D website work preview"
            loading="lazy"
            draggable={false}
            className="h-[270px] w-[420px] flex-shrink-0 rounded-2xl object-cover"
          />
        ))}
      </div>
    </div>
  );
}

export default function MarqueeSection() {
  const sectionRef = useRef<HTMLElement>(null);
  const row1Ref = useRef<HTMLDivElement>(null);
  const row2Ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const update = () => {
      const section = sectionRef.current;
      if (!section) return;
      const sectionTop = section.getBoundingClientRect().top + window.scrollY;
      const offset = (window.scrollY - sectionTop + window.innerHeight) * 0.3;
      if (row1Ref.current) {
        row1Ref.current.style.transform = `translateX(${offset - 200}px)`;
      }
      if (row2Ref.current) {
        row2Ref.current.style.transform = `translateX(${-(offset - 200)}px)`;
      }
    };

    update();
    window.addEventListener('scroll', update, { passive: true });
    return () => window.removeEventListener('scroll', update);
  }, []);

  return (
    <section ref={sectionRef} className="overflow-x-clip bg-[#0C0C0C] pb-10 pt-24 sm:pt-32 md:pt-40">
      <MarqueeRow images={row1Images} rowRef={row1Ref} className="-ml-[500px]" />
      <MarqueeRow images={row2Images} rowRef={row2Ref} className="mt-3" />
    </section>
  );
}
