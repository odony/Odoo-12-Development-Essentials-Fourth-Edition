from odoo import api, fields, models
 
class Book(models.Model): 
    _inherit = 'library.book' 
    is_available = fields.Boolean('Is Available?', readonly=False)
