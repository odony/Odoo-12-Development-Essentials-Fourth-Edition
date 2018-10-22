from odoo import fields, models


class Checkout(models.Model):
    _name = 'library.checkout'
    _description = 'Book Checkout'
    member_id = fields.Many2one('library.member', name='Member')
    stage_id = fields.Many2one('library.borrow.stage', name='Stage')
    state = fields.Selection(reference='stage_id.state')
    date_borrowed = fields.Date()
    qty = fields.Integer('Quantity')
    line_ids = fields.One2many(
        'library.checkout.line',
        'parent_id',
        'Checkout Lines'
    )


class CheckoutLine(models.Model):
    _name = 'library.checkout.line'
    _description = 'Book Checkout Line'
    borrow_id = fields.Many2one('library.checkout', name='Checkout')
    book_id = fields.Many2one('library.book', name='Book')
    date_returned = fields.Date()

