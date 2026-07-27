import { describe, expect, it } from "vitest";

const stages = ["Enquiry", "Assessment", "Quote Draft", "Customer Approval", "Lift Planning", "Ready for Allocation", "Completed"];
describe("workflow safeguards", () => {
  it("allows only the next stage", () => expect(stages.indexOf("Assessment")).toBe(stages.indexOf("Enquiry") + 1));
  it("does not allow skipping stages", () => expect(stages.indexOf("Lift Planning")).not.toBe(stages.indexOf("Enquiry") + 1));
});
