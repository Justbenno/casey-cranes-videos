import cors from "cors";
import express from "express";
import { z } from "zod";

const app = express();
app.use(cors({ origin: "http://localhost:5173" }));
app.use(express.json());

const workflowStages = ["Enquiry", "Assessment", "Quote Draft", "Customer Approval", "Lift Planning", "Ready for Allocation", "Completed"] as const;
const enquirySchema = z.object({
  customer: z.string().min(1), site: z.string().min(1), contact: z.string().min(1),
  phone: z.string().min(1), email: z.string().email(), description: z.string().min(1),
  requestedDate: z.string().date()
});

app.get("/api/health", (_request, response) => response.json({ status: "ok", mode: "demo", production: false }));
app.get("/api/workflow/stages", (_request, response) => response.json({ stages: workflowStages }));
app.post("/api/jobs", (request, response) => {
  const result = enquirySchema.safeParse(request.body);
  if (!result.success) return response.status(400).json({ error: "Invalid enquiry", details: result.error.flatten() });
  return response.status(201).json({ id: crypto.randomUUID(), ...result.data, status: "Enquiry", revision: 1, audit: { createdBy: "demo-user", createdDate: new Date().toISOString() } });
});
app.post("/api/jobs/:id/transition", (request, response) => {
  const schema = z.object({ from: z.enum(workflowStages), to: z.enum(workflowStages), approvalComments: z.string().min(1) });
  const result = schema.safeParse(request.body);
  if (!result.success) return response.status(400).json({ error: "A human approval comment is required", details: result.error.flatten() });
  const fromIndex = workflowStages.indexOf(result.data.from);
  if (workflowStages.indexOf(result.data.to) !== fromIndex + 1) return response.status(409).json({ error: "Workflow stages cannot be skipped" });
  return response.json({ id: request.params.id, ...result.data, recordedAt: new Date().toISOString(), immutable: true });
});

app.listen(Number(process.env.PORT ?? 4000), () => console.log("CaseyOps API listening on http://localhost:4000"));
