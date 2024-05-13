from odoo import models, fields, _

class purchase_model(models.Model):
    _name = 'purchase.model'

    name = fields.Char(string='Name')
    tanggal = fields.Date(string='Tanggal')
    status = fields.Selection([('draft', 'Draft'),('approve', 'Approve'),('done', 'Done')],default="draft")
    purchase_model_ids = fields.One2many('purchase.model.line','purchase_model_id', string="Purchase Model Ids")
   

class purchase_model_line(models.Model):
    _name='purchase.model.line'

    purchase_model_id = fields.Many2one('purchase.model', string='Purchase model Id')
    product_id = fields.Many2one('product.product',string='Product Id')
    quantity = fields.Float(string="Quantity", default=0)
    uom_id = fields.Many2one('uom.uom',string="Satuan")
