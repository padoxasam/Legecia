import TopBar from "./TopBar";

export default function CyberLayout({ children }) {
  return (
    <div style={wrapperStyle}>
      <TopBar />
      <main style={mainStyle}>{children}</main>
    </div>
  );
}

const wrapperStyle = {
  minHeight: "100vh",
  background: "linear-gradient(135deg, #05040a 0%, #0a0e1a 50%, #0d0820 100%)",
  color: "#e0e0ff",
  fontFamily: "'Inter', 'Segoe UI', sans-serif",
};

const mainStyle = {
  padding: "30px",
  maxWidth: 1200,
  margin: "0 auto",
};
