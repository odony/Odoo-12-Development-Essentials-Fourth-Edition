from odoo.tests.common import TransactionCase 
 
class TestBook(TransactionCase): 
 
    def setUp(self, *args, **kwargs): 
        result = super(TestBook, self).setUp(*args, **kwargs) 
        user_admin = self.env.ref('base.user_demo') 
        self.env= self.env(user=user_demo) 
        return result

    def test_create(self): 
        "Create a Book" 
        Book = self.env['library.book'] 
        book = Book.create({'name': 'Odoo Development Essentials'}) 
        self.assertEqual(book.active, True)

    def test_check_isbn(self): 
        "Check valid ISBN" 
        Book = self.env['library.book'] 
        book = Book.create({
            'name': 'Odoo Development Essentials',
            'isbn': '978-1-78439-279-6'})
        self.assertTrue(book.check_isbn())
