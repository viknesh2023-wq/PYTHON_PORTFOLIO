import { useRef } from 'react';
import { motion, useScroll, useTransform } from 'framer-motion';
import type { MotionValue } from 'framer-motion';
import FadeIn from '../components/FadeIn';
import LiveProjectButton from '../components/LiveProjectButton';

interface Project {
  id: string;
  name: string;
  category: string;
  images: [string, string, string];
}

const projects: Project[] = [
  {
    id: '01',
    name: 'Nextlevel Studio',
    category: 'Client',
    images: ['/assets/p1a.webp', '/assets/p1b.webp', '/assets/p1c.webp'],
  },
  {
    id: '02',
    name: 'Aura Brand Identity',
    category: 'Personal',
    images: ['/assets/p2a.webp', '/assets/p2b.webp', '/assets/p2c.webp'],
  },
  {
    id: '03',
    name: 'Solaris Digital',
    category: 'Client',
    images: ['/assets/p3a.webp', '/assets/p3b.webp', '/assets/p3c.webp'],
  },
];

function ProjectCard({
  project,
  index,
  total,
  progress,
}: {
  project: Project;
  index: number;
  total: number;
  progress: MotionValue<number>;
}) {
  const targetScale = 1 - (total - 1 - index) * 0.03;
  const scale = useTransform(progress, [index / total, 1], [1, targetScale]);

  return (
    <div className="flex h-[85vh] items-start justify-center">
      <motion.div
        className="project-card w-full origin-top rounded-[40px] border-2 border-[#D7E2EA] bg-[#0C0C0C] p-4 sm:rounded-[50px] sm:p-6 md:rounded-[60px] md:p-8"
        style={{
          scale,
          '--card-offset': `${index * 28}px`,
        } as unknown as React.CSSProperties}
      >
        {/* Top row */}
        <div className="flex flex-wrap items-center gap-x-6 gap-y-4 sm:gap-x-8 md:gap-x-10">
          <span className="text-[clamp(3rem,10vw,140px)] font-black leading-none text-[#D7E2EA]">
            {project.id}
          </span>
          <div className="flex flex-col gap-1 sm:gap-2">
            <span className="text-[clamp(0.7rem,1.2vw,1rem)] font-light uppercase tracking-widest text-[#D7E2EA] opacity-60">
              {project.category}
            </span>
            <h3 className="text-[clamp(1.2rem,3vw,2.6rem)] font-medium uppercase leading-tight text-[#D7E2EA]">
              {project.name}
            </h3>
          </div>
          <div className="ml-auto">
            <LiveProjectButton href={project.images[2]} />
          </div>
        </div>

        {/* Image grid */}
        <div className="mt-5 flex gap-3 sm:mt-6 sm:gap-4 md:mt-8">
          <div className="flex w-[40%] flex-col gap-3 sm:gap-4">
            <img
              src={project.images[0]}
              alt={`${project.name} visual 1`}
              loading="lazy"
              draggable={false}
              className="h-[clamp(130px,16vw,230px)] w-full rounded-[40px] object-cover sm:rounded-[50px] md:rounded-[60px]"
            />
            <img
              src={project.images[1]}
              alt={`${project.name} visual 2`}
              loading="lazy"
              draggable={false}
              className="h-[clamp(160px,22vw,340px)] w-full rounded-[40px] object-cover sm:rounded-[50px] md:rounded-[60px]"
            />
          </div>
          <div className="w-[60%]">
            <img
              src={project.images[2]}
              alt={`${project.name} hero visual`}
              loading="lazy"
              draggable={false}
              className="h-full w-full rounded-[40px] object-cover sm:rounded-[50px] md:rounded-[60px]"
            />
          </div>
        </div>
      </motion.div>
    </div>
  );
}

export default function ProjectsSection() {
  const containerRef = useRef<HTMLDivElement>(null);
  const { scrollYProgress } = useScroll({
    target: containerRef,
    offset: ['start start', 'end end'],
  });

  return (
    <section
      id="projects"
      className="relative z-10 -mt-10 rounded-t-[40px] bg-[#0C0C0C] px-5 py-20 sm:-mt-12 sm:rounded-t-[50px] sm:px-8 sm:py-24 md:-mt-14 md:rounded-t-[60px] md:px-10 md:py-32"
    >
      <FadeIn as="h2" delay={0} y={40} className="hero-heading mb-16 text-center text-[clamp(3rem,12vw,160px)] font-black uppercase leading-none tracking-tight sm:mb-20 md:mb-28">
        Project
      </FadeIn>

      <div ref={containerRef} className="mx-auto max-w-6xl">
        {projects.map((project, i) => (
          <ProjectCard
            key={project.id}
            project={project}
            index={i}
            total={projects.length}
            progress={scrollYProgress}
          />
        ))}
      </div>

      {/* Footer */}
      <div className="mt-20 flex flex-col items-center gap-8 pb-4 sm:mt-28">
        <p className="max-w-[520px] text-center text-[clamp(0.9rem,1.6vw,1.3rem)] font-light uppercase leading-snug tracking-wide text-[#D7E2EA] opacity-70">
          Have an idea worth building? Let&apos;s make it unforgettable.
        </p>
        <FadeIn delay={0.1} y={20}>
          <a
            href="mailto:hello@jack3d.studio"
            className="text-[clamp(1.4rem,4vw,3rem)] font-medium uppercase tracking-wide text-[#D7E2EA] underline decoration-2 underline-offset-8 transition-opacity duration-200 hover:opacity-70"
          >
            hello@jack3d.studio
          </a>
        </FadeIn>
        <p className="mt-6 text-xs font-light uppercase tracking-widest text-[#D7E2EA] opacity-40">
          © 2026 Jack — 3D Creator
        </p>
      </div>
    </section>
  );
}
