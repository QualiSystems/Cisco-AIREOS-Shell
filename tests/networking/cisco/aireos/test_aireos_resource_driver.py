from unittest import TestCase, skip

from cloudshell.networking.cisco.aireos.aireos_resource_driver import AireOSResourceDriver

@skip
class TestAireOSResourceDriver(TestCase):
    def setUp(self):
        self._instance = AireOSResourceDriver()

    def test_ini(self):
        pass
