from collections import OrderedDict

from cloudshell.networking.operations.connectivity_operations import ConnectivityOperations
import inject
from cloudshell.configuration.cloudshell_shell_core_binding_keys import LOGGER, API, CONTEXT
from cloudshell.configuration.cloudshell_cli_binding_keys import CLI_SERVICE
from cloudshell.cli.command_template.command_template_service import execute_command_map
import cloudshell.networking.cisco.aireos.operations.templates.add_remove_vlan as vlan_templates
import re


class AireOSConnectivity(ConnectivityOperations):
    def __init__(self, cli_service=None, logger=None, api=None):
        self._api = api
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

    @property
    def context(self):
        return inject.instance(CONTEXT)

    @property
    def api(self):
        return inject.instance(API)

    def remove_vlan(self, vlan_range, port_list, port_mode):
        vlan_id = vlan_range
        port_address = port_list
        port_id = self._get_port_id_by_address(port_address)
        interface_name = self._get_interface_name(port_id, vlan_id)
        if interface_name:
            remove_vlan_flow = OrderedDict()
            remove_vlan_flow[vlan_templates.DELETE_INTERFACE] = interface_name
            execute_command_map(remove_vlan_flow)
        else:
            raise Exception('AireOSConnectivity', 'Cannot find vlan with id {0} on port {1}'.format(vlan_id, port_id))

    def add_vlan(self, vlan_range, port_list, port_mode, qnq, ctag):
        vlan_id = vlan_range
        port_address = port_list
        self.logger.debug('VlanID: {0},Port: {1},Mode:{2}'.format(vlan_id, port_address, port_mode))

        port_id = self._get_port_id_by_address(port_address)

        if not self._get_interface_name(port_id, vlan_id):
            interface_name = 'vlan-' + vlan_id
            create_vla_flow = OrderedDict()
            create_vla_flow[vlan_templates.CREATE_VLAN_INTERFACE] = (interface_name, vlan_id)
            create_vla_flow[vlan_templates.CONFIGURE_INTERFACE_PORT] = [interface_name, port_id]
            execute_command_map(create_vla_flow, self.cli_service.send_command)
        else:
            raise Exception('AireOSConnectivity',
                            'Vlan {0} has configured on port {1} already'.format(vlan_id, port_id))

    def _get_port_id_by_address(self, port_address):
        # port = self._get_ports_by_resources_path(port_address)
        port = u'Unit:0Slot:0Port:4Gigabit-Level0x6060001'

        port_id_result = re.search(r'Port:(\d+)', port)
        if port_id_result:
            port_id = port_id_result.group(1)
        else:
            raise Exception('AireOSConnectivity', 'Cannot find port ID')
        return port_id

    def _get_interface_name(self, port_id, vlan_id):
        interface_name = None
        for interface in self._get_interface_summary():
            if interface['port'] == port_id and interface['vlan_id'] == vlan_id:
                interface_name = interface['interface']
        return interface_name

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

    def _get_ports_by_resources_path(self, port_address):
        port_resource_map = self.api.GetResourceDetails(self.context.resource.name)
        temp_port_name = self._get_resource_full_name(port_address, port_resource_map)
        if not temp_port_name:
            self.logger.error('Interface was not found')
            raise Exception('Interface {0} was not found'.format(port_address))
        port_name_splited = temp_port_name.split('/')[-1].split('-', 1)
        if len(port_name_splited) > 1:
            port_name = "{0}-{1}".format(port_name_splited[0], port_name_splited[1].replace('-', '/'))
        elif len(port_name_splited) == 1:
            port_name = "{0}".format(port_name_splited[0])
        else:
            raise Exception('JuniperJunosHandler', 'Get incorrect port description by API')
        return port_name

    def _get_resource_full_name(self, port_resource_address, resource_details_map):
        result = None
        for port in resource_details_map.ChildResources:
            if port.FullAddress in port_resource_address and port.FullAddress == port_resource_address:
                return port.Name
            if port.FullAddress in port_resource_address and port.FullAddress != port_resource_address:
                result = self._get_resource_full_name(port_resource_address, port)
            if result is not None:
                return result
        return result
