import { Link } from "react-router-dom";
import { motion } from "framer-motion";
import { useAuth } from "context/AuthContext";

export default function Home() {
  const { user } = useAuth();

  return (
    <div style={pageStyle}>
      <motion.div
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.7 }}
        style={heroWrap}
      >
        <h1 style={heroTitle}>⬡ LEGECIA</h1>
        <p style={heroSub}>
          Secure Digital Legacy Management — Protect what matters beyond time.
        </p>

        <div style={btnWrap}>
          {user ? (
            <Link to="/dashboard" style={primaryBtn}>Go to Dashboard →</Link>
          ) : (
            <>
              <Link to="/login" style={primaryBtn}>Sign In</Link>
              <Link to="/register" style={secondaryBtn}>Create Account</Link>
            </>
          )}
        </div>

        {/* Features grid */}
        <div style={featGrid}>
          {[
            { icon: "📦", title: "Packages", desc: "Create encrypted legacy packages with documents, credentials, and messages." },
            { icon: "🛡️", title: "Guardians", desc: "Assign trusted guardians to supervise and release your packages." },
            { icon: "🎯", title: "Milestones", desc: "Set time-based or event-based milestones for package delivery." },
            { icon: "🔔", title: "Notifications", desc: "Real-time alerts for all account and package activity." },
          ].map((f, i) => (
            <motion.div
              key={i}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.3 + i * 0.15 }}
              style={featCard}
            >
              <span style={{ fontSize: 32 }}>{f.icon}</span>
              <h3 style={featTitle}>{f.title}</h3>
              <p style={featDesc}>{f.desc}</p>
            </motion.div>
          ))}
        </div>
      </motion.div>
    </div>
  );
}

const pageStyle = {
  minHeight: "100vh",
  display: "flex",
  justifyContent: "center",
  alignItems: "center",
  background: "linear-gradient(135deg, #05040a 0%, #0a0e1a 50%, #0d0820 100%)",
  padding: "40px 20px",
};

const heroWrap = { textAlign: "center", maxWidth: 900 };

const heroTitle = {
  fontSize: 48,
  fontWeight: 900,
  letterSpacing: 6,
  color: "#00ffff",
  textShadow: "0 0 40px rgba(0,255,255,0.4)",
  marginBottom: 12,
};

const heroSub = {
  fontSize: 17,
  color: "#8a8abb",
  letterSpacing: 1,
  marginBottom: 36,
};

const btnWrap = { display: "flex", gap: 16, justifyContent: "center", marginBottom: 50 };

const primaryBtn = {
  padding: "14px 36px",
  borderRadius: 14,
  background: "linear-gradient(135deg, #00c8ff, #7b2fff)",
  color: "#fff",
  fontWeight: 700,
  fontSize: 15,
  textDecoration: "none",
};

const secondaryBtn = {
  padding: "14px 36px",
  borderRadius: 14,
  border: "1px solid rgba(0,255,255,0.3)",
  background: "transparent",
  color: "#00ffff",
  fontWeight: 700,
  fontSize: 15,
  textDecoration: "none",
};

const featGrid = {
  display: "grid",
  gridTemplateColumns: "repeat(auto-fit, minmax(200px, 1fr))",
  gap: 20,
};

const featCard = {
  padding: "28px 20px",
  borderRadius: 16,
  background: "rgba(12,10,30,0.7)",
  border: "1px solid rgba(0,255,255,0.08)",
  textAlign: "center",
};

const featTitle = {
  color: "#e0e0ff",
  fontSize: 16,
  fontWeight: 700,
  marginTop: 10,
  marginBottom: 6,
};

const featDesc = {
  color: "#6a6a9a",
  fontSize: 13,
  lineHeight: 1.5,
};
