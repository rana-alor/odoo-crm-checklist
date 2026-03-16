from odoo import api, fields, models

class CrmLead(models.Model):
    _inherit = "crm.lead"

    checklist_line_ids = fields.One2many("crm.lead.checklist.line","lead_id",string="Checklist Lines")
    checklist_total = fields.Integer(compute="_compute_checklist_progress", string="Checklist Total")
    checklist_done = fields.Integer(compute="_compute_checklist_progress", string="Checklist Done")
    checklist_progress = fields.Float(compute="_compute_checklist_progress", string="Checklist Progress")

    @api.depends("checklist_line_ids", "checklist_line_ids.is_done")
    def _compute_checklist_progress(self):
        for lead in self:
            total = len(lead.checklist_line_ids)
            done = len(lead.checklist_line_ids.filtered("is_done"))
            progress = (done / total * 100.0) if total else 0.0

            lead.checklist_total = total
            lead.checklist_done = done
            lead.checklist_progress = progress

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


