import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

/* Guards */
import AuthGuard from "./auth/AuthGuard";
import RoleGuard from "./auth/RoleGuard";

/* Pages */
import Home from "./pages/Home";
import Login from "./pages/Login";
import UserDashboard from "./pages/UserDashboard";
import GuardianDashboard from "./pages/GuardianDashboard";
import GuardianReview from "./pages/supervision/GuardianReview";
import CreateSupervision from "./pages/supervision/CreateSupervision";
import Notification from "./pages/Notification";

/* Layout */
import CyberLayout from "./layouts/CyberLayout";

function App() {
  return (
    <Router>
      <Routes>

        {/* PUBLIC */}
        <Route path="/login" element={<Login />} />

        {/* HOME (any authenticated user) */}
        <Route
          path="/"
          element={
            <AuthGuard>
              <CyberLayout>
                <Home />
              </CyberLayout>
            </AuthGuard>
          }
        />
        {/* ✅ ROLE SMART ENTRY (INSERT HERE) */}
          <Route
          path="/dashboard"
        element={
          <AuthGuard>
          <RoleRedirect />
        </AuthGuard>
          }
    />
        {/* USER DASHBOARD */}
        <Route
          path="/dashboard"
          element={
            <AuthGuard>
              <RoleGuard role="USER">
                <CyberLayout>
                  <UserDashboard />
                </CyberLayout>
              </RoleGuard>
            </AuthGuard>
          }
        />

        {/* CREATE SUPERVISION (USER) */}
        <Route
          path="/supervision/create"
          element={
            <AuthGuard>
              <RoleGuard role="USER">
                <CyberLayout>
                  <CreateSupervision />
                </CyberLayout>
              </RoleGuard>
            </AuthGuard>
          }
        />

        {/* GUARDIAN DASHBOARD */}
        <Route
          path="/guardian/dashboard"
          element={
            <AuthGuard>
              <RoleGuard role="GUARDIAN">
                <CyberLayout>
                  <GuardianDashboard />
                </CyberLayout>
              </RoleGuard>
            </AuthGuard>
          }
        />

        {/* GUARDIAN REVIEW */}
        <Route
          path="/guardian/review"
          element={
            <AuthGuard>
              <RoleGuard role="GUARDIAN">
                <CyberLayout>
                  <GuardianReview />
                </CyberLayout>
              </RoleGuard>
            </AuthGuard>
          }
        />

        {/* NOTIFICATIONS */}
        <Route
          path="/notifications"
          element={
            <AuthGuard>
              <CyberLayout>
                <Notification />
              </CyberLayout>
            </AuthGuard>
          }
        />

      </Routes>
    </Router>
  );
}

export default App;
