// src/pages/NotificationsPage.js
import { useEffect, useState } from "react";
import api from "utils/api";
import CyberLayout from "components/layouts/CyberLayout";
import NotificationCard from "components/NotificationCard";

function NotificationsPage() {
  const [notifications, setNotifications] = useState([]);

  useEffect(() => {
    api.get("notifications/list")
      .then((res) => setNotifications(res.data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <CyberLayout>
      <h1 style={{ color: "#00eaff" }}>🔔 Notifications Center</h1>

      <div
        style={{
          marginTop: "25px",
          display: "flex",
          flexDirection: "column",
          gap: "15px",
        }}
      >
        {notifications.map((n) => (
          <NotificationCard key={n.id} data={n} />
        ))}
      </div>
    </CyberLayout>
  );
}

export default NotificationsPage;
