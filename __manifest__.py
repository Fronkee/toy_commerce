{
    'name' : 'Toy Commerce',
    'author': 'Fronkee',
    'data':[
        'security/ir.model.access.csv',
        'views/payment.xml',
        'views/deli_config.xml',
        ],
    'category':'Customization',
    'depends':['web','website_sale','base','payment_demo'],
    'application':True,
    'assets':{
        'web.assets_frontend':[
            'toy_commerce/static/src/js/*',
            'toy_commerce/static/src/template/*',
        ],
    }
}