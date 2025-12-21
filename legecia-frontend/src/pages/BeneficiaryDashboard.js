import TopBar from "../../components/layout/TopBar";

export default function BeneficiaryDashboard() {
  return (
    <div style={{ minHeight: "100vh", background: "#05040a", color: "#00ffff" }}>
      <TopBar />

      <div style={{ padding: "30px" }}>
        <h2 style={{ letterSpacing: "2px" }}>BENEFICIARY DASHBOARD</h2>

        <div
          style={{
            marginTop: "30px",
            padding: "20px",
            border: "1px solid rgba(0,255,255,0.4)",
            borderRadius: "10px",
            backdropFilter: "blur(12px)",
            maxWidth: "500px",
          }}
        >
          <h4>My Supervised Packages</h4>
          <p style={{ fontSize: "14px", opacity: 0.8 }}>
            View supervision details and guardian actions.
          </p>
        </div>
      </div>
    </div>
  );
}
