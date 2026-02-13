{
    'name': 'Estate',
    'version': '1.0',
    'category': 'Real Estate',
    'summary': 'Manage your real estate properties',
    'description':'',
    'website': 'https://www.odoo.com/app/estate',
    'depends': 
    ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/propiedades_inmobiliarias.xml',
        'views/estate_menu.xml'
    ],
    'installable': True,
    'application': True,
}