# CRM Lead Checklist

Add a configurable checklist to CRM leads to track progress during the sales process.

---

## Features

- **Configurable checklist items** for CRM leads  
- **Automatic checklist generation** when a lead is created  
- **Checklist tab** in the lead form view  
- **Progress indicator** in both form and Kanban views  

---


## Technical Details

**Extends**

- `crm.lead`

**Models**

- `crm.lead.checklist.item`
- `crm.lead.checklist.line`

**Logic**

- Progress is computed based on completed checklist items

---

## Tested On

**Odoo 18**