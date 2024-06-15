{
    'name' : 'Toy Commerce',
    'author': 'Fronkee',
    'data':[
        'security/ir.model.access.csv',
        'views/payment.xml',
        'views/deli_config.xml',
        # 'views/website_address.xml'
        ],
    'category':'Customization',
    'depends':['web','website_sale','base','payment_demo','sale'],
    'application':True,
    'assets':{
        'web.assets_frontend':[
            'toy_commerce/static/src/js/*',
            'toy_commerce/static/src/template/*',
        ],
    }
}