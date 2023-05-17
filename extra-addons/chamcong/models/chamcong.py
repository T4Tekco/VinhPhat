# chamcong/models/chamcong.py
from odoo import models, fields, api


class Timekeeping(models.Model):
    _name = 'chamcong'
    _description = 'Timekeeping'

    user = fields.Char(string='User')
    product = fields.Char(string='Product')
    quantity = fields.Integer(string='Quatity')
    datetime = fields.Datetime(string='Time Timekeeping', default=lambda self: fields.Datetime.now(), widget="datetime")

    def show_tree_view(self):
        action = self.env.ref('action_my_model_tree_view').read()[0]
        return action
    
 