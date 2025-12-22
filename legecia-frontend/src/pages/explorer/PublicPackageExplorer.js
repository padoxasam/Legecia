import { useEffect, useState } from "react";
import axios from "api/axios"; 

export default function PublicPackageExplorer() {
  const [packages, setPackages] = useState([]);

  useEffect(() => {
    axios.get("/explorer/")
      .then(res => setPackages(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div style={{ padding: "30px" }}>
      <h2 style={{ color: "#00ffff" }}>Public Package Explorer</h2>

      <div style={{ display: "grid", gap: "20px", marginTop: "20px" }}>
        {packages.map(pkg => (
          <div
            key={pkg.id}
            style={{
              padding: "20px",
              border: "1px solid rgba(0,255,255,0.3)",
              borderRadius: "10px",
              backdropFilter: "blur(10px)"
            }}
          >
            <h4 style={{ color: "#00ffff" }}>{pkg.family_nickname}</h4>
            <p><strong>Posted:</strong> {pkg.posted_at}</p>
            <p>{pkg.remarks || "No remarks"}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
