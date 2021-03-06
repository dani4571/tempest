# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# Copyright 2012 NTT Data
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import urllib

from lxml import etree

from tempest.common.rest_client import RestClientXML
from tempest.services.compute.xml.common import Document
from tempest.services.compute.xml.common import Element
from tempest.services.compute.xml.common import xml_to_json
from tempest.services.compute.xml.common import XMLNS_11
from tempest.services.compute.xml.quotas_client import QuotasClientXML


class AdminQuotasClientXML(QuotasClientXML):

    def __init__(self, config, username, password, auth_url, tenant_name=None):
        super(AdminQuotasClientXML, self).__init__(config, username, password,
                                                   auth_url, tenant_name)

    def update_quota_set(self, tenant_id, injected_file_content_bytes=None,
                         metadata_items=None, ram=None, floating_ips=None,
                         key_pairs=None, instances=None,
                         security_group_rules=None, injected_files=None,
                         cores=None, injected_file_path_bytes=None,
                         security_groups=None):
        """
        Updates the tenant's quota limits for one or more resources
        """
        post_body = Element("quota_set",
                            xmlns=XMLNS_11)

        if injected_file_content_bytes is not None:
            post_body.add_attr('injected_file_content_bytes',
                               injected_file_content_bytes)

        if metadata_items is not None:
            post_body.add_attr('metadata_items', metadata_items)

        if ram is not None:
            post_body.add_attr('ram', ram)

        if floating_ips is not None:
            post_body.add_attr('floating_ips', floating_ips)

        if key_pairs is not None:
            post_body.add_attr('key_pairs', key_pairs)

        if instances is not None:
            post_body.add_attr('instances', instances)

        if security_group_rules is not None:
            post_body.add_attr('security_group_rules', security_group_rules)

        if injected_files is not None:
            post_body.add_attr('injected_files', injected_files)

        if cores is not None:
            post_body.add_attr('cores', cores)

        if injected_file_path_bytes is not None:
            post_body.add_attr('injected_file_path_bytes',
                               injected_file_path_bytes)

        if security_groups is not None:
            post_body.add_attr('security_groups', security_groups)

        resp, body = self.put('os-quota-sets/%s' % str(tenant_id),
                              str(Document(post_body)),
                              self.headers)
        body = xml_to_json(etree.fromstring(body))
        body = self._format_quota(body)
        return resp, body
