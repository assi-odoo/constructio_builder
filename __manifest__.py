{
    'name' : 'construction builder',
    'depends':[
        'base',
    ],
    'license':'LGPL-3',
    'application' : True,
    'installable' :True,
    'data':[
        'security/ir.model.access.csv',
        'views/construction_view.xml',
        'views/construction_orders.xml',
        'views/construction_menu.xml'
    ],
    'image':['static/description/module_icon.jpg'],
}