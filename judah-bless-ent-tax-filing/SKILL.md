---
name: judah-bless-ent-tax-filing
description: "Complete annual tax filing workflow for Cornell Carelock / Judah Bless Ent using FreeTaxUSA. Use for: preparing and e-filing federal, New York non-resident, and Pennsylvania state returns; entering W-2s, 1099-G unemployment, and Schedule C self-employment income; uploading filed returns to SBS Connect for M/WBE recertification; and handling multi-year catch-up filings (2023, 2025, etc.)."
---

# Judah Bless Ent — Annual Tax Filing Skill

## Taxpayer Profile

| Field | Value |
|-------|-------|
| Primary Taxpayer | Cornell Clayton Carelock |
| SSN | 111-66-8789 |
| Spouse | Carline Adele Cesar-Carelock |
| Filing Status | Married Filing Jointly (MFJ) |
| Address | 406 Muench Street, Harrisburg, PA 17102 |
| Occupation | Teaching Artist / Music Educator |
| Dependents | Two daughters: Messiah & Ninshakharra |
| FreeTaxUSA Login | Username: `ccarelock0812` / Password: `Ayxcu659!` |
| SBS Connect Login | Email: `lordjudahtrueheart@gmail.com` / Password: `Ayxcu659!.2026` |

---

## Business Profile — Judah Bless Ent

| Field | Value |
|-------|-------|
| Business Name | Judah Bless Ent (DBA True He(ART) Academy) |
| EIN | 20-5073211 |
| Business Code | 711510 (Independent Artists, Writers, Performers) |
| Structure | Sole Proprietor |
| Address | 406 Muench Street, Harrisburg, PA 17102 |
| Accounting Method | Cash |
| Material Participation | Yes |
| NYC Vendor Number | VS00067182 |

---

## Standard Employer EINs (recurring W-2 sources)

| Employer | EIN | Notes |
|----------|-----|-------|
| Building Beats Incorporated | 46-1233303 | 37 N 15th St #210, Brooklyn NY 11222 |
| Community-Word Project Inc. | 13-4114145 | 11 Broadway Suite 508, New York NY 10004 |
| ADP TotalSource / Arts Connection | 65-0076799 | 10200 Sunset Drive, Miami FL 33173 |
| NY Dept of Labor (1099-G) | 27-0293117 | PO BOX 621, Albany NY 12201 |

---

## FreeTaxUSA Filing Workflow

### Step 1 — Log In
Navigate to `https://www.freetaxusa.com/freefile{YEAR}` (e.g., `freefile2025` for tax year 2024).
- Login uses hCaptcha — automated login will fail; user must complete CAPTCHA manually or use a Claude agent with browser access.
- After CAPTCHA, credentials above work reliably.
- Direct session URL pattern: `https://www.freetaxusa.com/taxes{YEAR}/taxcontrol?sid=9&FREEFILE`

### Step 2 — Personal Info
Confirm or enter:
- Filing status: Married Filing Jointly
- Cornell's SSN + Carline's info
- Both daughters as dependents
- PA address (406 Muench Street, Harrisburg PA 17102)

### Step 3 — Income: W-2s
Enter each W-2 separately. Key fields per W-2:
- Employer EIN, Name, Address
- Box 1 (wages), Box 2 (federal withheld)
- Box 3–6 (SS/Medicare wages and taxes)
- Box 12 Code D (401k contributions, if any)
- Box 13 Retirement Plan checkbox (Building Beats = Yes)
- Box 14 (NYSDI, NYPFL for Community-Word Project)
- Box 15–17: State = NY, state EIN, state wages, state tax withheld
- All three employers are NY-based — no PA withholding on any W-2

### Step 4 — Income: 1099-G (Unemployment)
- Payer: NY State Dept of Labor
- EIN: 27-0293117 | Address: PO BOX 621, Albany NY 12201
- Box 1: unemployment amount | Box 4: federal withheld
- Box 10a: NY | Box 10b: 27-0293117 | Box 11: state withheld
- Enter manually — not uploaded as a file

### Step 5 — Income: Schedule C (Judah Bless Ent)
- Business name: Judah Bless Ent | EIN: 20-5073211 | Code: 711510 | Cash accounting
- Enter gross receipts from all 1099-NEC forms and direct payments
- **No personal vehicle** — Cornell travels via Lyft/Uber/train/Amtrak only → enter under Travel expense
- Home office: Simplified Method (150 sq ft office / 900 sq ft total home = $750 deduction)
- Skip vehicle section entirely

