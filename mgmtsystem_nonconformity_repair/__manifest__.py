# Copyright 2020 - TODAY, Escodoo
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Mgmtsystem Nonconformity Repair",
    "summary": """
        Bridge module between Repair and Non Conformities""",
    "version": "18.0.1.0.0",
    "license": "AGPL-3",
    "author": "Escodoo,Odoo Community Association (OCA)",
    "website": "https://vertel.se/apps/odoo-oca-management-system/mgmtsystem_nonconformity_repair",
    "depends": [
        "mgmtsystem_nonconformity",
        "repair",
    ],
    "data": [
        "views/mgmtsystem_nonconformity.xml",
    ],
    "demo": [],
}
