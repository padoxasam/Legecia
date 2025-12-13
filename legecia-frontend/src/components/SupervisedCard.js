import { useState } from "react";
import NeonButton from "./NeonButton";

export default function SupervisionCard({ supervision, onAction }) {
  const [busy, setBusy] = useState(false);
  const [message, setMessage] = useState("");

  const doAction = async (action, payload = null) => {
    setBusy(true);
    try {
      if (onAction) {
        await onAction(supervision.id, action, payload);
      }
      setMessage(`${action} successfully executed!`);
    } catch (e) {
      setMessage(`${action} failed ❌: ${e.message || e}`);
    } finally {
      setBusy(false);
    }
  };

  return (
    <div
      style={{
        padding: "18px",
        borderRadius: "14px",
        background:
          "linear-gradient(180deg, rgba(255,255,255,0.06), rgba(255,255,255,0.03))",
        border: "1px solid rgba(255,255,255,0.06)",
        boxShadow: "0 8px 30px rgba(8,12,20,0.5)",
        color: "#f6fbff",
        minWidth: "320px",
      }}
    >
      {/* Header */}
      <div style={{ display: "flex", justifyContent: "space-between" }}>
        <h3>{supervision.pack_name || "—"}</h3>
        <span
          style={{
            padding: "6px 10px",
            borderRadius: "999px",
            fontSize: "12px",
            background: "#ffffff20",
          }}
        >
          {supervision.guardian_status || "Unknown"}
        </span>
      </div>

      {/* Meta */}
      <p style={{ fontSize: "13px" }}>
        Owner: {supervision.user?.full_name || supervision.user?.username}
      </p>
      <p style={{ fontSize: "13px" }}>
        Beneficiary:{" "}
        {supervision.beneficiary?.full_name ||
          supervision.beneficiary?.username}
      </p>

      {/* Actions */}
      <div style={{ display: "flex", gap: "8px", marginTop: "12px" }}>
        <NeonButton label="View" onClick={() => doAction("view_package")} />
        <NeonButton label="Grant" onClick={() => doAction("approve")} />
        <NeonButton label="Extend" onClick={() => doAction("extend")} />
        <NeonButton label="Release" onClick={() => doAction("release")} />
      </div>

      {/* Message */}
      <small style={{ marginTop: "8px", display: "block" }}>{message}</small>
    </div>
  );
}
