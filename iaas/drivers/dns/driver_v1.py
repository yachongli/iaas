from oslo_log import log as logging

LOG = logging.getLogger(__name__)
# CERT_MANAGER_PLUGIN = neutron_lbaas.common.cert_manager.get_backend()
VERSION = '1.0'


class DnsDriverV1(object):
    def __init__(self,plugin,env='Project'):
        super(DnsDriverV1,self).__init__()
        self.Dns = DnsManager(self)

        LOG.debug(("DnsAasV1Driver: initializing, version= %s, impl= %s,env=%s"))

