# -*- coding: utf-8 -*-
#################################################################################
# Author      : CFIS (<https://www.cfis.store/>)
# Copyright(c): 2017-Present CFIS.
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://www.cfis.store/>
#################################################################################

{
    "name": "Export Attachments / Attachments Export to Zip",
    "summary": "This module helps the admin user to Export Attachments into Zip file",
    "version": "15.0.1",
    "description": """
        This module helps the admin user to Export Attachments into Zip file
        Export Attachments
        Export to Zip
        Zip Attachments
        Attachments Zip
        Attachment Export
        Export Zip Attachment
        Zip Export Attachment
    """,    
    "author": "CFIS",
    "maintainer": "CFIS",
    "license" :  "Other proprietary",
    "website": "https://www.cfis.store",
    "images": ["images/attachments_export_to_zip.png"],
    "category": "Project",
    "depends": [
        "base",
    ],
    "data": [
        "security/ir.model.access.csv",
        "wizard/ir_attachment_export.xml",
    ],
    "qweb": [],
    "installable": True,
    "application": True,
    "price"                :  9,
    "currency"             :  "EUR",
}
