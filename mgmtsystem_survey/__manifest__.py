# Copyright (C) 2010 Savoir-faire Linux (<http://www.savoirfairelinux.com>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Management System - Survey",
    'summary': "Links management system reviews to surveys.",
    'description': '''
Management System - Survey
==========================

    Links management system reviews to surveys.

    Features:

        - UI Integration: Extends 1 view(s) in the Odoo interface.
    ''',
    "version": "18.0.1.0.0",
    "author": "Savoir-faire Linux, Odoo Community Association (OCA)",
    "website": "https://vertel.se/apps/odoo-oca-management-system/mgmtsystem_survey",
    "license": "AGPL-3",
    "category": "Management System",
    "depends": ["mgmtsystem", "survey"],
    "data": ["views/survey_survey.xml"],
    "installable": True,
    "development_status": "Beta",
    "maintainers": ["max3903"],
}
