# -*- coding: utf-8 -*-
# Copyright 2020 Sunflower IT (https://sunflowerweb.nl)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields
import odoo.addons.decimal_precision as dp


class MrpBomLine(models.Model):
    _inherit = 'mrp.bom.line'

    bom_type = fields.Selection(related='bom_id.type')
    replace_product_id = fields.Many2one(
        'product.product', 'Replaces product (kit only)', required=False)
    replace_product_qty = fields.Float(
        'Replace quantity', default=0.0,
        digits=dp.get_precision('Product Unit of Measure'), required=False)
