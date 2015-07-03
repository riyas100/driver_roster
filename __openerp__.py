# -*- coding: utf-8 -*-
{
    "name" : "Driver Roster",
    'version' : '1.0',
    'author' : 'Muhammed Riyas',
    "category" : "sales",
    "description": """This module will assign sales order to driver for delivery.
        """,
    "depends": ['hr','sale'],
    "data" : [
            'security/ir.model.access.csv',
            'driver_roster_view.xml'
            ],
    'css': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
