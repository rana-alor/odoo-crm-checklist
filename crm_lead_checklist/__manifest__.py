{
    "name": "CRM Lead Checklist",
    "version": "18.0.1.0.0",
    "summary": "Checklist for CRM leads",
    'license': 'LGPL-3',
    "depends": ["crm"],
    "data": [
        "security/ir.model.access.csv",
        "views/checklist_item_views.xml",
        "views/crm_lead_views.xml",
    ],
    "installable": True,
    "application": False,
}
