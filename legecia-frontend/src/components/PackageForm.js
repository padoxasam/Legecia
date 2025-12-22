// components/PackageForm.js

import { useState } from "react"
import api from "../api/axios"

export default function PackageForm({ onCreated }) {
  const [data, setData] = useState({
    pack_name: "",
    description: "",
    tags: "",
    pack_type: "Event-Based",
    pack_delivery: "Guardian",
    pack_status: "Active",
    ownership: "PRIVATE",
    has_expiry: false,
    expiry_at: null
  })

  const submit = async () => {
    try {
      const res = await api.post("/api/package/", data)
      onCreated?.(res.data)
    } catch (err) {
      alert("Failed to create package")
    }
  }

  return (
    <div className="neon-card glass">

      <h3>Create Package</h3>

      <input
        placeholder="Package Name"
        onChange={e => setData({ ...data, pack_name: e.target.value })}
      />

      <textarea
        placeholder="Description"
        onChange={e => setData({ ...data, description: e.target.value })}
      />

      <select
        onChange={e => setData({ ...data, pack_type: e.target.value })}
      >
        <option>Event-Based</option>
        <option>Location-Based</option>
        <option>Countdown</option>
      </select>

      <select
        onChange={e => setData({ ...data, pack_delivery: e.target.value })}
      >
        <option>Guardian</option>
        <option>Direct</option>
        <option>Public</option>
      </select>

      <button onClick={submit}>Create Package</button>
    </div>
  )
}
