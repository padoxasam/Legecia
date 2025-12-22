import { Link } from "react-router-dom";

export default function Sidebar() {
  const user = JSON.parse(localStorage.getItem("user"));
  const role = user?.active_role;

  return (
    <aside className="glass-sidebar">
      {/* Common */}
      <Link to="/">Home</Link>

      {/* USER */}
      {role === "USER" && (
        <>
          <Link to="/dashboard">Dashboard</Link>
          <Link to="/packages">My Packages</Link>
          <Link to="/explorer">Explore</Link>
          <Link to="/milestones">Milestones</Link>
          <Link to="/supervision/create">Request Supervision</Link>
        </>
      )}

      {/* GUARDIAN */}
      {role === "GUARDIAN" && (
        <>
          <Link to="/guardian/dashboard">Guardian Dashboard</Link>
          <Link to="/guardian/review">Supervision Requests</Link>
          <Link to="/packages/monitored">Monitored Packages</Link>
        </>
      )}

      {/* BENEFICIARY */}
      {role === "BENEFICIARY" && (
        <>
          <Link to="/beneficiary/dashboard">My Dashboard</Link>
          <Link to="/packages/assigned">My Packages</Link>
        </>
      )}

      {/* SHARED */}
      {role && (
        <>
          <Link to="/communication">Communication</Link>
          <Link to="/notifications">Notifications</Link>
        </>
      )}
    </aside>
  );
}
