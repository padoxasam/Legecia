import palette from "./palette";

export default function NeonButton({ label, onClick, small, disabled }) {
  return (
    <button
      disabled={disabled}
      onClick={onClick}
      style={{
        padding: small ? "6px 10px" : "8px 12px",
        borderRadius: "8px",
        background: `linear-gradient(90deg, ${palette.accent}, ${palette.accent2})`,
        border: "none",
        cursor: "pointer",
        fontWeight: 600,
        opacity: disabled ? 0.6 : 1,
      }}
    >
      {label}
    </button>
  );
}
