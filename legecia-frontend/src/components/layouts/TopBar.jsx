import { useNavigate, Link } from "react-router-dom";
import { useAuth } from "context/AuthContext";
import { motion } from "framer-motion";

export default function TopBar() {
  const navigate = useNavigate();
  const { user, logout } = useAuth();

  return (
    <nav style={navStyle}>
      {/* LOGO */}
      <div onClick={() => navigate("/")} style={logoWrap}>
        <span style={logoText}>⬡ LEGECIA</span>
      </div>

      {/* NAV LINKS */}
      {user && (
        <div style={linksWrap}>
          <Link to="/dashboard" style={linkStyle}>Dashboard</Link>
          <Link to="/packages" style={linkStyle}>Packages</Link>
          <Link to="/notifications" style={linkStyle}>Notifications</Link>
          <Link to="/explorer" style={linkStyle}>Explorer</Link>

          <span style={roleChip}>{user.active_role}</span>

          <motion.button
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            onClick={logout}
            style={logoutBtn}
          >
            ⏻ Logout
          </motion.button>
        </div>
      )}
    </nav>
  );
}

const navStyle = {
  padding: "12px 30px",
  display: "flex",
  justifyContent: "space-between",
  alignItems: "center",
  borderBottom: "1px solid rgba(0,255,255,0.15)",
  backdropFilter: "blur(16px)",
  background: "rgba(5,4,10,0.6)",
};

const logoWrap = {
  cursor: "pointer",
  display: "flex",
  alignItems: "center",
};

const logoText = {
  fontSize: "22px",
  fontWeight: 800,
  letterSpacing: "3px",
  color: "#00ffff",
  textShadow: "0 0 20px rgba(0,255,255,0.6)",
};

const linksWrap = {
  display: "flex",
  alignItems: "center",
  gap: "20px",
};

const linkStyle = {
  color: "#9aa4ff",
  textDecoration: "none",
  fontSize: "14px",
  fontWeight: 500,
  transition: "color 0.2s",
};

const roleChip = {
  padding: "4px 12px",
  borderRadius: "20px",
  fontSize: "11px",
  fontWeight: 700,
  letterSpacing: "1px",
  border: "1px solid rgba(0,255,255,0.4)",
  color: "#00ffff",
  background: "rgba(0,255,255,0.08)",
};

const logoutBtn = {
  background: "transparent",
  border: "1px solid rgba(255,80,80,0.5)",
  color: "#ff5050",
  padding: "6px 14px",
  borderRadius: "8px",
  cursor: "pointer",
  fontSize: "13px",
  fontWeight: 600,
};
