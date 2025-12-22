import { useEffect, useState } from "react";
import axios from "api/axios"; 
import TopBar from "components/layouts/TopBar";


export default function CredentialsPage() {
  const [credentials, setCredentials] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    fetchCredentials();
  }, []);

  const fetchCredentials = async () => {
    try {
      const res = await axios.get("/api/admin/credentials/");
      setCredentials(res.data);
    } catch (err) {
      setError("Failed to load credentials");
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <TopBar />

      <div style={containerStyle}>
        <h2 style={titleStyle}>Credentials Audit</h2>

        {loading && <p>Loading...</p>}
        {error && <p style={{ color: "red" }}>{error}</p>}

        {!loading && !error && (
          <div style={tableWrapper}>
            <table style={tableStyle}>
              <thead>
                <tr>
                  <th>Username</th>
                  <th>Recovery Email</th>
                  <th>2FA</th>
                  <th>Failed Attempts</th>
                  <th>Last Seen</th>
                  <th>Created</th>
                </tr>
              </thead>

              <tbody>
                {credentials.map((cred) => (
                  <tr key={cred.credential_id}>
                    <td>{cred.username}</td>
                    <td>{cred.recover_email}</td>
                    <td>
                      <span
                        style={{
                          color: cred.two_factor ? "#00ffae" : "#ffb86b",
                          fontWeight: 600,
                        }}
                      >
                        {cred.two_factor ? "ENABLED" : "DISABLED"}
                      </span>
                    </td>
                    <td>{cred.failed_entry}</td>
                    <td>{cred.last_seen ? formatDate(cred.last_seen) : "—"}</td>
                    <td>{formatDate(cred.created_at)}</td>
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
  color: "#00ffff",
  letterSpacing: "1px",
};

const tableWrapper = {
  overflowX: "auto",
  border: "1px solid rgba(0,255,255,0.2)",
  borderRadius: "10px",
  backdropFilter: "blur(12px)",
};
const tableStyle = {
  width: "100%",
  borderCollapse: "collapse",
};
