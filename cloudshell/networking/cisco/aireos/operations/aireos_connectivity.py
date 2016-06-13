from cloudshell.networking.operations.connectivity_operations import ConnectivityOperations
import inject
from cloudshell.configuration.cloudshell_shell_core_binding_keys import LOGGER


class AireOSConnectivity(ConnectivityOperations):
    @property
    def logger(self):
        return inject.instance(LOGGER)

    def remove_vlan(self, vlan_range, port_list, port_mode):
        pass

    def add_vlan(self, vlan_range, port_list, port_mode, qnq, ctag):
        pass
