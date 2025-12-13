import {useState} from "react"
import api from "../api/axios"

export default function PackageForm({onCreated}){
  const [data,setData]=useState({
    pack_name:"",
    description:"",
    tags:"",
    pack_type:"",
    pack_delivery:"",
    has_expiry:false,
    expiry_at:null
  })

  const submit=async()=>{
    const res=await api.post("/api/package/",data)
    onCreated?.(res.data)
  }

  return (
    <div className="neon-card glass">
      <input onChange={e=>setData({...data,pack_name:e.target.value})}/>
      <button onClick={submit}>Create</button>
    </div>
  )
}
