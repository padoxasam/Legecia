import api from "./axios"

export async function sendSupervisionRequest(payload){
  return api.post("/api/supervision/requests/",payload)
}

export async function listSupervisionRequests(){
  return api.get("/api/supervision/requests/")
}

export async function respondToRequest(id,action){
  return api.post(`/api/supervision/requests/${id}/${action}/`)
}
