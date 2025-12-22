// src/pages/Login.jsx
import { useState, useContext } from "react";
import { useNavigate } from "react-router-dom";
import axios from "api/axios"; 

import { AuthContext } from "context/AuthContext";

export default function Login() {
  const navigate = useNavigate();
  const { setAuth } = useContext(AuthContext);

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setLoading(true);

    try {
      const res = await axios.post("/login/", {
        username,
        password,
      });

      const { access_token, refresh_token, user } = res.data;

      // 🔐 Store auth globally
      setAuth({
        access: access_token,
        refresh: refresh_token,
        user,
      });

      // 💾 Persist session
      localStorage.setItem("access", access_token);
      localStorage.setItem("refresh", refresh_token);
      localStorage.setItem("user", JSON.stringify(user));

      // 🚀 Redirect (RoleRedirect will handle dashboard)
      navigate("/dashboard");
    } catch (err) {
      if (err.response?.data?.error) {
        setError(err.response.data.error);
      } else if (err.response?.data) {
        setError(JSON.stringify(err.response.data));
      } else {
        setError("Login failed. Please try again.");
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      style={{
        minHeight: "100vh",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        background: "#050b14",
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
          style={{
            width: "100%",
            padding: "12px",
            background: "#00ffff",
            border: "none",
            cursor: "pointer",
            fontWeight: "bold",
          }}
        >
          {loading ? "Signing in..." : "Login"}
        </button>
      </form>
    </div>
  );
}

const inputStyle = {
  width: "100%",
  padding: "10px",
  marginBottom: "15px",
  background: "transparent",
  border: "1px solid rgba(0,255,255,0.4)",
  color: "#00ffff",
};
