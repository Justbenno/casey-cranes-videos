import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./styles.css";

type Stage = "Enquiry" | "Assessment" | "Quote Draft" | "Customer Approval" | "Lift Planning" | "Ready for Allocation" | "Completed";
type Job = { jobNumber: string; customer: string; site: string; requestedDate: string; status: Stage; crane: string; description: string };

const stages: Stage[] = ["Enquiry", "Assessment", "Quote Draft", "Customer Approval", "Lift Planning", "Ready for Allocation", "Completed"];
const jobs: Job[] = [
  { jobNumber: "ENQ-24018", customer: "Harbour Point Developments", site: "Fictional Bay, VIC", requestedDate: "2026-08-04", status: "Assessment", crane: "GMK5170", description: "Roof plant installation and tandem lift review" },
  { jobNumber: "ENQ-24017", customer: "Southern Structures", site: "Example Industrial Estate, VIC", requestedDate: "2026-08-06", status: "Quote Draft", crane: "GMK5150", description: "Steel portal frame installation" },
  { jobNumber: "ENQ-24016", customer: "Northbank Civil", site: "Demo Wharf, VIC", requestedDate: "2026-08-11", status: "Lift Planning", crane: "GMK4080", description: "Generator placement with spreader beam" }
];

function App() {
  const [active, setActive] = useState("Dashboard");
  const [selected, setSelected] = useState<Job>(jobs[0]);
  const nav = ["Dashboard", "Jobs", "Estimating", "Lift Planning", "Workflow", "Evidence", "Administration"];
  return (
    <div className="app-shell">
      <aside className="sidebar">
        <div className="brand"><span className="brand-mark">C</span><div><strong>CASEY</strong><small>CRANE HIRE</small></div></div>
        <div className="demo-banner">STAGE 1 · DEMO MODE</div>
        <nav>{nav.map((item) => <button className={active === item ? "nav-item active" : "nav-item"} onClick={() => setActive(item)} key={item}><span>{icons[item]}</span>{item}</button>)}</nav>
        <div className="sidebar-footer"><span className="status-dot" /> Localhost only<br /><small>Fictional operational data</small></div>
      </aside>
      <main className="main-content">
        <header className="topbar"><div><span className="eyebrow">CASEYOPS / {active.toUpperCase()}</span><h1>{active}</h1></div><div className="user-chip"><span className="avatar">EC</span><div><strong>Demo Estimator</strong><small>Estimator role</small></div></div></header>
        {active === "Dashboard" ? <Dashboard onSelect={(job) => { setSelected(job); setActive("Jobs"); }} /> : <Workspace active={active} selected={selected} onSelect={setSelected} />}
      </main>
    </div>
  );
}

function Dashboard({ onSelect }: { onSelect: (job: Job) => void }) {
  return <div className="page"><section className="metrics">{[["12", "Active enquiries", "3 require review"], ["04", "Draft quotations", "Human approval required"], ["03", "Lift plans", "1 awaiting sign-off"], ["07", "Evidence items", "2 added today"]].map(([value, label, note]) => <div className="metric-card" key={label}><span>{label}</span><strong>{value}</strong><small>{note}</small></div>)}</section><div className="grid-two"><section className="panel"><div className="panel-heading"><div><span className="eyebrow">CONTROLLED WORKFLOW</span><h2>Jobs requiring attention</h2></div><button className="button-link">View all →</button></div>{jobs.map((job) => <button className="job-row" key={job.jobNumber} onClick={() => onSelect(job)}><span className="job-icon">↗</span><span className="job-summary"><strong>{job.jobNumber}</strong><span>{job.customer} · {job.site}</span></span><span className="status-pill">{job.status}</span><span className="chevron">›</span></button>)}</section><section className="panel"><div className="panel-heading"><div><span className="eyebrow">AUDIT TRAIL</span><h2>Recent activity</h2></div></div>{["Lift plan LP-0003 submitted for review", "Evidence added to ENQ-24017", "Quote Q-0002 revised to v2", "ENQ-24018 moved to Assessment"].map((item, i) => <div className="activity" key={item}><span className="activity-dot" /><div><strong>{item}</strong><small>{i + 1} hour{ i ? "s" : "" } ago · Demo Estimator</small></div></div>)}</section></div><section className="workflow-strip"><div className="panel-heading"><div><span className="eyebrow">NO STAGE SKIPPING</span><h2>Workflow board</h2></div><span className="read-only">READ ONLY PREVIEW</span></div><div className="stage-track">{stages.map((stage, i) => <div className="stage" key={stage}><span className={i < 3 ? "stage-number done" : "stage-number"}>{i < 3 ? "✓" : i + 1}</span><span>{stage}</span>{i < stages.length - 1 && <i>→</i>}</div>)}</div></section></div>;
}

