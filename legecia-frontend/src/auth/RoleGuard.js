import { Navigate } from "react-router-dom";
import { useAuth } from "context/AuthContext";

export default function RoleGuard({ role, children }) {
  const { user } = useAuth();

  if (!user) {
    return <Navigate to="/login" replace />;
  }

  if (user.active_role !== role) {
    return <Navigate to="/dashboard" replace />;
  }

  return children;
}
