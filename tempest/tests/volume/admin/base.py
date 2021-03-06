# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 OpenStack, LLC
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


from tempest import config
import tempest.services.volume.json.admin.volume_types_client \
        as volume_types_json_client
import tempest.services.volume.xml.admin.volume_types_client \
        as volume_types_xml_client
from tempest.tests.volume.base import BaseVolumeTest


class BaseVolumeAdminTest(BaseVolumeTest):
    """Base test case class for all Volume Admin API tests."""
    @classmethod
    def setUpClass(cls):
        super(BaseVolumeAdminTest, cls).setUpClass()
        cls.config = config.TempestConfig()
        cls.adm_user = cls.config.identity.admin_username
        cls.adm_pass = cls.config.identity.admin_password
        cls.adm_tenant = cls.config.identity.admin_tenant_name
        cls.auth_url = cls.config.identity.uri

        if not cls.adm_user and cls.adm_pass and cls.adm_tenant:
            msg = ("Missing Volume Admin API credentials "
                   "in configuration.")
            raise cls.skipException(msg)

    @classmethod
    def tearDownClass(cls):
        super(BaseVolumeAdminTest, cls).tearDownClass()


class BaseVolumeAdminTestJSON(BaseVolumeAdminTest):
    @classmethod
    def setUpClass(cls):
        cls._interface = "json"
        super(BaseVolumeAdminTestJSON, cls).setUpClass()
        cls.client = volume_types_json_client.\
        VolumeTypesClientJSON(cls.config, cls.adm_user, cls.adm_pass,
                              cls.auth_url, cls.adm_tenant)


class BaseVolumeAdminTestXML(BaseVolumeAdminTest):
    @classmethod
    def setUpClass(cls):
        cls._interface = "xml"
        super(BaseVolumeAdminTestXML, cls).setUpClass()
        cls.client = volume_types_xml_client.\
        VolumeTypesClientXML(cls.config, cls.adm_user, cls.adm_pass,
                             cls.auth_url, cls.adm_tenant)
