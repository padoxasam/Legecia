// src/layouts/CyberLayout.js
import LogoutButton from "components/LogoutButton";

function CyberLayout({ children }) {
  return (
    <div
      style={{
        minHeight: "100vh",
        background: "radial-gradient(circle at top, #020024, #00010F)",
        color: "#e0e0ff",
        fontFamily: "Orbitron",
      }}
    >
      {/* Top bar */}
      <div
        style={{
          padding: "15px 30px",
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          borderBottom: "1px solid rgba(0,255,255,0.3)",
        }}
      >
        <h3 style={{ color: "#00ffff" }}>LEGECIA</h3>
        <LogoutButton />
      </div>

      {/* Page content */}
      <div style={{ padding: "30px" }}>{children}</div>
    </div>
  );
}

export default CyberLayout;
