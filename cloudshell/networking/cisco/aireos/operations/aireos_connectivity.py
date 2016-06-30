from cloudshell.networking.operations.connectivity_operations import ConnectivityOperations
import inject
from cloudshell.configuration.cloudshell_shell_core_binding_keys import LOGGER
from cloudshell.configuration.cloudshell_cli_binding_keys import CLI_SERVICE
from cloudshell.cli.command_template.command_template_service import execute_command_map
import cloudshell.networking.cisco.aireos.operations.templates.add_remove_vlan as vlan_templates
import re


class AireOSConnectivity(ConnectivityOperations):
    def __init__(self, cli_service=None, logger=None):
        self._logger = logger
        self._cli_service = cli_service

    @property
    def logger(self):
        return inject.instance(LOGGER)

    @property
    def cli_service(self):
        if self._cli_service is None:
            self._cli_service = inject.instance(CLI_SERVICE)
        return self._cli_service

    def remove_vlan(self, vlan_range, port_list, port_mode):
        pass

    def add_vlan(self, vlan_range, port_list, port_mode, qnq, ctag):
        """Configure specified vlan range in specified switchport mode on provided port

        :param vlan_range: range of vlans to be added, if empty, and switchport_type = trunk,
        trunk mode will be assigned
        :param port: List of interfaces Resource Full Address
        :param port_mode: type of adding vlan ('trunk' or 'access')
        :param qnq: QNQ parameter for switchport mode dot1nq
        :param ctag: CTag details
        :return: success message
        :rtype: string
        """
        pp=u'Unit:0Slot:0Port:1Gigabit-Level0x6060001'

        return self._get_interface_summary()

    def _get_interface_summary(self):
        out = execute_command_map({vlan_templates.INTERFACE_SUMMARY: []}, self.cli_service.send_command)
        result_list = []
        for line in out.splitlines():
            result = re.search(r'^(?P<interface>\S+)\s+' +
                               r'(?P<port>\d*|N\/A)\s+' +
                               r'(?P<vlan_id>\d*|N\/A|untagged)\s+' +
                               r'(?P<ip_address>\S+)?', line)
            if result:
                result_list.append(result.groupdict())

        return result_list

    # def _get_interface_
