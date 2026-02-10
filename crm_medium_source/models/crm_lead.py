from odoo import models, fields, api


class CrmLead(models.Model):
    _inherit = "crm.lead"

    source_gravity = fields.Char(
        string="Source (Gravity)",
        help="Free text source, auto-creates CRM Source if missing",
    )

    medium_gravity = fields.Char(
        string="Medium (Gravity)",
        help="Free text medium, auto-creates CRM Medium if missing",
    )

    @api.onchange('source_gravity')
    def _onchange_source_gravity(self):
        """On change: attach existing Source if name matches."""
        if self.source_gravity and self.source_gravity.strip():
            name = self.source_gravity.strip()
            src = self.env['utm.source'].search([('name', '=ilike', name)], limit=1)
            if src:
                self.source_id = src.id
        else:
            self.source_id = False

    @api.onchange('medium_gravity')
    def _onchange_medium_gravity(self):
        """On change: attach existing Medium if name matches."""
        if self.medium_gravity and self.medium_gravity.strip():
            name = self.medium_gravity.strip()
            med = self.env['utm.medium'].search([('name', '=ilike', name)], limit=1)
            if med:
                self.medium_id = med.id
        else:
            self.medium_id = False

    @api.model_create_multi
    def create(self, vals_list):
        """Sync source/medium before creating the lead."""
        for vals in vals_list:
            self._prepare_source_medium(vals)
        return super().create(vals_list)

    def write(self, vals):
        """Sync source/medium before updating the lead."""
        self._prepare_source_medium(vals)
        return super().write(vals)

    def _prepare_source_medium(self, vals):
        """Create or find Source/Medium from free text fields and update vals."""
        
        # ---- SOURCE ----
        if 'source_gravity' in vals and vals.get('source_gravity'):
            source_name = vals['source_gravity'].strip()
            if source_name:
                source = self.env["utm.source"].search(
                    [("name", "=ilike", source_name)],
                    limit=1,
                )
                if not source:
                    source = self.env["utm.source"].create({"name": source_name})
                vals['source_id'] = source.id

        # ---- MEDIUM ----
        if 'medium_gravity' in vals and vals.get('medium_gravity'):
            medium_name = vals['medium_gravity'].strip()
            if medium_name:
                medium = self.env["utm.medium"].search(
                    [("name", "=ilike", medium_name)],
                    limit=1,
                )
                if not medium:
                    medium = self.env["utm.medium"].create({"name": medium_name})
                vals['medium_id'] = medium.id