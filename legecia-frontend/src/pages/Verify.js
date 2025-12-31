import { useParams, useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
import axios from "../utils/api";

export default function VerifyEmail() {
  const { uid, token } = useParams();
  const navigate = useNavigate();

  const [status, setStatus] = useState("loading");
  const [email, setEmail] = useState("");
  const [cooldown, setCooldown] = useState(0);
  const [sending, setSending] = useState(false);

  /* ================= VERIFY TOKEN ================= */
  useEffect(() => {
    axios
      .get(`/verify-email/${uid}/${token}/`)
      .then(() => {
        setStatus("success");

        // 🔁 Auto-redirect after 3s
        setTimeout(() => navigate("/login"), 3000);
      })
      .catch(() => setStatus("error"));
  }, [uid, token, navigate]);

  /* ================= COOLDOWN TIMER ================= */
  useEffect(() => {
    if (cooldown === 0) return;
    const timer = setInterval(() => {
      setCooldown(c => c - 1);
    }, 1000);
    return () => clearInterval(timer);
  }, [cooldown]);

  /* ================= RESEND ================= */
  const resend = async () => {
    if (!email) {
      alert("Enter your email");
      return;
    }

    try {
      setSending(true);
      await axios.post("/resend-verification/", { email });
      alert("Verification email sent.");
      setCooldown(60); // ⏱ start cooldown
    } catch {
      alert("Too many attempts. Try again later.");
    } finally {
      setSending(false);
    }
  };

  /* ================= UI STATES ================= */
  if (status === "loading") {
    return <h2 style={{ color: "white" }}>Verifying...</h2>;
  }

  if (status === "success") {
    return (
      <h2 style={{ color: "#00ffff" }}>
        Email verified 🎉 Redirecting to login...
      </h2>
    );
  }

  return (
    <div style={{ color: "white", textAlign: "center" }}>
      <h2>Invalid or expired link</h2>

      <input
        placeholder="Enter your email"
        value={email}
        onChange={e => setEmail(e.target.value)}
        style={{ padding: "10px", marginTop: "10px" }}
      />

      <button
        type="button"
        onClick={resend}
        disabled={cooldown > 0 || sending}
        style={{
          marginTop: "10px",
          padding: "10px",
          border: "1px dashed #00ffff",
          background: "transparent",
          color: cooldown > 0 ? "#555" : "#00ffff",
          cursor: cooldown > 0 ? "not-allowed" : "pointer",
        }}
      >
        {cooldown > 0
          ? `Resend available in ${cooldown}s`
          : sending
          ? "Sending..."
          : "Resend verification email"}
      </button>
    </div>
  );
}
