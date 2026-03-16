from odoo import api, fields, models

class CrmLead(models.Model):
    _inherit = "crm.lead"

    checklist_line_ids = fields.One2many("crm.lead.checklist.line","lead_id",string="Checklist Lines")

    @api.model_create_multi
    def create(self, vals_list):
        leads = super().create(vals_list)
        checklist_items = self.env["crm.lead.checklist.item"].search(
            [("active", "=", True)],
            order="sequence, id",
        )

        for lead in leads:
            line_vals = []
            for item in checklist_items:
                line_vals.append({
                    "lead_id": lead.id,
                    "item_id": item.id,
                    "sequence": item.sequence,
                    "is_done": False,
                })
            if line_vals:
                self.env["crm.lead.checklist.line"].create(line_vals)

        return leads