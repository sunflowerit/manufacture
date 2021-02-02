# -*- coding: utf-8 -*-
# Copyright 2020 Sunflower IT (https://sunflowerweb.nl)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class MrpBomLine(models.Model):
    _name = 'mrp.bom.line'

    replace_product_id = fields.Many2one(
        'product.poduct', 'Replaces product', required=False)
    replace_product_qty = fields.Float(
        'Replace quantity', default=1.0,
        digits=dp.get_precision('Product Unit of Measure'), required=False)

