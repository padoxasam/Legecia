import React, { useState } from "react";
import { createMilestone } from "api/milestone";

const CreateMilestone = () => {
  const [form, setForm] = useState({});
  const [file, setFile] = useState(null);

  const submit = async () => {
    const data = new FormData();
    Object.entries(form).forEach(([k, v]) => data.append(k, v));
    data.append("user_reference_file", file);

    await createMilestone(data);
    alert("Milestone created");
  };

  return (
    <div>
      <h2>Create Milestone</h2>

      <input placeholder="Milestone Name"
        onChange={e => setForm({ ...form, milestone_name: e.target.value })} />

      <input placeholder="Family Name"
        onChange={e => setForm({ ...form, family_name: e.target.value })} />

      <textarea placeholder="Remarks"
        onChange={e => setForm({ ...form, remarks: e.target.value })} />

      <input type="file" onChange={e => setFile(e.target.files[0])} />

      <button onClick={submit}>Create</button>
    </div>
  );
};

export default CreateMilestone;