function Workspace({ active, selected, onSelect }: { active: string; selected: Job; onSelect: (job: Job) => void }) {
  if (active === "Jobs" || active === "Workflow") return <div className="page"><section className="panel"><div className="panel-heading"><div><span className="eyebrow">CONTROLLED REGISTER</span><h2>{active === "Jobs" ? "Job enquiry register" : "Workflow board"}</h2></div><button className="primary-button">+ New enquiry</button></div><div className="table-wrap"><table><thead><tr><th>Job number</th><th>Customer / site</th><th>Requested</th><th>Crane</th><th>Status</th><th>Revision</th></tr></thead><tbody>{jobs.map((job) => <tr onClick={() => onSelect(job)} key={job.jobNumber}><td><strong>{job.jobNumber}</strong></td><td>{job.customer}<small>{job.site}</small></td><td>{job.requestedDate}</td><td>{job.crane}</td><td><span className="status-pill">{job.status}</span></td><td>v1</td></tr>)}</tbody></table></div></section><section className="detail-grid"><Detail label="Selected enquiry" value={selected.jobNumber} /><Detail label="Description" value={selected.description} /><Detail label="Contact" value="Demo contact · (03) 9000 0000" /><Detail label="Audit status" value="Created · modified · approval pending" /></section></div>;
  const titles: Record<string, [string, string]> = { Estimating: ["Draft quotation workspace", "Prepare costs for human review. No quote is final."], "Lift Planning": ["Lift planning workspace", "Capture engineering inputs before approval."], Evidence: ["Shared evidence record", "Every item is versioned and retained. Nothing is deleted."], Administration: ["Administration", "Placeholder roles and permissions for the Stage 1 demonstration."] };
  const [title, subtitle] = titles[active] ?? ["Workspace", "Stage 1 controlled workspace"];
  return <div className="page"><section className="panel form-panel"><div className="panel-heading"><div><span className="eyebrow">HUMAN REVIEW REQUIRED</span><h2>{title}</h2><p>{subtitle}</p></div><span className="draft-badge">DRAFT ONLY</span></div><div className="form-grid">{(active === "Lift Planning" ? ["Load weight", "Dimensions", "Centre of gravity", "Pick radius", "Set radius", "Crane model", "Boom length", "Counterweight", "Outriggers", "Hook block", "Total rigging", "OEM capacity", "Utilisation %", "Safety margin"] : active === "Estimating" ? ["Crane", "Labour", "Transport", "Travel", "Fuel levy", "GST", "Notes"] : ["Record title", "Record type", "Revision", "Approval comments"]).map((label) => <label key={label}>{label}<input placeholder={`Enter ${label.toLowerCase()}`} /></label>)}</div><div className="form-actions"><span>All changes create an audit record.</span><button className="secondary-button">Save revision</button><button className="primary-button">Submit for review</button></div></section></div>;
}
function Detail({ label, value }: { label: string; value: string }) { return <div className="detail-card"><span className="eyebrow">{label}</span><strong>{value}</strong></div>; }
const icons: Record<string, string> = { Dashboard: "▦", Jobs: "▤", Estimating: "$", "Lift Planning": "⌁", Workflow: "⇄", Evidence: "▧", Administration: "⚙" };
import { useState } from "react";
createRoot(document.getElementById("root")!).render(<StrictMode><App /></StrictMode>);
