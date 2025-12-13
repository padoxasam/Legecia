// src/components/NotificationCard.js
import { motion } from "framer-motion";

function NotificationCard({ data }) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 15 }}
      animate={{ opacity: 1, y: 0 }}
      style={{
        backdropFilter: "blur(10px)",
        background: "rgba(255,255,255,0.05)",
        border: "1px solid rgba(0,255,255,0.3)",
        borderRadius: "16px",
        padding: "16px",
        boxShadow: "0 0 20px rgba(0,255,255,0.15)",
      }}
    >
      <h5 style={{ color: "#00eaff" }}>
        {data.priority} — {data.topic}
      </h5>
      <p>{data.message}</p>
      <small style={{ opacity: 0.7 }}>
        {new Date(data.created_at).toLocaleString()}
      </small>
    </motion.div>
  );
}

export default NotificationCard;
