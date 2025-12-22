// src/components/ui/GlassCard.jsx

export default function GlassCard({ title, children }) {
  return (
    <div style={styles.card}>
      {title && <h3 style={styles.title}>{title}</h3>}
      <div>{children}</div>
    </div>
  );
}

const styles = {
  card: {
    background: "rgba(255, 255, 255, 0.08)",
    backdropFilter: "blur(12px)",
    WebkitBackdropFilter: "blur(12px)",
    borderRadius: "16px",
    padding: "20px",
    marginBottom: "20px",
    border: "1px solid rgba(255, 255, 255, 0.15)",
    boxShadow: "0 8px 32px rgba(0,0,0,0.3)",
    color: "#fff",
  },
  title: {
    marginBottom: "12px",
    fontSize: "18px",
    fontWeight: "600",
    borderBottom: "1px solid rgba(255,255,255,0.2)",
    paddingBottom: "8px",
  },
};
