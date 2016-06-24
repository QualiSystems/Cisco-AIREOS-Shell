from collections import OrderedDict
import time

from cloudshell.networking.operations.interfaces.configuration_operations_interface import \
    ConfigurationOperationsInterface
from cloudshell.networking.operations.interfaces.send_command_interface import SendCommandInterface
from cloudshell.networking.operations.interfaces.firmware_operations_interface import FirmwareOperationsInterface
from cloudshell.networking.operations.interfaces.power_operations_interface import PowerOperationsInterface
from cloudshell.configuration.cloudshell_shell_core_binding_keys import LOGGER, CONTEXT, API
from cloudshell.configuration.cloudshell_cli_binding_keys import CLI_SERVICE
from cloudshell.shell.core.context_utils import get_attribute_by_name
import cloudshell.networking.cisco.aireos.operations.templates.save_restore_configuration as save_restore
from cloudshell.cli.command_template.command_template_service import execute_command_map
import inject
import re


class AireOSOperations(ConfigurationOperationsInterface, SendCommandInterface, FirmwareOperationsInterface,
                       PowerOperationsInterface):
    def __init__(self, cli_service=None, logger=None):
        self._cli_service = cli_service
        self._logger = logger

    @property
    def logger(self):
        if not self._logger:
            self._logger = inject.instance(LOGGER)
        return self._logger

    @property
    def cli_service(self):
        if not self._cli_service:
            self._cli_service = inject.instance(CLI_SERVICE)
        return self._cli_service

    @property
    def context(self):
        return inject.instance(CONTEXT)

    @property
    def api(self):
        return inject.instance(API)

    def save_configuration(self, destination_host, source_filename, vrf=None):
        system_name = self.context.resource.fullname
        system_name = re.sub(r'[\.\s]', '_', system_name)

        if source_filename and source_filename.lower() == 'startup':
            config_type = 'config'
        else:
            config_type = 'run-config'

        file_name = "{0}-{1}-{2}".format(system_name, source_filename, time.strftime("%d%m%y-%H%M%S", time.localtime()))
        backup_location = ''
        if not destination_host:
            backup_location = get_attribute_by_name('Backup Location')
            if not backup_location:
                raise Exception('AireOSOperations', "Backup location or path is empty")
        else:
            backup_location = destination_host

        destanation_params = re.search(r'^(?P<protocol>.+)\://(?P<host>[^/]+)(?P<path>/.+)$', backup_location)
        if not destanation_params:
            raise Exception('AireOSOperations', 'Incorrect Backup location')

        destanation_dict = destanation_params.groupdict()
        protocol = destanation_dict['protocol']
        host = destanation_dict['host']
        path = destanation_dict['path']

        save_flow = OrderedDict()
        save_flow[save_restore.SAVE_CONFIGURATION_DATATYPE] = config_type
        save_flow[save_restore.SAVE_CONFIGURATION_MODE] = protocol
        save_flow[save_restore.SAVE_CONFIGURATION_SERVERIP] = host
        save_flow[save_restore.SAVE_CONFIGURATION_FILENAME] = file_name
        save_flow[save_restore.SAVE_CONFIGURATION_PATH] = path
        execute_command_map(save_flow, self.cli_service.send_command)

        self.send_command(save_restore.SAVE_CONFIGURATION_START.get_command())

        return file_name

    def restore_configuration(self, source_file, config_type, restore_method='override', vrf=None):
        pass

    def send_config_command(self, command):
        return self.cli_service.send_config_command(command)

    def send_command(self, command):
        return self.cli_service.send_command(command)

    def update_firmware(self, remote_host, file_path, size_of_firmware):
        pass

    def shutdown(self):
        pass
