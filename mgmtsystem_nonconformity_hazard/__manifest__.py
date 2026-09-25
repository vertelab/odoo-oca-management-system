# Copyright 2024 - TODAY, Escodoo
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Management System - Nonconformity Hazard",
    'summary': "Links nonconformities to hazards.",
    'description': '''
Management System - Nonconformity Hazard
========================================

    Links nonconformities to hazards.

    Features:

        - UI Integration: Extends 2 view(s) in the Odoo interface.
        - Extends Odoo: Builds on mgmtsystem.hazard, mgmtsystem.nonconformity.
    ''',
    "version": "18.0.1.0.0",
    "author": "Escodoo, Odoo Community Association (OCA)",
    "website": "https://vertel.se/apps/odoo-oca-management-system/mgmtsystem_nonconformity_hazard",
    "license": "AGPL-3",
    "category": "Management System",
    "depends": ["mgmtsystem_hazard", "mgmtsystem_nonconformity"],
    "data": [
        "views/mgmtsystem_hazard.xml",
        "views/mgmtsystem_nonconformity.xml",
    ],
    "autoinstall": True,
}
