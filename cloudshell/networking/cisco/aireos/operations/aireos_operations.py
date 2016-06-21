from cloudshell.networking.operations.interfaces.configuration_operations_interface import \
    ConfigurationOperationsInterface
from cloudshell.networking.operations.interfaces.send_command_interface import SendCommandInterface
from cloudshell.configuration.cloudshell_shell_core_binding_keys import LOGGER
from cloudshell.configuration.cloudshell_cli_binding_keys import CLI_SERVICE
import inject


class AireOSOperations(ConfigurationOperationsInterface, SendCommandInterface):
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

    def save_configuration(self, destination_host, source_filename, vrf=None):
        return self.cli_service.send_command('help')

    def restore_configuration(self, source_file, config_type, restore_method='override', vrf=None):
        pass

    def send_config_command(self, command):
        return self.cli_service.send_config_command(command)

    def send_command(self, command):
        return self.cli_service.send_command(command)
