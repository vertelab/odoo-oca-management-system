# Copyright (C) 2010 Savoir-faire Linux (<http://www.savoirfairelinux.com>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Management System - Review",
    'summary': "Adds management reviews.",
    'description': '''
Management System - Review
==========================

    Adds management reviews.

    Features:

        - Reports: Adds printable reports.
        - UI Integration: Extends 2 view(s) in the Odoo interface.
        - Extends Odoo: Builds on mail.thread, mgmtsystem.review, mgmtsystem.review.line.
    ''',
    "version": "18.0.1.0.0",
    "author": "Savoir-faire Linux, Odoo Community Association (OCA)",
    "website": "https://vertel.se/apps/odoo-oca-management-system/mgmtsystem_review",
    "license": "AGPL-3",
    "category": "Management System",
    "depends": ["mgmtsystem_nonconformity", "mgmtsystem_survey"],
    "data": [
        "security/ir.model.access.csv",
        "security/mgmtsystem_review_security.xml",
        "data/ir_sequence.xml",
        "views/mgmtsystem_review.xml",
        "views/res_users.xml",
        "report/review.xml",
        "report/report.xml",
    ],
    "installable": True,
}