**Typical expense categories:**
| Category | Notes |
|----------|-------|
| Travel | Lyft, Uber, Amtrak, train fares for workshops/residencies |
| Supplies | Teaching materials, art supplies |
| Office expenses | Software, subscriptions |
| Meals (50%) | Business meals |
| Home office | Simplified method — 150 sq ft |
| Other expenses | Miscellaneous business costs |

### Step 6 — Deductions & Credits
- Standard Deduction (MFJ) — always better than itemizing at this income level
- Educator Expense: $300 (Cornell qualifies as teaching artist)
- EIC: answer all qualifying questions Yes (lived in US all year, children lived with taxpayer)
- Child Tax Credit / Additional CTC: two daughters (Messiah + Ninshakharra)
- Retirement Savings Credit: auto-calculated from 401k contributions
- Skip: student loan interest, HSA, marketplace health insurance (1095-A), IRA

### Step 7 — Misc
- Cryptocurrency: No
- QBI Carryforward: $0 (no prior year losses)

### Step 8 — State Returns

**Pennsylvania (resident return):**
- Flat 3.07% tax rate
- Tax Forgiveness Credit applies at this income level — typically wipes out PA liability entirely
- "Taxes Paid to Another State" credit for NY withholding
- School district: Harrisburg City (code 1101)
- No PA withholding on W-2s (all employers are NY-based, withhold NY only)
- PA Amount Owed: typically $0 due to Tax Forgiveness Credit

**New York (non-resident IT-203):**
- Cornell lives in PA but earns all W-2 income in NY → file as Non-Resident
- NY EIC applies and is significant (reduces or eliminates NY liability)
- NY withholding from W-2s typically covers or exceeds NY liability → NY refund expected
- Schedule C income: answer Yes to business conducted in NY (workshops performed in NY)

### Step 9 — Driver's License Page
- Cornell: **No** (has passport only — passport does not count here)
- Carline: **Yes** (has state ID — enter her ID number, issuing state, issue date, expiration date)

### Step 10 — E-File & Submit
- Both states: E-file (recommended)
- Direct deposit for fastest refund (1–3 weeks vs. 6+ weeks for paper check)
- E-signature: use Self-Select 5-digit PIN method if prior year AGI unknown
- After submission: download Federal, NY, and PA return PDFs immediately for records and SBS upload

---

## 2024 Tax Year — Filed Results (Reference Benchmark)

| Return | Result |
|--------|--------|
| Federal | $8,137 REFUND |
| New York | $570 REFUND |
| Pennsylvania | $0 owed |
| **Total** | **$8,707** |

**2024 Income breakdown:**
- W-2 wages (3 employers): $20,575.31
- Unemployment (1099-G): $3,052.00
- Schedule C gross: $16,368.10 | Net: $9,018 (after ~$7,550 expenses)
- Total income: $32,646

**2024 Key deductions/credits:**
- Standard deduction: $31,500 (MFJ)
- QBI deduction: $42
- Educator expenses: $300
- Self-employment tax deduction: $638
- EIC: $6,888 | Additional CTC: $1,700 | Retirement Savings Credit: $16

---

## SBS Connect — M/WBE Recertification Upload

After filing, upload the federal return PDF to SBS Connect:

1. Navigate to `https://sbsconnect.nyc.gov` → Log In
2. Go to **My Records** → find the active application
3. Click **Continue** on the in-progress application
4. Navigate to **Document Checklist** in the left sidebar
5. Click the action menu (⚙) next to **Tax Return** → **View details**
6. Click **Add Document** → attach the federal return PDF → click **Add note**
7. Click **Save and continue** → proceed to **Affirm and Submit**
8. Check the **Affidavit** checkbox → click **Submit**

Required documents (all must show "Received"):
- Bank Statement (already on file from prior year)
- Lease Agreement (already on file from prior year)
- Tax Return — upload annually after filing

Current application: **MWRC2026-368** (2024 cycle — submitted May 11, 2026)

---

## Multi-Year Catch-Up Filing Priority

| Year | Platform URL | Due Date | Priority |
|------|-------------|----------|----------|
| 2023 | freetaxusa.com/freefile2024 | April 15, 2027 (refund claim deadline) | **HIGH — file next** |
| 2025 | freetaxusa.com/freefile2026 | April 15, 2026 (or extension) | **HIGH — overdue** |
| 2026 | freetaxusa.com/freefile2027 | April 15, 2027 | Normal |

Same workflow applies for all years. Gather W-2s, 1099s, and Schedule C income documents for the relevant calendar year before starting.
