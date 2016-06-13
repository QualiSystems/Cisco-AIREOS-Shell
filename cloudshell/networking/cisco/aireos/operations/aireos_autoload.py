from cloudshell.networking.operations.interfaces.autoload_operations_interface import AutoloadOperationsInterface
import inject
from cloudshell.configuration.cloudshell_snmp_binding_keys import SNMP_HANDLER
from cloudshell.configuration.cloudshell_shell_core_binding_keys import LOGGER


class AireOSAutoload(AutoloadOperationsInterface):
    def __init__(self):
        self._snmp_handler = None

    @property
    def snmp_handler(self):
        if self._snmp_handler is None:
            self._snmp_handler = inject.instance(SNMP_HANDLER)
        return self._snmp_handler

    @property
    def logger(self):
        return inject.instance(LOGGER)

    def discover(self):
        pass
