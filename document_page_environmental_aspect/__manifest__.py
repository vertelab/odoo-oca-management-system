##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2010 Savoir-faire Linux (<http://www.savoirfairelinux.com>).
#    License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name": "Environmental Aspects",
    'summary': "Adds environmental aspect document pages.",
    'description': '''
Environmental Aspects
=====================

    Adds environmental aspect document pages.

    Features:

        - UI Integration: Extends 1 view(s) in the Odoo interface.
    ''',
    "version": "18.0.1.0.0",
    "author": "Savoir-faire Linux, Odoo Community Association (OCA)",
    "website": "https://vertel.se/apps/odoo-oca-management-system/document_page_environmental_aspect",
    "license": "AGPL-3",
    "category": "Generic Modules/Others",
    "depends": ["document_page", "mgmtsystem"],
    "data": ["data/document_page.xml", "views/document_page.xml"],
    "installable": True,
}
