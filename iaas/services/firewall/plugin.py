import copy

from neutron_lib import context as ncontext
from neutron_lib.plugins import directory

from neutron.api.v2 import attributes as attrs
from neutron.api.v2 import base as napi_base
from neutron.db import agentschedulers_db
from neutron.db import servicetype_db as st_db
from neutron.extensions import flavors
from neutron import service
from neutron.services.flavors import flavors_plugin
from neutron.services import provider_configuration as pconf
from neutron.services import service_base
from neutron_lib import constants as n_constants
from neutron_lib import exceptions as n_exc
from neutron_lib.plugins import constants
from oslo_log import log as logging
from oslo_utils import encodeutils

from iaas import agent_scheduler as agent_shceduler_v1
import iaas.common.cert_manager
from iaas.common.tls_utils import cert_parser
from iaas.db.dns import dns_dbv1 as ddbv1
from iaas.db.dns import models
from iaas.extensions import dnsv1
from iaas.services.dns import constants as dns_const
from iaas.services.dns import data_models

LOG = logging.getLogger(__name__)
CERT_MANAGER_PLUGIN = iaas.common.cert_manager.get_backend()

class DnsPlugingV1(dnsv1.DnsPluginBaseV1):
    support_extensions= [
        "zdns"
    ]

    agent_notifiers = (
    )

    def __init__(self):
        self.db = ddbv1.DnsPluginDbv1()

    def create_zone(self):
        pass

    def update_zone(self):
        pass

    def delete_zone(self):
        pass

    def get_zone(self):
        pass

    def get_zones(self):
        pass

