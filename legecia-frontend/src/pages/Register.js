import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import API from "api/axios";
import { motion } from "framer-motion";

export default function Register() {
  const [form, setForm] = useState({ u_username: "", u_email: "", password: "" });
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setSuccess("");
    setLoading(true);
    try {
      const res = await API.post("/register/", form);
      setSuccess(res.data.message || "Registration successful! Check your email.");
      setTimeout(() => navigate("/login"), 3000);
    } catch (err) {
      setError(err.response?.data?.error || err.response?.data?.u_email?.[0] || "Registration failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={pageStyle}>
      <motion.div
        initial={{ opacity: 0, y: 40 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        style={cardStyle}
      >
        <h1 style={titleStyle}>⬡ LEGECIA</h1>
        <p style={subtitleStyle}>Create Your Account</p>

        {error && <div style={errorStyle}>{error}</div>}
        {success && <div style={successStyle}>{success}</div>}

        <form onSubmit={handleSubmit}>
          <input
            style={inputStyle}
            placeholder="Username"
            value={form.u_username}
            onChange={(e) => setForm({ ...form, u_username: e.target.value })}
            required
          />
          <input
            style={inputStyle}
            type="email"
            placeholder="Email"
            value={form.u_email}
            onChange={(e) => setForm({ ...form, u_email: e.target.value })}
            required
          />
          <input
            style={inputStyle}
            type="password"
            placeholder="Password"
            value={form.password}
            onChange={(e) => setForm({ ...form, password: e.target.value })}
            required
          />
          <motion.button
            whileHover={{ scale: 1.02 }}
            whileTap={{ scale: 0.98 }}
            style={btnStyle}
            type="submit"
            disabled={loading}
          >
            {loading ? "Creating Account..." : "Register →"}
          </motion.button>
        </form>

        <p style={footerText}>
          Already have an account?{" "}
          <Link to="/login" style={linkStyle}>Sign In</Link>
        </p>
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
};

const cardStyle = {
  width: "100%",
  maxWidth: 400,
  padding: "50px 40px",
  borderRadius: "20px",
  background: "rgba(12,10,30,0.85)",
  border: "1px solid rgba(0,255,255,0.12)",
  boxShadow: "0 0 60px rgba(0,255,255,0.06)",
  backdropFilter: "blur(20px)",
};

const titleStyle = {
  textAlign: "center",
  fontSize: "32px",
  fontWeight: 800,
  letterSpacing: "4px",
  color: "#00ffff",
  marginBottom: 4,
  textShadow: "0 0 30px rgba(0,255,255,0.4)",
};

const subtitleStyle = {
  textAlign: "center",
  color: "#6a6a9a",
  fontSize: "13px",
  letterSpacing: "2px",
  marginBottom: 30,
};

const errorStyle = {
  background: "rgba(255,50,50,0.1)",
  border: "1px solid rgba(255,50,50,0.3)",
  color: "#ff6666",
  padding: "10px",
  borderRadius: "10px",
  fontSize: "13px",
  marginBottom: 16,
  textAlign: "center",
};

const successStyle = {
  background: "rgba(0,255,100,0.08)",
  border: "1px solid rgba(0,255,100,0.3)",
  color: "#00ff88",
  padding: "10px",
  borderRadius: "10px",
  fontSize: "13px",
  marginBottom: 16,
  textAlign: "center",
};

const inputStyle = {
  width: "100%",
  padding: "14px 16px",
  marginBottom: 16,
  borderRadius: "12px",
  border: "1px solid rgba(100,100,200,0.2)",
  background: "rgba(255,255,255,0.03)",
  color: "#e0e0ff",
  fontSize: "15px",
  outline: "none",
  boxSizing: "border-box",
};

const btnStyle = {
  width: "100%",
  padding: "14px",
  borderRadius: "12px",
  border: "none",
  background: "linear-gradient(135deg, #00c8ff, #7b2fff)",
  color: "#fff",
  fontWeight: 700,
  fontSize: "15px",
  cursor: "pointer",
  marginTop: 8,
};

const footerText = {
  textAlign: "center",
  marginTop: 24,
  color: "#6a6a9a",
  fontSize: "13px",
};

const linkStyle = {
  color: "#00ffff",
  textDecoration: "none",
  fontWeight: 600,
};
