import { Navigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export default function RoleRedirect() {
  const { user } = useAuth();

  if (!user) return null;

  switch (user.active_role) {
    case "GUARDIAN":
      return <Navigate to="/guardian/dashboard" replace />;
    case "BENEFICIARY":
      return <Navigate to="/beneficiary/dashboard" replace />;
    default:
      return <Navigate to="/dashboard/user" replace />;
  }
}
