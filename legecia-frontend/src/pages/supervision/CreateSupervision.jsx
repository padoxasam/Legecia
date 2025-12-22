// pages/supervision/CreateSupervision.jsx

import { useState } from "react";
import axios from "api/axios"; 
import { motion } from "framer-motion";
import GlassCard from "components/GlassCard";
import NeonButton from "components/NeonButton";

export default function CreateSupervision() {
  const [form, setForm] = useState({
    pack: "",
    bene: "",
    guard: "",
    packat: "LOCKED",
    guardian_revealing: false,
    days: 30,
    remarks: ""
  });

  const handleChange = e => {
    const { name, value, type, checked } = e.target;
    setForm(prev => ({
      ...prev,
      [name]: type === "checkbox" ? checked : value
    }));
  };

  const handleSubmit = async () => {
    // 🔐 calculate supervision_end
    const end = new Date();
    end.setDate(end.getDate() + Number(form.days));

    // 1️⃣ Create Draft
    const res = await axios.post("/api/supervision/create/", {
      pack: form.pack,
      bene: form.bene,
      guard: form.guard,
      packat: form.packat,
      guardian_revealing: form.guardian_revealing,
      supervision_end: end.toISOString(),
      remarks: form.remarks
    });

    const supervisionId = res.data.data.id;

    // 2️⃣ Send to guardian
    await axios.post(`/api/supervision/send/${supervisionId}/`);
  };

  return (
    <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }}>
      <GlassCard title="Request Supervision">

        {/* TODO: populate dynamically */}
        <select name="pack" onChange={handleChange}>
          <option value="">Select Package</option>
        </select>

        <select name="guard" onChange={handleChange}>
          <option value="">Select Guardian</option>
        </select>

        <select name="bene" onChange={handleChange}>
          <option value="">Select Beneficiary</option>
        </select>

        <select name="packat" onChange={handleChange}>
          <option value="LOCKED">Locked</option>
          <option value="Timed">Timed</option>
          <option value="Manual">Guardian Manual</option>
        </select>

        <label>
          Guardian Can Reveal
          <input
            type="checkbox"
            name="guardian_revealing"
            checked={form.guardian_revealing}
            onChange={handleChange}
          />
        </label>

        <input
          type="number"
          min="1"
          name="days"
          value={form.days}
          onChange={handleChange}
        />

        <textarea
          name="remarks"
          placeholder="Remarks"
          onChange={handleChange}
        />

        <NeonButton onClick={handleSubmit}>
          Send Request
        </NeonButton>

      </GlassCard>
    </motion.div>
  );
}
