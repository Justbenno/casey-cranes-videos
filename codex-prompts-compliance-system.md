# Casey Crane Compliance System Codex Prompts

Copy/paste the prompts below into Codex (or any compatible agent) to generate the Airtable base + automations and the Power Automate flow for Casey Crane Hire’s compliance system.

---

## A — Build the Airtable Base + All Automations

```
You are an assistant generating a complete Airtable base and automation setup for Casey Crane Hire’s compliance system. Build everything exactly as specified.

====================================================================
BASE NAME: CASEY CRANE COMPLIANCE
====================================================================

Create 4 tables with the exact fields, formulas, and views below.

====================================================================
TABLE 1 — Employees
====================================================================

Fields:
- Employee Name (single line text)
- Email (email)
- Licence Type (single select)
- Licence Expiry Date (date)
- VOC Expiry (date)
- Medical Expiry (date)
- ReminderNeeded (formula):
  OR(
    DATETIME_DIFF({Licence Expiry Date}, TODAY(), 'days') = 30,
    DATETIME_DIFF({Licence Expiry Date}, TODAY(), 'days') = 7,
    DATETIME_DIFF({Licence Expiry Date}, TODAY(), 'days') = 0,
    DATETIME_DIFF({Licence Expiry Date}, TODAY(), 'days') < 0
  )
- Record URL (formula): RECORD_URL()
- Calendar Event Created (checkbox)

View:
- Licence Reminders Needed → Filter: ReminderNeeded = 1

====================================================================
TABLE 2 — Cranes
====================================================================

Fields:
- Crane ID (text)
- Last Service Date (date)
- Service Interval (days) (number)
- Next Service Due (formula):
  DATEADD({Last Service Date}, {Service Interval (days)}, 'days')
- MaintenanceReminderNeeded (formula):
  OR(
    DATETIME_DIFF({Next Service Due}, TODAY(), 'days') = 14,
    DATETIME_DIFF({Next Service Due}, TODAY(), 'days') = 3,
    DATETIME_DIFF({Next Service Due}, TODAY(), 'days') = 0,
    DATETIME_DIFF({Next Service Due}, TODAY(), 'days') < 0
  )
- Maintenance Manager Email (email)
- Record URL (formula): RECORD_URL()
- Calendar Event Created (checkbox)

View:
- Maintenance Reminders Needed → Filter: MaintenanceReminderNeeded = 1

====================================================================
TABLE 3 — Jobs
====================================================================

Fields:
- Job Number (text)
- Client (text)
- Job Date (date)
- Required Documents (multiple select)
- Uploaded Documents (multiple select)
- Missing Documents (formula):
  ARRAYJOIN(
    ARRAYDIFF({Required Documents}, {Uploaded Documents}),
    ", "
  )
- JobReminderNeeded (formula):
  AND(
    {Missing Documents} != "",
    DATETIME_DIFF({Job Date}, TODAY(), 'days') <= 3
  )
- Supervisor Email (email)
- Record URL (formula): RECORD_URL()
- Calendar Event Created (checkbox)

View:
- Job Reminders Needed → Filter: JobReminderNeeded = 1

====================================================================
TABLE 4 — General Compliance
====================================================================

Fields:
- Item Name (text)
- Responsible Email (email)
- VOC Expiry (date)
- Insurance Expiry (date)
- Registration Expiry (date)
- UpdateRequired (formula):
  OR(
    DATETIME_DIFF({VOC Expiry}, TODAY(), 'days') < 0,
    DATETIME_DIFF({Insurance Expiry}, TODAY(), 'days') < 0,
    DATETIME_DIFF({Registration Expiry}, TODAY(), 'days') < 0
  )
- Record URL (formula): RECORD_URL()

View:
- Update Required → Filter: UpdateRequired = 1

====================================================================
CREATE 4 AIRTABLE AUTOMATIONS
====================================================================

Automation A — Licence Reminder
Trigger: When record enters view → Licence Reminders Needed
Action: Send email
To: {Email}
Subject: Licence Expiry Reminder – {Licence Type}
Body:
Hi {Employee Name},
Your {Licence Type} expires on {Licence Expiry Date}.
Record: {Record URL}

Automation B — Maintenance Reminder
Trigger: When record enters view → Maintenance Reminders Needed
Action: Send email
To: {Maintenance Manager Email}
Subject: Maintenance Due – Crane {Crane ID}
Body:
Crane {Crane ID} is due for maintenance on {Next Service Due}.
Record: {Record URL}

Automation C — Job Document Reminder
Trigger: When record enters view → Job Reminders Needed
Action: Send email
To: {Supervisor Email}
Subject: Missing Compliance Documents – Job {Job Number}
Body:
Missing documents: {Missing Documents}
Record: {Record URL}

Automation D — General Compliance Reminder
Trigger: When record enters view → Update Required
Action: Send email
To: {Responsible Email}
Subject: Compliance Update Required – {Item Name}
Body:
{Item Name} requires updating.
Record: {Record URL}

====================================================================
END OF SPECIFICATION — BUILD THE BASE AND AUTOMATIONS EXACTLY
====================================================================
```

