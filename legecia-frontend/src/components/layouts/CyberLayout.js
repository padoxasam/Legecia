// src/layouts/CyberLayout.js
import VantaBackground from "components/VantaBackground";
import TopBar from "./TopBar";

function CyberLayout({ children }) {

  return (
    <div
      style={{
        minHeight: "100vh",
        position: "relative", 
        color: "#e0e0ff",
        fontFamily: "Orbitron",
        overflow: "hidden",
      }}
    >
      <VantaBackground />

      <div style={{ position: "relative", zIndex: 10 }}>
        {/* ✅ SINGLE TOP BAR (no duplication) */}
        <TopBar />

        <div style={{ padding: "30px" }}>
          {children}
        </div>
      </div>
    </div>
  );
}

export default CyberLayout;
