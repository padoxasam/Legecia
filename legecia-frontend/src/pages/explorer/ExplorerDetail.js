import { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import axios from "api/axios"; 

export default function ExplorerDetail() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [pkg, setPkg] = useState(null);

  useEffect(() => {
    axios.get(`/explorer/${id}/`)
      .then(res => setPkg(res.data))
      .catch(() => navigate("/explorer"));
  }, [id, navigate]);

  const remove = () => {
    axios.delete(`/explorer/${id}/`)
      .then(() => navigate("/explorer"));
  };

  if (!pkg) return null;

  return (
    <div style={{ padding: "30px" }}>
      <h2 style={{ color: "#00ffff" }}>{pkg.family_nickname}</h2>

      <p>{pkg.remarks}</p>

      <button
        onClick={remove}
        style={{
          marginTop: "20px",
          background: "red",
          color: "white",
          padding: "10px",
          border: "none"
        }}
      >
        Remove Listing
      </button>
    </div>
  );
}
