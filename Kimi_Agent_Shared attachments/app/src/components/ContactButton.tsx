interface ContactButtonProps {
  label?: string;
  href?: string;
  className?: string;
}

export default function ContactButton({
  label = 'Contact Me',
  href = 'mailto:hello@jack3d.studio',
  className = '',
}: ContactButtonProps) {
  return (
    <a
      href={href}
      className={`inline-block rounded-full px-8 py-3 text-xs font-medium uppercase tracking-widest text-white outline outline-2 -outline-offset-[3px] outline-white transition-transform duration-200 hover:scale-[1.03] active:scale-[0.98] sm:px-10 sm:py-3.5 sm:text-sm md:px-12 md:py-4 md:text-base ${className}`}
      style={{
        background: 'linear-gradient(123deg, #18011F 7%, #B600A8 37%, #7621B0 72%, #BE4C00 100%)',
        boxShadow: '0px 4px 4px rgba(181, 1, 167, 0.25), 4px 4px 12px #7721B1 inset',
      }}
    >
      {label}
    </a>
  );
}
