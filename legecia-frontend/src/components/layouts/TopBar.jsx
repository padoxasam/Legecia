import { useContext } from "react";
import { useNavigate } from "react-router-dom";
import LogoutButton from "components/LogoutButton";
import { AuthContext } from "context/AuthContext";
import logo from "../assets/logo.png";

export default function TopBar() {
  const navigate = useNavigate();
  const { auth } = useContext(AuthContext);

  const isAuthenticated = !!auth?.access;

  return (
    <div
      style={{
        padding: "15px 30px",
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        borderBottom: "1px solid rgba(0,255,255,0.3)",
        backdropFilter: "blur(12px)",
      }}
    >
      {/* LOGO ONLY */}
      <div
        onClick={() => navigate("/")}
        style={{
          display: "flex",
          alignItems: "center",
          cursor: "pointer",
        }}
      >
        <img
          src={logo}
          alt="Legecia Logo"
          style={{
            height: "56px",           // 🔥 bigger
            width: "56px",
            objectFit: "contain",
            background: "transparent", // 🔥 no white fill
            filter: "drop-shadow(0 0 10px rgba(0,255,255,0.8))",
          }}
        />
      </div>

      {isAuthenticated && <LogoutButton />}
    </div>
  );
}
