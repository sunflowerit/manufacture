# -*- coding: utf-8 -*-
# Copyright 2020 Sunflower IT (https://sunflowerweb.nl)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
import odoo.addons.decimal_precision as dp


class StockMove(models.Model):
    _inherit = 'stock.move'

    def _generate_move_phantom(self, bom_line, quantity):
        move = super(StockMove, self)._generate_move_phantom(bom_line, quantity)
        if move:
            move.replace_product_id = bom_line.replace_product_id
            move.replace_product_qty = bom_line.replace_product_qty
        return move

    replace_product_id = fields.Many2one(
        'product.product', 'Replaces product (kit only)', required=False)
    replace_product_qty = fields.Float(
        'Replace quantity', default=0.0,
        digits=dp.get_precision('Product Unit of Measure'), required=False)

    @api.multi
    def action_confirm(self):
        moves = super(StockMove, self).action_confirm()
        replacements = moves.filtered('replace_product_id').mapped(
            lambda m: (m.replace_product_id, m.replace_product_qty or 1.0)
        )
        for product, qty in replacements:
            match = moves.filtered(lambda m: m.product_id == product and m.product_qty == qty)[:1]
            if match:
                match.action_cancel()
                match.unlink()
                moves -= match
        return moves
