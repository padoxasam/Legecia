import { useState, useEffect } from "react";
import axios from "../../api/axios";
import { motion } from "framer-motion";
import GlassCard from "../../components/ui/GlassCard";
import NeonButton from "../../components/ui/NeonButton";

export default function CreateSupervision() {
  const [form, setForm] = useState({
    pack: "",
    bene: "",
    guard: "",
    packat: "LOCKED",
    guadian_control: true,
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
    const expiry = new Date();
    expiry.setDate(expiry.getDate() + Number(form.days));

    await axios.post("/api/supervision/create/", {
      ...form,
      guard_stat: "Pending",
      user_stat: "Active",
      expires_at: expiry.toISOString().split("T")[0]
    });
  };

  return (
    <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }}>
      <GlassCard title="Request Supervision">
        
        <select name="pack" onChange={handleChange}>
          <option>Select Package</option>
        </select>

        <select name="guard" onChange={handleChange}>
          <option>Select Guardian</option>
        </select>

        <select name="bene" onChange={handleChange}>
          <option>Select Beneficiary</option>
        </select>

        <select name="packat" onChange={handleChange}>
          <option value="LOCKED">Locked</option>
          <option value="Timed">Timed</option>
          <option value="Manual">Guardian Manual</option>
        </select>

        <label>
          Guardian Can Control
          <input type="checkbox" name="guadian_control" checked={form.guadian_control} onChange={handleChange} />
        </label>

        <label>
          Guardian Can Reveal Content
          <input type="checkbox" name="guardian_revealing" checked={form.guardian_revealing} onChange={handleChange} />
        </label>

        <input
          type="number"
          min="30"
          max="100"
          name="days"
          value={form.days}
          onChange={handleChange}
        />

        <textarea name="remarks" onChange={handleChange} />

        <NeonButton onClick={handleSubmit}>
          Send Request
        </NeonButton>

      </GlassCard>
    </motion.div>
  );
}
