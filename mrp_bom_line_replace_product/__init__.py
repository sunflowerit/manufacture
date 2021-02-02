# -*- encoding: utf-8 -*-
from . import models
from . import wizards
from openerp import SUPERUSER_ID


def set_bill_of_material_references(cr, registry):
    """
    This function adds a reference record to each existing boms when the
    module is installed. This ensures that each bom has a reference
    so that the module works properly.
    """
    bom_obj = registry['mrp.bom']
    ref_obj = registry['mrp.bom.reference']
    bom_ids = bom_obj.search(cr, SUPERUSER_ID, [])
    for bom in bom_obj.browse(cr, SUPERUSER_ID, bom_ids):
        if not bom.reference_id:
            ref_obj.create(cr, SUPERUSER_ID, {'bom_id': bom.id})
