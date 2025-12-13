import NeonCard from "./NeonCard";
import palette from "./palette";

export default function Metric({ title, value, hint }) {
  return (
    <NeonCard style={{ minWidth: "160px" }}>
      <div style={{ display: "flex", justifyContent: "space-between" }}>
        <small style={{ color: palette.muted }}>{title}</small>
        <h3 style={{ margin: 0 }}>{value}</h3>
      </div>
      <small style={{ color: palette.muted }}>{hint}</small>
    </NeonCard>
  );
}
