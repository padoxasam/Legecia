import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { useAuth } from "context/AuthContext";
import API from "api/axios";
import { motion } from "framer-motion";

export default function Login() {
  const [form, setForm] = useState({ login: "", password: "" });
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();
  const { login } = useAuth();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setLoading(true);
    try {
      const res = await API.post("/login/", form);
      login(res.data.user, res.data.access_token, res.data.refresh_token);
      navigate("/dashboard");
    } catch (err) {
      setError(err.response?.data?.error || "Login failed");
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
        <p style={subtitleStyle}>Digital Legacy Management</p>

        {error && <div style={errorStyle}>{error}</div>}

        <form onSubmit={handleSubmit}>
          <input
            style={inputStyle}
            placeholder="Email or Username"
            value={form.login}
            onChange={(e) => setForm({ ...form, login: e.target.value })}
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
            {loading ? "Authenticating..." : "Sign In →"}
          </motion.button>
        </form>

        <p style={footerText}>
          Don't have an account?{" "}
          <Link to="/register" style={linkStyle}>Register</Link>
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
