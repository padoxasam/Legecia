import { Link } from "react-router-dom";

export default function Sidebar() {
  return (
    <aside className="glass-sidebar">
      <Link to="/">Home</Link>
      <Link to="/supervision/create">Request Supervision</Link>
      <Link to="/guardian/review">Guardian Requests</Link>
      <Link to="/notifications">Notifications</Link>
    </aside>
  );
}
