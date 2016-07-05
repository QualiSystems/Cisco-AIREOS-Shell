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

        file_name = "{0}-{1}-{2}".format(system_name, config_type, time.strftime("%d%m%y-%H%M%S", time.localtime()))
        if not destination_host:
            backup_location = get_attribute_by_name('Backup Location')
            if not backup_location:
                raise Exception('AireOSOperations', "Backup location or path is empty")
        else:
            backup_location = destination_host

        destination_params = re.search(r'^(?P<protocol>.+)\://(?P<host>[^/\:]+)[\:]*(?P<port>\d*)(?P<path>/.+)$',
                                       backup_location)
        if not destination_params:
            raise Exception('AireOSOperations', 'Incorrect Backup location')

        destination_dict = destination_params.groupdict()
        protocol = destination_dict['protocol']
        host = destination_dict['host']
        path = destination_dict['path']
        port = destination_dict['port']

        self.logger.debug(
            'Datatype: {0}, Protocol: {1}, Host: {2}, Path: {3}, File: {4}'.format(config_type, protocol, host, path,
                                                                                   file_name))
        save_flow = OrderedDict()
        save_flow[save_restore.SAVE_CONFIGURATION_DATATYPE] = config_type
        save_flow[save_restore.SAVE_CONFIGURATION_MODE] = protocol
        save_flow[save_restore.SAVE_CONFIGURATION_SERVERIP] = host
        save_flow[save_restore.SAVE_CONFIGURATION_FILENAME] = file_name
        save_flow[save_restore.SAVE_CONFIGURATION_PATH] = path
        if port:
            save_flow[save_restore.SAVE_CONFIGURATION_PORT] = port
        execute_command_map(save_flow, self.cli_service.send_command)

        expected_map = OrderedDict({r'[yY]/[nN]': lambda session: session.send_line('y')})
        error_map = OrderedDict({r'[Ee]rror:': 'Save configuration error, see logs for details'})

        self.cli_service.send_command(save_restore.SAVE_CONFIGURATION_START.get_command(), expected_map=expected_map,
                                      error_map=error_map)

        return file_name

    def restore_configuration(self, source_file, config_type, restore_method='override', vrf=None):

        if not source_file:
            raise Exception('AireOSOperations', 'Configuration URL cannot be empty')

        connection_dict = self._parse_url(source_file)

        restore_flow = OrderedDict()
        datatype = 'config'
        restore_flow[save_restore.RESTORE_CONFIGURATION_DATATYPE] = datatype
        protocol = connection_dict['protocol']
        restore_flow[save_restore.RESTORE_CONFIGURATION_MODE] = protocol
        if 'user' in connection_dict:
            user = connection_dict['user']
            self.logger.debug('Username: ' + user)
            restore_flow[save_restore.RESTORE_CONFIGURATION_USER] = user
        if 'password' in connection_dict:
            password = connection_dict['password']
            self.logger.debug('Password: ' + password)
            restore_flow[save_restore.RESTORE_CONFIGURATION_PASSWORD] = password

        host = connection_dict['host']
        restore_flow[save_restore.RESTORE_CONFIGURATION_SERVERIP] = host
        if 'port' in connection_dict:
            port = connection_dict['port']
            if port:
                self.logger.debug('Port: ' + port)
                restore_flow[save_restore.RESTORE_CONFIGURATION_PORT] = port

        path = connection_dict['path']
        restore_flow[save_restore.RESTORE_CONFIGURATION_PATH] = path
        file_name = connection_dict['filename']
        restore_flow[save_restore.RESTORE_CONFIGURATION_FILENAME] = file_name

        self.logger.debug(
            'Datatype: {0}, Protocol: {1}, Host: {2}, Path: {3}, File: {4}'.format(datatype, protocol, host, path,
                                                                                   file_name))
        execute_command_map(restore_flow, self.cli_service.send_command)

        expected_map = OrderedDict({r'[yY]/[nN]': lambda session: session.send_line('y')})
        error_map = OrderedDict({r'[Ee]rror:': 'Restore configuration error, see logs for details'})

        self.cli_service.send_command(save_restore.RESTORE_CONFIGURATION_START.get_command(), expected_map=expected_map,
                                      error_map=error_map)

    def send_config_command(self, command):
        return self.cli_service.send_config_command(command)

    def send_command(self, command):
        return self.cli_service.send_command(command)

    def update_firmware(self, remote_host, file_path, size_of_firmware):
        if not remote_host and not file_path:
            raise Exception('AireOSOperations', 'Configuration URL cannot be empty')
        if remote_host.endswith('/'):
            remote_host = remote_host[:-1]
        if str(file_path).startswith('/'):
            file_path = file_path[1:]

        url = '{0}/{1}'.format(remote_host, file_path)
        connection_dict = self._parse_url(url)

        restore_flow = OrderedDict()
        datatype = 'code'
        restore_flow[save_restore.RESTORE_CONFIGURATION_DATATYPE] = datatype
        protocol = connection_dict['protocol']
        restore_flow[save_restore.RESTORE_CONFIGURATION_MODE] = protocol
        if 'user' in connection_dict:
            user = connection_dict['user']
            self.logger.debug('Username: ' + user)
            restore_flow[save_restore.RESTORE_CONFIGURATION_USER] = user
        if 'password' in connection_dict:
            password = connection_dict['password']
            self.logger.debug('Password: ' + password)
            restore_flow[save_restore.RESTORE_CONFIGURATION_PASSWORD] = password

        host = connection_dict['host']
        restore_flow[save_restore.RESTORE_CONFIGURATION_SERVERIP] = host
        if 'port' in connection_dict:
            port = connection_dict['port']
            if port:
                self.logger.debug('Port: ' + port)
                restore_flow[save_restore.RESTORE_CONFIGURATION_PORT] = port

        path = connection_dict['path']
        restore_flow[save_restore.RESTORE_CONFIGURATION_PATH] = path
        file_name = connection_dict['filename']
        restore_flow[save_restore.RESTORE_CONFIGURATION_FILENAME] = file_name

        self.logger.debug(
            'Datatype: {0}, Protocol: {1}, Host: {2}, Path: {3}, File: {4}'.format(datatype, protocol, host, path,
                                                                                   file_name))
        execute_command_map(restore_flow, self.cli_service.send_command)

        expected_map = OrderedDict({r'[yY]/[nN]': lambda session: session.send_line('y')})
        error_map = OrderedDict({r'[Ee]rror:': 'Restore configuration error, see logs for details'})

        self.cli_service.send_command(save_restore.RESTORE_CONFIGURATION_START.get_command(), expected_map=expected_map,
                                      error_map=error_map)

    def _parse_url(self, url):
        url_list = str(url).split('@')
        if len(url_list) == 1:
            url_params = re.search(
                r'^(?P<protocol>.+)\://(?P<host>[^/\:\@]+)[\:]*(?P<port>\d*)(?P<path>/.+)\/(?P<filename>[^/]+)$',
                url_list[0])
            url_dict = url_params.groupdict()
        elif len(url_list) == 2:
            url_params_1 = re.search(r'^(?P<protocol>.+)\://(?P<user>[^/\:\@]+)[\:]+(?P<password>[^/\:\@]+)$',
                                     url_list[0])
            url_params_2 = re.search(r'^(?P<host>[^/\:\@]+)[\:]*(?P<port>\d*)(?P<path>/.+)\/(?P<filename>[^/]+)$',
                                     url_list[1])
            url_dict = url_params_1.groupdict()
            url_dict.update(url_params_2.groupdict())
        else:
            raise Exception('AireOSOperations', 'Cannot parse URL, Incorrect url: {0}'.format(url))
        return url_dict

    def shutdown(self):
        pass
