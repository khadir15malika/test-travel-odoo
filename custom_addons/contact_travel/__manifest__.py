#{
    #'name': 'Contact Travel',
    #'version': '1.0',
    #'summary': 'Gestion des voyages pour les contacts',
    #'description': 'Ce module permet de gérer les voyages pour les contacts.',
    #'category': 'Sales/CRM',
    #'author': 'Malika',
    #'website': 'www.contacttravel.com',
    #'depends': ['base', 'crm'],
    #'data': [
        #'views/contact_travel_views.xml', w dima win ykoun files ta3 python drlhm __init__.py kima hadii win models
    #],
    #'installable': True,
    #'application': True,
#} ldork ma lgahouch hhhh pc ta3i thqil tani hhhh

# -*- coding: utf-8 -*- bach n7otoh f depends, lzm dima DCdreri haka ki ta5dmi bl many2one wela on 2many t7oti module ta3hm f dependsdcr

{   
    'name': "Contact Travel",

    'summary': """Contact Travel Software""",

    'description': """

       this module allows you to manage trips for contacts

    """,
    'category': 'Tools',
    'version': '16.0.1.0.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/voyage.xml'
    ],
    'installation': True,
    'application': True,
    'auto_install': False
}    











