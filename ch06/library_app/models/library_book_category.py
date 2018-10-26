from odoo import fields, models


class BookCategory(models.Model):
    _name = 'library.book.category'
    _description = 'Book Category'

    name = fields.Char('Name', required=True)
    active = fields.Boolean('Active?', default=True)
    parent_id = fields.Many2one(
        'library.book.category',
        name='Parent',)
    child_ids = fields.One2many(
        'library.book.category',
        'parent_id',
        name='Subcategories',
    )
