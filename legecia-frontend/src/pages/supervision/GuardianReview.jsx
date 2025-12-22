// pages/supervision/GuardianReview.jsx

import { useEffect, useState } from "react";
import axios from "api/axios"; 
import GlassCard from "components/GlassCard";
import NeonButton from "components/NeonButton";

export default function GuardianReview() {
  const [requests, setRequests] = useState([]);

  useEffect(() => {
    axios
      .get("/api/supervision/guardian/pending/")
      .then(res => setRequests(res.data));
  }, []);

  const updateRequest = async (id, payload) => {
    await axios.put(`/api/supervision/${id}/`, payload);
    setRequests(reqs => reqs.filter(r => r.id !== id));
  };

  return (
    <>
      {requests.map(req => (
        <GlassCard key={req.id} title={req.pack_name}>

          <p>User ID: {req.user}</p>
          <p>Beneficiary ID: {req.bene}</p>
          <p>Mode: {req.packat}</p>

          <label>
            Reveal Content
            <input
              type="checkbox"
              checked={req.guardian_revealing}
              onChange={e =>
                setRequests(prev =>
                  prev.map(r =>
                    r.id === req.id
                      ? { ...r, guardian_revealing: e.target.checked }
                      : r
                  )
                )
              }
            />
          </label>

          <NeonButton
            onClick={() =>
              updateRequest(req.id, {
                supervision_status: "Approved",
                guard_stat: "Active",
                guardian_revealing: req.guardian_revealing
              })
            }
          >
            Approve
          </NeonButton>

          <NeonButton
            danger
            onClick={() =>
              updateRequest(req.id, {
                supervision_status: "Rejected",
                remarks: "Rejected by guardian"
              })
            }
          >
            Reject
          </NeonButton>

        </GlassCard>
      ))}
    </>
  );
}
