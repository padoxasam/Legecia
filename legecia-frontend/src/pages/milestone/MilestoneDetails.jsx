import React, { useEffect, useState } from "react";
import { fetchMilestone } from "api/milestone";
import { useParams } from "react-router-dom";

const MilestoneDetail = () => {
  const { milestoneId } = useParams();
  const [milestone, setMilestone] = useState(null);

  useEffect(() => {
    fetchMilestone(milestoneId).then(res => setMilestone(res.data));
  }, [milestoneId]);

  if (!milestone) return <p>Loading...</p>;

  return (
    <div>
      <h2>{milestone.milestone_name}</h2>
      <p>Family: {milestone.family_name}</p>
      <p>Uploaded: {new Date(milestone.upload_date).toLocaleString()}</p>
      <p>Status: {milestone.verified_documents ? "Verified" : "Pending"}</p>
    </div>
  );
};

export default MilestoneDetail;
