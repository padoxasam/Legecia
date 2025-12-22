import api from "../utils/api";

export const createMilestone = (formData) => {
  return api.post("/milestone/create/", formData, {
    headers: { "Content-Type": "multipart/form-data" },
  });
};

export const uploadBeneficiaryMilestone = (milestoneId, formData) => {
  return api.post(`/milestone/upload/${milestoneId}/`, formData, {
    headers: { "Content-Type": "multipart/form-data" },
  });
};

export const fetchMilestone = (milestoneId) => {
  return api.get(`/milestone/${milestoneId}/`);
};
