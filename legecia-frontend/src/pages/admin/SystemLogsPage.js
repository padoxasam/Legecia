import React, { useEffect, useState, useContext } from "react";
import { fetchSystemLogs, fetchMyLogs } from "api/logs";
import NotificationCard from "components/NotificationCard";
import { AuthContext } from "context/AuthContext";

const SystemLogsPage = () => {
  const { user } = useContext(AuthContext);
  const [logs, setLogs] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const loader = user?.is_admin ? fetchSystemLogs : fetchMyLogs;

    loader()
      .then(res => setLogs(res.data))
      .finally(() => setLoading(false));
  }, [user]);

  if (loading) {
    return <p>Loading activity logs...</p>;
  }

  return (
    <div>
      <h2>
        {user?.is_admin ? "System Activity Logs" : "My Activity"}
      </h2>

      {logs.length === 0 && <p>No logs available.</p>}

      {logs.map(log => (
        <NotificationCard
          key={log.log_id}
          title={log.log_action.replaceAll("_", " ")}
          subtitle={`Visitor ID: ${log.visitor_id}`}
          content={log.additional_comments}
          footer={new Date(log.log_at).toLocaleString()}
          status={log.log_stat}
        />
      ))}
    </div>
  );
};

export default SystemLogsPage;
