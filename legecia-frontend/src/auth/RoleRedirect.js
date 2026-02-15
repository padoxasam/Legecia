import { useAuth } from "context/AuthContext";
import { Navigate } from "react-router-dom";

export default function RoleRedirect() {
  const { user } = useAuth();

  if (!user) return <Navigate to="/login" replace />;

  if (user.active_role === "USER") return <Navigate to="/user/dashboard" replace />;
  if (user.active_role === "GUARDIAN") return <Navigate to="/guardian/dashboard" replace />;
  if (user.active_role === "BENEFICIARY") return <Navigate to="/beneficiary/dashboard" replace />;

  return <Navigate to="/" replace />;
}
