import { Navigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export default function RoleGuard({ role, children }) {
  const { user } = useAuth();

  if (!user) {
    return <Navigate to="/login" replace />;
  }

  if (user.account_type !== role) {
    return <Navigate to="/" replace />;
  }

  return children;
}
