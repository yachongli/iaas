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


