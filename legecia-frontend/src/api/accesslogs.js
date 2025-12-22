import api from "../utils/api";

// ADMIN ONLY — authentication & security logs
export const fetchAccessLogs = () => {
  return api.get("/access-logs/");
};
