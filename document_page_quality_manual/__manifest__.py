# Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Quality Manual",
    'summary': "Adds a quality manual document page.",
    'description': '''
Quality Manual
==============

    Adds a quality manual document page.

    Features:

        - Demo Data: Ships pre-configured demo data for the industry.
    ''',
    "version": "18.0.1.0.0",
    "category": "Management System",
    "author": "OpenERP SA, Odoo Community Association (OCA)",
    "website": "https://vertel.se/apps/odoo-oca-management-system/document_page_quality_manual",
    "license": "AGPL-3",
    "depends": ["mgmtsystem_manual"],
    "data": ["data/document_page.xml"],
    "installable": True,
    "auto_install": False,
    "images": ["static/description/quality_manual_form.png"],
}
