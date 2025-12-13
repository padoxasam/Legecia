import LogoutButton from "../auth/LogoutButton";

export default function TopBar() {
  return (
    <div
      style={{
        padding: "15px 30px",
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        borderBottom: "1px solid rgba(0,255,255,0.3)",
        backdropFilter: "blur(12px)",
      }}
    >
      <h3 style={{ color: "#00ffff", letterSpacing: "2px" }}>
        LEGECIA
      </h3>
      <LogoutButton />
    </div>
  );
}