---

## B — Build the Power Automate Flow

```
You are an assistant generating a complete Power Automate flow for Casey Crane Hire’s compliance system. Build the entire flow exactly as specified below.

====================================================================
FLOW NAME: Casey Crane – Compliance Calendar Sync
====================================================================

GOAL:
Create a single daily Power Automate flow that:
1. Runs every day at 06:00 Australia/Melbourne.
2. Pulls records from Airtable views:
   - Employees → Licence Reminders Needed
   - Cranes → Maintenance Reminders Needed
   - Jobs → Job Reminders Needed
3. For each record where {Calendar Event Created} is not checked:
   - Create an Outlook calendar event.
   - PATCH Airtable to set {Calendar Event Created} = true.

====================================================================
PART 1 — INITIAL SETUP
====================================================================

Trigger:
- Recurrence
- Every 1 day
- Time: 06:00
- Time zone: AUS Eastern Standard Time

Variables:
1. varAirtableBaseId (string) = "YOUR_BASE_ID"
2. varAirtableApiKey (string) = "YOUR_API_KEY"
3. varAirtableBaseUrl (string) = concat('https://api.airtable.com/v0/', variables('varAirtableBaseId'))

====================================================================
PART 2 — AIRTABLE GET REQUESTS
====================================================================

HTTP GET — Employees:
Method: GET
URI:
concat(
  variables('varAirtableBaseUrl'),
  '/Employees',
  '?view=Licence%20Reminders%20Needed',
  '&filterByFormula=NOT({Calendar%20Event%20Created})'
)
Headers:
Authorization: concat('Bearer ', variables('varAirtableApiKey'))
Content-Type: application/json

HTTP GET — Cranes:
Method: GET
URI:
concat(
  variables('varAirtableBaseUrl'),
  '/Cranes',
  '?view=Maintenance%20Reminders%20Needed',
  '&filterByFormula=NOT({Calendar%20Event%20Created})'
)

HTTP GET — Jobs:
Method: GET
URI:
concat(
  variables('varAirtableBaseUrl'),
  '/Jobs',
  '?view=Job%20Reminders%20Needed',
  '&filterByFormula=NOT({Calendar%20Event%20Created})'
)

====================================================================
PART 3 — PARSE JSON
====================================================================

Parse JSON — Employees:
Content: body('HTTP_-_Get_Employees')
Schema: [include full schema here]

Parse JSON — Cranes:
Content: body('HTTP_-_Get_Cranes')
Schema: [include full schema here]

Parse JSON — Jobs:
Content: body('HTTP_-_Get_Jobs')
Schema: [include full schema here]

====================================================================
PART 4 — APPLY TO EACH LOOPS
====================================================================

Employees loop:
Apply to each: body('Parse_JSON_-_Employees')?['records']

Cranes loop:
Apply to each: body('Parse_JSON_-_Cranes')?['records']

Jobs loop:
Apply to each: body('Parse_JSON_-_Jobs')?['records']

====================================================================
PART 5 — OUTLOOK EVENT CREATION
====================================================================

Employees:
Subject:
concat(
  items('Apply_to_each_-_Employees')?['fields']?['Licence Type'],
  ' Expiry – ',
  items('Apply_to_each_-_Employees')?['fields']?['Employee Name']
)
Start date:
items('Apply_to_each_-_Employees')?['fields']?['Licence Expiry Date']
Body:
concat(
  'Record: ',
  items('Apply_to_each_-_Employees')?['fields']?['Record URL']
)

Cranes:
Subject:
concat(
  'Maintenance Due – Crane ',
  items('Apply_to_each_-_Cranes')?['fields']?['Crane ID']
)
Start date:
items('Apply_to_each_-_Cranes')?['fields']?['Next Service Due']

Jobs:
Subject:
concat(
  'Job ',
  items('Apply_to_each_-_Jobs')?['fields']?['Job Number'],
  ' – ',
  items('Apply_to_each_-_Jobs')?['fields']?['Client']
)
Start date:
items('Apply_to_each_-_Jobs')?['fields']?['Job Date']

====================================================================
PART 6 — AIRTABLE PATCH REQUESTS
====================================================================

PATCH Employees:
Method: PATCH
URI:
concat(
  variables('varAirtableBaseUrl'),
  '/Employees/',
  items('Apply_to_each_-_Employees')?['id']
)
Body:
{
  "fields": {
    "Calendar Event Created": true
  }
}

PATCH Cranes:
Method: PATCH
URI:
concat(
  variables('varAirtableBaseUrl'),
  '/Cranes/',
  items('Apply_to_each_-_Cranes')?['id']
)
Body: same as above

PATCH Jobs:
Method: PATCH
URI:
concat(
  variables('varAirtableBaseUrl'),
  '/Jobs/',
  items('Apply_to_each_-_Jobs')?['id']
)
Body: same as above

====================================================================
END OF SPECIFICATION — BUILD THE FLOW EXACTLY AS ABOVE
====================================================================
```
