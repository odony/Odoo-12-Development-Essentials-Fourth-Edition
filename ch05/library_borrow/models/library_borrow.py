from odoo import fields, models


class Borrow(models.Model):
    _name = 'library.borrow'
    _description = 'Book Borrowing'
   book_id = fields.Many2one('library.book', name='Book')
   member_id = fields.Many2one('library.member', name='Member')

