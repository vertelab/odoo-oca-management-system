# Copyright (C) 2010 Savoir-faire Linux (<http://www.savoirfairelinux.com>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Document Management - Wiki - Work Instructions",
    'summary': "Adds work instruction document pages.",
    'description': '''
Document Management - Wiki - Work Instructions
==============================================

    Adds work instruction document pages.

    Features:

        - UI Integration: Extends 1 view(s) in the Odoo interface.
    ''',
    "version": "18.0.1.0.0",
    "author": "Savoir-faire Linux,Odoo Community Association (OCA)",
    "website": "https://vertel.se/apps/odoo-oca-management-system/document_page_work_instruction",
    "license": "AGPL-3",
    "category": "Management System",
    "depends": ["document_page", "mgmtsystem"],
    "data": ["data/document_page.xml", "views/document_page_work_instructions.xml"],
    "installable": True,
}
