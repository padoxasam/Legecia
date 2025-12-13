// src/components/LogoutButton.js
import { motion } from "framer-motion";

function LogoutButton() {
  const logout = () => {
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");
    localStorage.removeItem("username");
    window.location.href = "/login";
  };

  return (
    <motion.button
      whileHover={{ scale: 1.1 }}
      whileTap={{ scale: 0.95 }}
      onClick={logout}
      style={{
        background: "transparent",
        border: "1px solid #00ffff",
        color: "#00ffff",
        padding: "8px 14px",
        borderRadius: "12px",
        boxShadow: "0 0 15px #00ffff",
        cursor: "pointer",
      }}
    >
      ⏻ Logout
    </motion.button>
  );
}

export default LogoutButton;
