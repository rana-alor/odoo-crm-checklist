from odoo import fields, models

class CrmLeadChecklistLine(models.Model):
    _name = "crm.lead.checklist.line"
    _description = "CRM Lead Checklist Line"
    _order = "sequence, id"

    lead_id = fields.Many2one("crm.lead",required=True,ondelete="cascade")
    item_id = fields.Many2one("crm.lead.checklist.item",required=True,ondelete="cascade")
    name = fields.Char(related="item_id.name",store=True)
    sequence = fields.Integer(default=10)
    is_done = fields.Boolean(string="Done")