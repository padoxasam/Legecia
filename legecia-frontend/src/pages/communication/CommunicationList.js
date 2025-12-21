import { useEffect, useState } from "react";
import axios from "../../../utils/axios";

export default function CommunicationList() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    axios.get("/communication/").then((res) => setItems(res.data));
  }, []);

  return (
    <div style={{ marginTop: "30px" }}>
      <h4 style={{ color: "#00ffff" }}>Existing Channels</h4>

      {items.map((item) => (
        <div
          key={item.id}
          style={{
            marginBottom: "12px",
            padding: "15px",
            border: "1px solid rgba(0,255,255,0.15)",
          }}
        >
          <p style={{ color: "#00ffff" }}>
            Beneficiary: {item.be_email}
          </p>
          <p style={{ color: "#94a3b8" }}>
            Package ID: {item.packg}
          </p>
          <p style={{ color: "#94a3b8" }}>
            Relationship: {item.relationship}
          </p>
        </div>
      ))}
    </div>
  );
}
