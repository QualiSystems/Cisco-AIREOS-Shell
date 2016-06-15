from cloudshell.networking.cisco.aireos.aireos_bootstrap import AireOSBootstrap
from cloudshell.networking.cisco.aireos.operations.aireos_connectivity import AireOSConnectivity
from cloudshell.networking.networking_resource_driver_interface import NetworkingResourceDriverInterface
from cloudshell.shell.core.resource_driver_interface import ResourceDriverInterface
from cloudshell.shell.core.context_utils import ContextFromArgsMeta
import cloudshell.networking.cisco.aireos.aireos_config as driver_config
from cloudshell.networking.cisco.aireos.operations.aireos_autoload import AireOSAutoload


class AireOSResourceDriver(ResourceDriverInterface, NetworkingResourceDriverInterface):
    __metaclass__ = ContextFromArgsMeta

    def __init__(self):
        self._autoload = None
        self._connectivity = None
        bootstrap = AireOSBootstrap()
        bootstrap.add_config(driver_config)
        bootstrap.initialize()

    @property
    def autoload(self):
        if self._autoload is None:
            self._autoload = AireOSAutoload()
        return self._autoload

    @property
    def connectivity(self):
        if self._connectivity is None:
            self._connectivity = AireOSConnectivity()
        return self._connectivity

    def get_inventory(self, context):
        return self.autoload.discover()

    def send_custom_command(self, context, command):
        pass

    def update_firmware(self, context, remote_host, file_path):
        pass

    def shutdown(self, context):
        pass

    def ApplyConnectivityChanges(self, context, request):
        self.connectivity.apply_connectivity_changes(request)

    def send_custom_config_command(self, context, command):
        pass

    def restore(self, context, path, config_type, restore_method):
        pass

    def save(self, context, folder_path, configuration_type):
        pass

    def initialize(self, context):
        pass

    def cleanup(self):
        pass
