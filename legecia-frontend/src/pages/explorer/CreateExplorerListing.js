import { useState } from "react";
import axios from "api/axios"; 

export default function CreateExplorerListing() {
  const [form, setForm] = useState({
    pack: "",
    family_nickname: "",
    remarks: "",
    is_public: true,
    posted_at: new Date().toISOString().slice(0, 10),
  });

  const submit = () => {
    axios.post("/explorer/create/", form)
      .then(() => alert("Package listed publicly"))
      .catch(err => alert("Error creating listing"));
  };

  return (
    <div style={{ padding: "30px" }}>
      <h2 style={{ color: "#00ffff" }}>Create Public Package Listing</h2>

      <input
        placeholder="Package ID"
        onChange={e => setForm({ ...form, pack: e.target.value })}
      />

      <input
        placeholder="Family Nickname"
        onChange={e => setForm({ ...form, family_nickname: e.target.value })}
      />

      <textarea
        placeholder="Remarks"
        onChange={e => setForm({ ...form, remarks: e.target.value })}
      />

      <button
        onClick={submit}
        style={{
          marginTop: "15px",
          padding: "10px",
          background: "#00ffff",
          border: "none",
          cursor: "pointer"
        }}
      >
        Publish
      </button>
    </div>
  );
}
