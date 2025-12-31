import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import axios from "api/axios";
import { useAuth } from "context/AuthContext";
import VantaBackground from "../components/VantaBackground";

export default function Login() {
  const navigate = useNavigate();
  const { setUser } = useAuth();

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setLoading(true);

    try {
      const res = await axios.post("/login/", { username, password });

      const { access_token, refresh_token, user } = res.data;

      localStorage.setItem("access", access_token);
      localStorage.setItem("refresh", refresh_token);
      localStorage.setItem("user", JSON.stringify(user));

      setUser(user);
      navigate("/dashboard");
    } catch (err) {
      setError(
        err.response?.data?.error ||
        "Login failed. Please try again."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      {/* 🌌 Dynamic Background */}
      <VantaBackground />

      {/* 🧩 Login Card */}
      <div
        style={{
          minHeight: "100vh",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          position: "relative",
          zIndex: 10,
        }}
      >
        <form
          onSubmit={handleSubmit}
          style={{
            width: "360px",
            padding: "30px",
            border: "1px solid rgba(0,255,255,0.3)",
            borderRadius: "10px",
            backdropFilter: "blur(12px)",
            background: "rgba(5, 11, 20, 0.6)",
          }}
        >
          <h2 style={{ color: "#00ffff", textAlign: "center" }}>
            LEGECIA LOGIN
          </h2>

          {error && (
            <div style={{ color: "#ff4d4d", marginBottom: "15px" }}>
              {error}
            </div>
          )}

          <input
            type="text"
            placeholder="Username or Email"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            style={inputStyle}
          />

          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            style={inputStyle}
          />

          <button
            type="submit"
            disabled={loading}
            style={buttonStyle}
          >
            {loading ? "Signing in..." : "Login"}
          </button>

          <div style={{ marginTop: "20px", textAlign: "center" }}>
            <span style={{ color: "#9aa4ff" }}>
              Didn’t register before?
            </span>
            <br />
            <Link
              to="/register"
              style={{
                color: "#00ffff",
                fontWeight: "bold",
                textDecoration: "none",
                textShadow: "0 0 6px rgba(0,255,255,0.7)",
              }}
            >
              Register now!
            </Link>
          </div>
        </form>
      </div>
    </>
  );
}

const inputStyle = {
  width: "100%",
  padding: "10px",
  marginBottom: "15px",
  border: "1px solid rgba(0,255,255,0.4)",
  color: "#00ffff",
};

const buttonStyle = {
  width: "100%",
  padding: "12px",
  background: "#00ffff",
  border: "none",
  cursor: "pointer",
  fontWeight: "bold",
};
