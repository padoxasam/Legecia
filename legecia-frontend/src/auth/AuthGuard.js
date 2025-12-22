import { useAuth } from "../context/AuthContext";

export default function AuthGuard({ children }) {
  const { user } = useAuth();

  // DEV FALLBACK
  if (!user) {
    return children;
  }

  return children;
}
