import { BrowserRouter, Routes, Route } from "react-router-dom";
import { AuthProvider } from "context/AuthContext";
import AuthGuard from "auth/AuthGuard";
import RoleRedirect from "auth/RoleRedirect";
import CyberLayout from "components/layouts/CyberLayout";

// Public pages
import Home from "pages/Home";
import Login from "pages/Login";
import Register from "pages/Register";
import Verify from "pages/Verify";
import VerifySuccess from "pages/VerifySuccess";

// Dashboards
import UserDashboard from "pages/UserDashboard";
import GuardianDashboard from "pages/GuardianDashboard";
import BeneficiaryDashboard from "pages/BeneficiaryDashboard";

// Feature pages
import PackagesPage from "pages/packages/PackagesPage";
import NotificationPage from "pages/Notification";
import CommunicationPage from "pages/communication/CommunicationPage";
import CommunicationForm from "pages/communication/CommunicationForm";

// Milestones
import CreateMilestone from "pages/milestone/CreateMilestone";
import MilestoneDetails from "pages/milestone/MilestoneDetails";
import UploadMilestone from "pages/milestone/uploadMilestone";

// Supervision
import CreateSupervision from "pages/supervision/CreateSupervision";
import GuardianReview from "pages/supervision/GuardianReview";

// Explorer
import PublicPackageExplorer from "pages/explorer/PublicPackageExplorer";
import CreateExplorerListing from "pages/explorer/CreateExplorerListing";
import ExplorerDetail from "pages/explorer/ExplorerDetail";

// Admin
import AccessLogsPage from "pages/admin/AccessLogsPage";
import CredentialsPage from "pages/admin/CredentialsPage";
import SystemLogsPage from "pages/admin/SystemLogsPage";

function ProtectedLayout({ children }) {
  return (
    <AuthGuard>
      <CyberLayout>{children}</CyberLayout>
    </AuthGuard>
  );
}

export default function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Routes>
          {/* Public */}
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/verify/:uid/:token" element={<Verify />} />
          <Route path="/verify-success" element={<VerifySuccess />} />

          {/* Smart redirect based on role */}
          <Route path="/dashboard" element={<AuthGuard><RoleRedirect /></AuthGuard>} />

          {/* Dashboards */}
          <Route path="/user/dashboard" element={<ProtectedLayout><UserDashboard /></ProtectedLayout>} />
          <Route path="/guardian/dashboard" element={<ProtectedLayout><GuardianDashboard /></ProtectedLayout>} />
          <Route path="/beneficiary/dashboard" element={<ProtectedLayout><BeneficiaryDashboard /></ProtectedLayout>} />

          {/* Packages */}
          <Route path="/packages" element={<ProtectedLayout><PackagesPage /></ProtectedLayout>} />

          {/* Notifications */}
          <Route path="/notifications" element={<ProtectedLayout><NotificationPage /></ProtectedLayout>} />

          {/* Communication */}
          <Route path="/communication" element={<ProtectedLayout><CommunicationPage /></ProtectedLayout>} />
          <Route path="/communication/new" element={<ProtectedLayout><CommunicationForm /></ProtectedLayout>} />

          {/* Milestones */}
          <Route path="/milestone/create" element={<ProtectedLayout><CreateMilestone /></ProtectedLayout>} />
          <Route path="/milestone/:id" element={<ProtectedLayout><MilestoneDetails /></ProtectedLayout>} />
          <Route path="/milestone/:id/upload" element={<ProtectedLayout><UploadMilestone /></ProtectedLayout>} />

          {/* Supervision */}
          <Route path="/supervision/create" element={<ProtectedLayout><CreateSupervision /></ProtectedLayout>} />
          <Route path="/supervision/review/:id" element={<ProtectedLayout><GuardianReview /></ProtectedLayout>} />

          {/* Explorer */}
          <Route path="/explorer" element={<ProtectedLayout><PublicPackageExplorer /></ProtectedLayout>} />
          <Route path="/explorer/create" element={<ProtectedLayout><CreateExplorerListing /></ProtectedLayout>} />
          <Route path="/explorer/:id" element={<ProtectedLayout><ExplorerDetail /></ProtectedLayout>} />

          {/* Admin */}
          <Route path="/admin/access-logs" element={<ProtectedLayout><AccessLogsPage /></ProtectedLayout>} />
          <Route path="/admin/credentials" element={<ProtectedLayout><CredentialsPage /></ProtectedLayout>} />
          <Route path="/admin/system-logs" element={<ProtectedLayout><SystemLogsPage /></ProtectedLayout>} />
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  );
}
