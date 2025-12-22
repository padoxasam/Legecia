import { useEffect, useState } from "react";
import axios from "api/axios"; 
import TopBar from "components/layouts/TopBar";

export default function AccessLogsPage() {
  const [logs, setLogs] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    fetchLogs();
  }, []);

  const fetchLogs = async () => {
    try {
      const res = await axios.get("/api/access-logs/");
      setLogs(res.data);
    } catch (err) {
      setError("Failed to load access logs");
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <TopBar />

      <div style={containerStyle}>
        <h2 style={titleStyle}>Access Logs Audit</h2>

        {loading && <p>Loading logs...</p>}
        {error && <p style={{ color: "red" }}>{error}</p>}

        {!loading && !error && (
          <div style={tableWrapper}>
            <table style={tableStyle}>
              <thead>
                <tr>
                  <th>ID</th>
                  <th>IP Address</th>
                  <th>Device</th>
                  <th>Login Time</th>
                  <th>Logout Time</th>
                  <th>Status</th>
                </tr>
              </thead>

              <tbody>
                {logs.map((log) => (
                  <tr key={log.access_id}>
                    <td>{log.access_id}</td>
                    <td>{log.ip_address}</td>
                    <td>{log.device_info || "—"}</td>
                    <td>{formatDate(log.login_start)}</td>
                    <td>{log.logout ? formatDate(log.logout) : "—"}</td>
                    <td>
                      <span
                        style={{
                          color: log.successful_log ? "#00ffae" : "#ff4d4d",
                          fontWeight: 600,
                        }}
                      >
                        {log.successful_log ? "SUCCESS" : "FAILED"}
                      </span>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </>
);}
function formatDate(value) {
  return new Date(value).toLocaleString();
}
const containerStyle = {
  padding: "30px",
  color: "#eaffff",
};

const titleStyle = {
  marginBottom: "20px",
  letterSpacing: "1px",
  color: "#00ffff",
};

const tableWrapper = {
  overflowX: "auto",
  backdropFilter: "blur(12px)",
  border: "1px solid rgba(0,255,255,0.2)",
  borderRadius: "10px",
};

const tableStyle = {
  width: "100%",
  borderCollapse: "collapse",
};

