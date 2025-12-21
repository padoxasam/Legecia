import { useState } from "react";
import axios from "../../../utils/axios";

const inputStyle = {
  width: "100%",
  padding: "10px",
  marginBottom: "12px",
  background: "transparent",
  border: "1px solid rgba(0,255,255,0.3)",
  color: "#00ffff",
};

const buttonStyle = {
  background: "transparent",
  border: "1px solid #00ffff",
  color: "#00ffff",
  padding: "10px 20px",
  cursor: "pointer",
};

export default function CreateCommunicationForm() {
  const [form, setForm] = useState({
    b_u: "",
    packg: "",
    us_email: "",
    be_email: "",
    relationship: "",
    dep_mechanism: "",
    com_m1: "",
    com_m2: "",
    additional_comments: "",
  });

  const handleChange = (e) =>
    setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post("/communication/", form);
      alert("Communication channel created");
    } catch (err) {
      alert("Error creating communication channel");
    }
  };

  return (
    <form
      onSubmit={handleSubmit}
      style={{
        marginTop: "25px",
        padding: "20px",
        border: "1px solid rgba(0,255,255,0.2)",
        backdropFilter: "blur(12px)",
      }}
    >
      <h4 style={{ color: "#00ffff" }}>Create New Channel</h4>

      <input name="b_u" placeholder="Beneficiary ID" onChange={handleChange} style={inputStyle} />
      <input name="packg" placeholder="Package ID" onChange={handleChange} style={inputStyle} />

      <input name="us_email" placeholder="Your Email" onChange={handleChange} style={inputStyle} />
      <input name="be_email" placeholder="Beneficiary Email" onChange={handleChange} style={inputStyle} />

      <select name="relationship" onChange={handleChange} style={inputStyle}>
        <option value="">Relationship</option>
        <option value="MOTHER">Mother</option>
        <option value="FATHER">Father</option>
        <option value="BROTHER">Brother</option>
        <option value="SISTER">Sister</option>
        <option value="OTHER">Other</option>
      </select>

      <input name="dep_mechanism" placeholder="Dependency Mechanism" onChange={handleChange} style={inputStyle} />
      <input name="com_m1" placeholder="Primary Communication" onChange={handleChange} style={inputStyle} />
      <input name="com_m2" placeholder="Secondary Communication (optional)" onChange={handleChange} style={inputStyle} />

      <textarea
        name="additional_comments"
        placeholder="Additional Comments"
        onChange={handleChange}
        style={{ ...inputStyle, height: "80px" }}
      />

      <button style={buttonStyle}>Create</button>
    </form>
  );
}
