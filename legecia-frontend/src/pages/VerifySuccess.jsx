export default function VerifySuccess() {
  return (
    <div style={{
      minHeight: "100vh",
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      color: "white"
    }}>
      <div style={{
        padding: "25px",
        border: "1px solid #00ffff",
        borderRadius: "10px",
        textAlign: "center"
      }}>
        <h2 style={{ color: "#00ffff" }}>Email Verified 🎉</h2>
        <p>You can now log in to your account.</p>

        <a
          href="/login"
          style={{
            marginTop: "10px",
            display: "inline-block",
            padding: "10px 15px",
            background: "#00ffff",
            color: "#000",
            borderRadius: "8px",
            fontWeight: "bold",
          }}
        >
          Go to Login
        </a>
      </div>
    </div>
  );
}
