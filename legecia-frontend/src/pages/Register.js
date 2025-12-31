import { useState } from "react";
import { Link } from "react-router-dom";
import axios from "../utils/api";
import { FaEye, FaEyeSlash } from "react-icons/fa";

export default function Register() {
  const [form, setForm] = useState({
    username: "",
    email: "",
    password1: "",
    password2: "",
  });

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [message, setMessage] = useState("");

  // 👁 password visibility states
  const [showPassword1, setShowPassword1] = useState(false);
  const [showPassword2, setShowPassword2] = useState(false);

  const submit = async (e) => {
    e.preventDefault();
    setError("");
    setMessage("");
    setLoading(true);

    try {
  const res = await axios.post("/auth/register/", form);
  setMessage(res.data.message || "Registration successful. Check your email.");
} catch (err) {
  const data = err.response?.data;

  if (!data) {
    setError("Server unavailable. Please try again.");
  } else if (typeof data === "object") {
    const messages = [];

    Object.values(data).forEach((value) => {
      if (Array.isArray(value)) messages.push(value[0]);
      else if (typeof value === "string") messages.push(value);
    });

    setError(messages.join(" • "));
  } else {
    setError("Registration failed");
  }
}

 finally {
      setLoading(false);
    }
  };

  return (
    <div style={pageStyle}>
      <form onSubmit={submit} style={cardStyle}>
        <h2 style={titleStyle}>Create Account</h2>
        <p style={subtitleStyle}>
          Secure your digital legacy with LEGECIA
        </p>

        {error && <div style={errorStyle}>{error}</div>}
        {message && <div style={successStyle}>{message}</div>}

        <input
          style={inputStyle}
          placeholder="Username"
          value={form.username}
          onChange={(e) =>
            setForm({ ...form, username: e.target.value })
          }
          required
        />

        <input
          style={inputStyle}
          placeholder="Email address"
          type="email"
          value={form.email}
          onChange={(e) =>
            setForm({ ...form, email: e.target.value })
          }
          required
        />

        {/* 🔐 PASSWORD */}
        <div style={{ position: "relative" }}>
          <input
            style={inputStyle}
            placeholder="Password"
            type={showPassword1 ? "text" : "password"}
            value={form.password1}
            onChange={(e) =>
              setForm({ ...form, password1: e.target.value })
            }
            required
          />
          <span
            onClick={() => setShowPassword1(!showPassword1)}
            style={eyeStyle}
          >
            {showPassword1 ? <FaEyeSlash /> : <FaEye />}
          </span>
        </div>

        {/* 🔐 REPEAT PASSWORD */}
        <div style={{ position: "relative" }}>
          <input
            style={inputStyle}
            placeholder="Repeat password"
            type={showPassword2 ? "text" : "password"}
            value={form.password2}
            onChange={(e) =>
              setForm({ ...form, password2: e.target.value })
            }
            required
          />
          <span
            onClick={() => setShowPassword2(!showPassword2)}
            style={eyeStyle}
          >
            {showPassword2 ? <FaEyeSlash /> : <FaEye />}
          </span>
        </div>

        <button type="submit" style={buttonStyle} disabled={loading}>
          {loading ? "Creating account..." : "Create Account"}
        </button>

        <div style={footerStyle}>
          Already have an account?
          <Link to="/login" style={linkStyle}>
            Sign in
          </Link>
        </div>
      </form>
    </div>
  );
}

/* ================= STYLES ================= */

const pageStyle = {
  minHeight: "100vh",
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
};

const cardStyle = {
  width: "380px",
  padding: "30px",
  border: "1px solid rgba(0,255,255,0.4)",
  borderRadius: "12px",
  backdropFilter: "blur(14px)",
};

const titleStyle = {
  color: "#00ffff",
  textAlign: "center",
  fontFamily: "sans-serif",
};

const subtitleStyle = {
  color: "#cedadaff",
  textAlign: "center",
  fontFamily: "sans-serif",
  marginBottom: "20px",
};

const errorStyle = {
  color: "#ff4d4d",
  marginBottom: "15px",
  textAlign: "center",
    fontFamily: "sans-serif",

};

const successStyle = {
  color: "#00ffff",
  marginBottom: "15px",
  textAlign: "center",
};

const inputStyle = {
  width: "100%",
  fontFamily: "sans-serif",
  padding: "20px",
  marginBottom: "15px",
  background: "transparent",
  border: "1px solid rgba(0,255,255,0.4)",
  color: "#00ffff",
};

const eyeStyle = {
  position: "absolute",
  right: "12px",
  top: "50%",
  transform: "translateY(-50%)",
  cursor: "pointer",
  color: "#00ffff",
};

const buttonStyle = {
  width: "100%",
  fontFamily: "Georgia",
  padding: "12px",
  background: "#00ffff",
  border: "none",
  cursor: "pointer",
  fontWeight: "bold",
};

const footerStyle = {
  marginTop: "20px",
  fontFamily: "Impact",
  textAlign: "center",
  color: "#f110d3ff",
};

const linkStyle = {
  marginLeft: "6px",
  color: "#00ffff",
  textDecoration: "none",
};
