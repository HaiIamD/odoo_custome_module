{
    'name': ' Module Custome Dimas',
    'version': '14.0.1.0.0',
    'category': 'purchase',
    'summary': 'Purchase Customer Module',
    'description': """
    Ini merupakan module purchase buatan Dimas Toriq Sibarani
    """,
    'website': '',
    'author': 'Dimas Toriq Sibarani',
    'depends': ['web', 'base','product'],
    'data': [
        'security/ir.model.access.csv',
        'views/dimas_purchase_action.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
}
