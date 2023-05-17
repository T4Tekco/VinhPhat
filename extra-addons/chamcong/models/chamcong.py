from odoo import models, fields, api

class Timekeeping(models.Model):
    # _inherit = "product.product"
    _name = 'chamcong'
    _description = 'Timekeeping'

    user_id = fields.Many2one('res.partner', string='User',)
    product_id = fields.Many2one(
        'product.product',
        string='Product',
        
        required=True)
    
    quantity = fields.Integer(string='Quantity')

    datetime = fields.Datetime(
        string='Time Timekeeping', 
        default=lambda self: fields.Datetime.now(), 
        
        widget="datetime")

