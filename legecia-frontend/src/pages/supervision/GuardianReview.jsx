import { useEffect, useState } from "react";
import axios from "../../api/axios";
import GlassCard from "../../components/ui/GlassCard";
import NeonButton from "../../components/ui/NeonButton";

export default function GuardianReview() {
  const [requests, setRequests] = useState([]);

  useEffect(() => {
    axios.get("/api/supervision/guardian/pending/")
      .then(res => setRequests(res.data));
  }, []);

  const updateRequest = async (id, payload) => {
    await axios.put(`/api/supervision/${id}/`, payload);
    setRequests(reqs => reqs.filter(r => r.id !== id));
  };

  return (
    <div>
      {requests.map(req => (
        <GlassCard key={req.id} title={`Package #${req.pack}`}>
          <p>User: {req.user}</p>
          <p>Beneficiary: {req.bene}</p>
          <p>Type: {req.packat}</p>

          <label>
            Allow Control
            <input
              type="checkbox"
              defaultChecked={req.guadian_control}
              onChange={e =>
                req.guadian_control = e.target.checked
              }
            />
          </label>

          <label>
            Reveal Content
            <input
              type="checkbox"
              defaultChecked={req.guardian_revealing}
              onChange={e =>
                req.guardian_revealing = e.target.checked
              }
            />
          </label>

          <NeonButton
            onClick={() =>
              updateRequest(req.id, {
                guard_stat: "Active",
                guardian_revealing: req.guardian_revealing
              })
            }>
            Approve
          </NeonButton>

          <NeonButton
            danger
            onClick={() =>
              updateRequest(req.id, {
                guard_stat: "Rejected",
                remarks: "Rejected by guardian"
              })
            }>
            Reject
          </NeonButton>
        </GlassCard>
      ))}
    </div>
  );
}
