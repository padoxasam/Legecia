import { useState } from "react";
import NeonButton from "./NeonButton";

export default function GuardianToolBar({ onRefresh }) {
  const [loading, setLoading] = useState(false);

  const refresh = async () => {
    setLoading(true);
    await onRefresh();
    setTimeout(() => setLoading(false), 400);
  };

  return (
    <div
      style={{
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        padding: "14px 18px",
        borderRadius: "12px",
        background: "linear-gradient(135deg,#0f2027,#203a43,#2c5364)",
        boxShadow: "0 0 20px rgba(0,255,255,0.15)",
        marginBottom: "20px",
      }}
    >
      <h3 style={{ margin: 0, color: "#9ff" }}>
        Guardian Supervision Panel
      </h3>

      <NeonButton
        label={loading ? "Syncing..." : "Refresh"}
        onClick={refresh}
        disabled={loading}
      />
    </div>
  );
}
