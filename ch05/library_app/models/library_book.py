from odoo import api, fields, models
from odoo.exceptions import Warning


# Ch03
def check_isbn(isbn):
    digits = [int(x) for x in isbn if x.isdigit()]
    if len(isbn)==13:
        ponderators = [1, 3] * 6
        total = sum(a * b for a,b in zip(digits[:12], ponderators))
        remain = total % 10
        check = 10 - remain if remain != 0 else 0
        return digits[-1] == check


class Book(models.Model):
    _name = 'library.book'
    _description = 'Book'

    name = fields.Char('Title', required=True)
    isbn = fields.Char('ISBN')
    active = fields.Boolean('Active?', default=True)
    date_published = fields.Date()
    image = fields.Binary('Cover')
    publisher_id = fields.Many2one('res.partner', string='Publisher')
    author_ids = fields.Many2many('res.partner', string='Authors')

    @api.multi
    def button_check_isbn(self):
        for book in self:
            if not book.isbn:
               raise Warning(
                  'Please provide an ISBN13 for %s' % book.name) 
            if book.isbn and not check_isbn(book.isbn):
               raise Warning(
                  '%s is an invalid ISBN' % book.isbn) 
