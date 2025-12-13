import { useState } from "react";
import NeonButton from "./NeonButton";

export default function GuardianToolBar({ onRefresh }) {
  const [loading, setLoading] = useState(false);

  const refresh = async () => {
    setLoading(true);
    try {
      if (onRefresh) {
        await onRefresh();
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      style={{
        display: "flex",
        gap: "12px",
        alignItems: "center",
        justifyContent: "space-between",
        marginBottom: "18px",
      }}
    >
      <h3 style={{ margin: 0 }}>Supervision Controls</h3>

      <NeonButton
        label={loading ? "Refreshing..." : "Refresh"}
        onClick={refresh}
        disabled={loading}
      />
    </div>
  );
}
