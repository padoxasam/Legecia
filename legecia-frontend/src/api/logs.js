import api from "../utils/api";

// Admin — all system events
export const fetchSystemLogs = () => {
  return api.get("/logs/");
};

// User — own activity
export const fetchMyLogs = () => {
  return api.get("/logs/me/");
};
