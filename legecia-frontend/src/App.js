import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

/* ================= AUTH ================= */
import AuthGuard from "auth/AuthGuard";
import RoleGuard from "auth/RoleGuard";
import RoleRedirect from "auth/RoleRedirect";

/* ================= LAYOUT ================= */
import CyberLayout from "components/layouts/CyberLayout";

/* ================= PUBLIC ================= */
import Login from "pages/Login";

/* ================= CORE ================= */
import Home from "pages/Home";
import Notification from "pages/Notification";

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
import SystemLogsPage from "pages/admin/SystemLogsPage";

/* ================= MILESTONE ================= */
import CreateMilestone from "pages/milestone/CreateMilestone";
import UploadMilestone from "pages/milestone/UploadMilestone";
import MilestoneDetail from "pages/milestone/MilestoneDetails";

/* ================= PACKAGES ================= */
import PackagesPage from "pages/packages/PackagesPage";

function App() {
  return (
    <Router>
      <Routes>

        {/* ===== PUBLIC ===== */}
        <Route path="/login" element={<Login />} />

        {/* ===== ROLE REDIRECT ===== */}
        <Route
          path="/dashboard"
          element={
            <AuthGuard>
              <RoleRedirect />
            </AuthGuard>
          }
        />

        {/* ===== HOME ===== */}
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

        {/* ===== USER ===== */}
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

        {/* ===== GUARDIAN ===== */}
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

        {/* ===== BENEFICIARY ===== */}
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

        {/* ===== NOTIFICATIONS ===== */}
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

        {/* ===== COMMUNICATION ===== */}
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

        {/* ===== EXPLORER ===== */}
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

        {/* ===== MILESTONE ===== */}
        <Route path="/milestone/create" element={<CreateMilestone />} />
        <Route path="/milestone/upload/:milestoneId" element={<UploadMilestone />} />
        <Route path="/milestone/:milestoneId" element={<MilestoneDetail />} />

        {/* ===== PACKAGES ===== */}
        <Route path="/packages" element={<PackagesPage />} />

        {/* ===== ADMIN ===== */}
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

        <Route
          path="/logs"
          element={
            <AuthGuard>
              <SystemLogsPage />
            </AuthGuard>
          }
        />

      </Routes>
    </Router>
  );
}
export default App;
