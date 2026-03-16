from odoo import fields, models

class CrmLeadChecklistItem(models.Model):
    _name = "crm.lead.checklist.item"
    _description = "CRM Lead Checklist Item"
    _order = "sequence, id"

    name = fields.Char(required=True)
    sequence = fields.Integer(default=10)
    active = fields.Boolean(default=True)