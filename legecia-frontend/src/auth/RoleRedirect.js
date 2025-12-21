import { Navigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";
import { useEffect } from "react";

export default function RoleRedirect() {
  const { user } = useAuth();
  const navigate = useNavigate();

  useEffect(() => {
    if (!user) return;

    if (user.active_role === "USER") navigate("/dashboard/user");
    if (user.active_role === "GUARDIAN") navigate("/dashboard/guardian");
    if (user.active_role === "BENEFICIARY") navigate("/dashboard/beneficiary");
  }, [user, navigate]);

  return null;
}