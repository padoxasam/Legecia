// pages/packages/PackagesPage.js

import { useEffect, useState } from "react"
import api from "api/axios"
import PackageCard from "components/PackageCard"
import PackageForm from "components/PackageForm"
import CyberLayout from "components/layouts/CyberLayout"

// User Packages Page
export default function PackagesPage() {
  const [packages, setPackages] = useState([])
  const [loading, setLoading] = useState(true)

  // Load packages when page mounts
  useEffect(() => {
    loadPackages()
  }, [])

  // Fetch packages from backend
  const loadPackages = async () => {
    try {
      const res = await api.get("/api/package/")
      setPackages(res.data)
    } catch (err) {
      console.error("Failed to load packages", err)
    } finally {
      setLoading(false)
    }
  }

  // Called after package creation
  const handleCreated = (newPkg) => {
    setPackages(prev => [newPkg, ...prev])
  }

  // Request guardian (future logic)
  const handleRequestGuardian = (pkg) => {
    console.log("Request guardian for:", pkg)
    // TODO: integrate supervision request API
  }

  return (
    <CyberLayout title="My Packages">

      {/* CREATE PACKAGE FORM */}
      <PackageForm onCreated={handleCreated} />

      <div className="grid grid-3 mt-4">
        {loading && <p>Loading packages...</p>}

        {!loading && packages.length === 0 && (
          <p>No packages found.</p>
        )}

        {!loading && packages.map(pkg => (
          <PackageCard
            key={pkg.pack_id}
            pkg={pkg}
            onRequest={handleRequestGuardian}
          />
        ))}
      </div>

    </CyberLayout>
  )
}
