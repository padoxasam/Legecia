import TopBar from "../../components/layout/TopBar";

export default function GuardianDashboard() {
  return (
    <div style={{ minHeight: "100vh", background: "#05040a", color: "#00ffff" }}>
      <TopBar />

      <div style={{ padding: "30px" }}>
        <h2 style={{ letterSpacing: "2px" }}>GUARDIAN DASHBOARD</h2>

        <div style={{ display: "flex", gap: "20px", marginTop: "30px" }}>
          <DashboardCard
            title="Supervision Requests"
            description="Approve or reject incoming requests"
          />

          <DashboardCard
            title="Active Supervisions"
            description="Manage approved supervised packages"
          />
        </div>
      </div>
    </div>
  );
}

function DashboardCard({ title, description }) {
  return (
    <div
      style={{
        width: "260px",
        padding: "20px",
        border: "1px solid rgba(0,255,255,0.4)",
        borderRadius: "10px",
        backdropFilter: "blur(12px)",
      }}
    >
      <h4>{title}</h4>
      <p style={{ fontSize: "14px", opacity: 0.8 }}>{description}</p>
      <button style={buttonStyle}>OPEN</button>
    </div>
  );
}

const buttonStyle = {
  marginTop: "12px",
  background: "transparent",
  border: "1px solid #00ffff",
  color: "#00ffff",
  padding: "8px 16px",
  cursor: "pointer",
};
