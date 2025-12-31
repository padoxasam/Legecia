import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

/* ================= AUTH ================= */
import AuthGuard from "auth/AuthGuard";
import RoleGuard from "auth/RoleGuard";
import RoleRedirect from "auth/RoleRedirect";
import VerifySuccess from "pages/VerifySuccess";
/* ================= LAYOUT ================= */
import CyberLayout from "components/layouts/CyberLayout";

/* ================= PUBLIC ================= */
import Login from "pages/Login";
import Register from "pages/Register";

/* ================= CORE ================= */
import Home from "pages/Home";
import Notification from "pages/Notification";
import VerifyEmail from "pages/Verify";
/* ================= DASHBOARDS ================= */
import UserDashboard from "pages/UserDashboard";
import GuardianDashboard from "pages/GuardianDashboard";
import BeneficiaryDashboard from "pages/BeneficiaryDashboard";

/* ================= SUPERVISION ================= */
import CreateSupervision from "pages/supervision/CreateSupervision";
import GuardianReview from "pages/supervision/GuardianReview";

/* ================= EXPLORER ================= */
import PublicPackageExplorer from "pages/explorer/PublicPackageExplorer";
import CreateExplorerListing from "pages/explorer/CreateExplorerListing";
import ExplorerDetail from "pages/explorer/ExplorerDetail";

/* ================= COMMUNICATION ================= */
import CommunicationPage from "pages/communication/CommunicationPage";

/* ================= ADMIN ================= */
import AccessLogsPage from "pages/admin/AccessLogsPage";
import CredentialsPage from "pages/admin/CredentialsPage";

function App() {
  return (
    <Router>
      <Routes>

        {/* ================= PUBLIC ================= */}
        <Route
          path="/login"
          element={
            <CyberLayout>
              <Login />
            </CyberLayout>
          }
        />

        <Route
          path="/register"
          element={
            <CyberLayout>
              <Register />
            </CyberLayout>
          }
        />
        {/* ✅ EMAIL VERIFICATION (PUBLIC) */}
<Route path="/verify/:uid/:token" element={<VerifyEmail />} />
<Route path="/verify-success" element={<VerifySuccess />} />
        {/* ================= ROLE REDIRECT ================= */}
        <Route
          path="/dashboard"
          element={
            <AuthGuard>
              <RoleRedirect />
            </AuthGuard>
          }
        />

        {/* ================= HOME ================= */}
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

        {/* ================= USER ================= */}
        <Route
          path="/user/dashboard"
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

        {/* ================= GUARDIAN ================= */}
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

        {/* ================= BENEFICIARY ================= */}
        <Route
          path="/beneficiary/dashboard"
          element={
            <AuthGuard>
              <RoleGuard role="BENEFICIARY">
                <CyberLayout>
                  <BeneficiaryDashboard />
                </CyberLayout>
              </RoleGuard>
            </AuthGuard>
          }
        />
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
        {/* ================= COMMUNICATION ================= */}
        <Route
          path="/communication"
          element={
            <AuthGuard>
              <CyberLayout>
                <CommunicationPage />
              </CyberLayout>
            </AuthGuard>
          }
        />

        {/* ================= EXPLORER ================= */}
        <Route
          path="/explorer"
          element={
            <AuthGuard>
              <CyberLayout>
                <PublicPackageExplorer />
              </CyberLayout>
            </AuthGuard>
          }
        />

        <Route
          path="/explorer/create"
          element={
            <AuthGuard>
              <CyberLayout>
                <CreateExplorerListing />
              </CyberLayout>
            </AuthGuard>
          }
        />

        <Route
          path="/explorer/:id"
          element={
            <AuthGuard>
              <CyberLayout>
                <ExplorerDetail />
              </CyberLayout>
            </AuthGuard>
          }
        />

        {/* ================= ADMIN ================= */}
        <Route
          path="/admin/access-logs"
          element={
            <AuthGuard>
              <RoleGuard role="ADMIN">
                <CyberLayout>
                  <AccessLogsPage />
                </CyberLayout>
              </RoleGuard>
            </AuthGuard>
          }
        />

        <Route
          path="/admin/credentials"
          element={
            <AuthGuard>
              <RoleGuard role="ADMIN">
                <CyberLayout>
                  <CredentialsPage />
                </CyberLayout>
              </RoleGuard>
            </AuthGuard>
          }
        />

      </Routes>
    </Router>
  );
}

export default App;
