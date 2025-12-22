import React, { useState } from "react";
import { uploadBeneficiaryMilestone } from "api/milestone";
import { useParams } from "react-router-dom";

const UploadMilestone = () => {
  const { milestoneId } = useParams();
  const [file, setFile] = useState(null);

  const submit = async () => {
    const data = new FormData();
    data.append("beneficiary_file", file);

    await uploadBeneficiaryMilestone(milestoneId, data);
    alert("Milestone uploaded");
  };

  return (
    <div>
      <h2>Upload Milestone File</h2>
      <input type="file" onChange={e => setFile(e.target.files[0])} />
      <button onClick={submit}>Upload</button>
    </div>
  );
};

export default UploadMilestone;
