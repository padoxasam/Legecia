import palette from "./palette";

export default function NeonCard({ children, style = {} }) {
  return (
    <div
      style={{
        background: palette.panel,
        borderRadius: "10px",
        padding: "14px",
        boxShadow: palette.glow,
        border: "1px solid rgba(255,255,255,0.03)",
        ...style,
      }}
    >
      {children}
    </div>
  );
}
