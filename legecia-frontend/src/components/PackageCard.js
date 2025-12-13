export default function PackageCard({pkg,onRequest}){
  return(
    <div className="neon-card">
      <h3>{pkg.pack_name}</h3>
      <p>{pkg.description}</p>
      {pkg.is_public && <span className="badge neon">PUBLIC</span>}
      <button onClick={()=>onRequest(pkg)}>Request Guardian</button>
    </div>
  )
}
