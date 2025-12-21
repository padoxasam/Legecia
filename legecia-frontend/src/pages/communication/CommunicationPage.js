import TopBar from "../../../components/layout/TopBar";
import CreateCommunicationForm from "./CreateCommunicationForm";
import CommunicationList from "./CommunicationList";

export default function CommunicationPage() {
  return (
    <div style={{ minHeight: "100vh", background: "#020617" }}>
      <TopBar />

      <div style={{ padding: "30px" }}>
        <h2 style={{ color: "#00ffff", letterSpacing: "2px" }}>
          Communication Channels
        </h2>

        <CreateCommunicationForm />
        <CommunicationList />
      </div>
    </div>
  );
}
