{
   'name': 'Custom Sales Report',
   'version': '1.0',
   'author': 'Suruchi,
   'category': 'Sales',
   'depends': ['base', 'sale'],
   'data': [
       'security/ir.model.access.csv',
       'views/sales_report_view.xml',
       'views/sale_report_menu.xml',

   ],
   'installable': True,
   'auto_install': False,
}