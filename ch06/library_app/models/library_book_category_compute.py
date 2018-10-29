from odoo import api, fields, models


class BookCategory(models.Model):
    _inherit = 'library.book.category'
    _rec_name = 'complete_name'

    def _get_complete_name(self):
        self.ensure_one()
        if self.parent_id:
            head = self.parent_id._get_complete_name()
            tail = self.name
            return '%s / %s' % (head, tail)
        else:
            return self.name

    @api.depends('name', 'parent_id')
    def _compute_complete_name(self):
        for categ in self:
            if categ.id:
                categ.complete_name = categ._get_complete_name()
            else:
                categ.complete_name = None

    def _search_complete_name(self, operator, value):
        print((operator, value))
        return [
            '|',
                ('name', operator, value),
                '|',
                    ('parent_id.name', operator, value),
                    ('parent_id.parent_id.name', operator, value)]

    def _inverse_complete_name(self):
        for categ in self:
            if categ.complete_name:
                names = categ.complete_name.split(' / ')
                categ.name = names[-1]
                if categ.parent_id and len(names) > 1:
                    categ.parent_id.complete_name = ' / '.join(names[:-1])

    complete_name = fields.Char(
        compute='_compute_complete_name',
        search='_search_complete_name',
        inverse='_inverse_complete_name',
    )

    @api.depends('child_ids')
    def _compute_subcategory_count(self):
        for categ in self:
            categ.subcategory_count = 0
            categ.title_count = 0
            if categ.id:
                children = self.search([('id', 'child_of', categ.id)])
                categ.subcategory_count = len(children)
                if children:
                    Book = self.env['library.book']
                    titles = Book.search_count([('category_id', 'in', children.ids)])
                    categ.title_count = titles

    subcategory_count = fields.Integer(
        string='# Subcategories',
        compute=_compute_subcategory_count)
    title_count = fields.Integer(
        string='# Titles (incl. subcateg.)',
        compute=_compute_subcategory_count)
