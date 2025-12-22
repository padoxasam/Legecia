// components/PackageCard.js

export default function PackageCard({ pkg, onRequest }) {
  return (
    <div className="neon-card">
      <h3>{pkg.pack_name}</h3>

      <p>{pkg.description || "No description"}</p>

      <div className="meta">
        <span>{pkg.pack_type}</span>
        <span>{pkg.pack_delivery}</span>
      </div>

      {pkg.unlocked && <span className="badge neon">UNLOCKED</span>}

      {pkg.pack_delivery === "Public" && (
        <span className="badge neon">PUBLIC</span>
      )}

      {/* Guardian flow */}
      {pkg.pack_delivery === "Guardian" && (
        <button onClick={() => onRequest(pkg)}>
          Request Guardian
        </button>
      )}
    </div>
  )
}
