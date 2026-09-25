# Copyright 2024 - TODAY, Escodoo
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Management System - Nonconformity Maintenance Equipment",
    'summary': "Links nonconformities to maintenance equipment.",
    'description': '''
Management System - Nonconformity Maintenance Equipment
=======================================================

    Links nonconformities to maintenance equipment.

    Features:

        - UI Integration: Extends 1 view(s) in the Odoo interface.
        - Extends Odoo: Builds on mgmtsystem.nonconformity.
    ''',
    "version": "18.0.1.0.0",
    "author": "Escodoo, Odoo Community Association (OCA)",
    "website": "https://vertel.se/apps/odoo-oca-management-system/mgmtsystem_nonconformity_maintenance_equipment",
    "license": "AGPL-3",
    "category": "Management System",
    "depends": ["maintenance", "mgmtsystem_nonconformity"],
    "data": [
        "views/mgmtsystem_nonconformity.xml",
    ],
}
