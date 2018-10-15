{ 
'name': 'Library Members and Borrowing', 
'description': 'Use library cards for people to borrow books.', 
'author': 'Daniel Reis', 
'data': [
    'security/ir.model.access.csv',
    'views/book_view.xml',
    'views/book_list_template.xml',
    'views/library_menu.xml',
],
'depends': [
    'library_app',
    'mail',
], 
'application': False, 
} 

