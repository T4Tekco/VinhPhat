from odoo import _, models
from odoo.addons.http_routing.models.ir_http import url_for


class Website(models.Model):
    _inherit = "website"

    @staticmethod
    def _get_product_sort_mapping():
        return [
            ("website_sequence asc", _("Featured")),
            ("create_date desc", _("Newest Arrivals")),
            ("name asc", _("Name (A-Z)")),
        ]
