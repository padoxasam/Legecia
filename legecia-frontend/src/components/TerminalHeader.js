import palette from "./palette";

export default function TerminalHeader({ title, subtitle }) {
  return (
    <div
      style={{
        padding: "10px 16px",
        borderBottom: "1px solid rgba(255,255,255,0.04)",
        boxShadow: palette.glow,
      }}
    >
      <div style={{ display: "flex", gap: "12px", alignItems: "center" }}>
        <span
          style={{
            width: "10px",
            height: "10px",
            borderRadius: "50%",
            background: palette.accent,
          }}
        />
        <h2 style={{ margin: 0 }}>{title}</h2>
      </div>
      <small style={{ color: palette.muted }}>{subtitle}</small>
    </div>
  );
}
