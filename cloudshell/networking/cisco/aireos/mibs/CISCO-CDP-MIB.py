# PySNMP SMI module. Autogenerated from smidump -f python CISCO-CDP-MIB
# by libsmi2pysnmp-0.1.3 at Wed Dec  2 12:39:01 2015,
# Python version sys.version_info(major=2, minor=7, micro=6, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( ciscoMgmt, ) = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
( CiscoNetworkAddress, CiscoNetworkProtocol, ) = mibBuilder.importSymbols("CISCO-TC", "CiscoNetworkAddress", "CiscoNetworkProtocol")
( VlanIndex, ) = mibBuilder.importSymbols("CISCO-VTP-MIB", "VlanIndex")
( ifIndex, ) = mibBuilder.importSymbols("IF-MIB", "ifIndex")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Integer32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32")
( DisplayString, TimeStamp, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "TruthValue")

# Objects

ciscoCdpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 23)).setRevisions(("2005-03-21 00:00","2005-03-14 00:00","2001-11-23 00:00","2001-04-23 00:00","2000-11-22 00:00","1998-12-10 00:00","1998-09-16 00:00","1996-07-08 00:00","1995-08-15 00:00","1995-07-27 00:00","1995-01-25 00:00",))
if mibBuilder.loadTexts: ciscoCdpMIB.setOrganization("Cisco System Inc.")
if mibBuilder.loadTexts: ciscoCdpMIB.setContactInfo("       Cisco Systems\nCustomer Service\n\nPostal: 170 West Tasman Drive,\nSan Jose CA 95134-1706.\nUSA\n\nTel: +1 800 553-NETS\n\nE-mail: cs-snmp@cisco.com")
if mibBuilder.loadTexts: ciscoCdpMIB.setDescription("The MIB module for management of the Cisco Discovery\nProtocol in Cisco devices.")
ciscoCdpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 23, 1))
cdpInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 1))
cdpInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 1, 1))
if mibBuilder.loadTexts: cdpInterfaceTable.setDescription("The (conceptual) table containing the status of CDP on\nthe device's interfaces.")
cdpInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 1, 1, 1)).setIndexNames((0, "CISCO-CDP-MIB", "cdpInterfaceIfIndex"))
if mibBuilder.loadTexts: cdpInterfaceEntry.setDescription("An entry (conceptual row) in the cdpInterfaceTable,\ncontaining the status of CDP on an interface.")
cdpInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: cdpInterfaceIfIndex.setDescription("The ifIndex value of the local interface.\n\nFor 802.3 Repeaters on which the repeater ports do not\nhave ifIndex values assigned, this value is a unique\nvalue for the port, and greater than any ifIndex value\nsupported by the repeater; in this case, the specific\nport is indicated by corresponding values of\ncdpInterfaceGroup and cdpInterfacePort, where these\nvalues correspond to the group number and port number\nvalues of RFC 1516.")
cdpInterfaceEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 1, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdpInterfaceEnable.setDescription("An indication of whether the Cisco Discovery Protocol\nis currently running on this interface.  This variable\nhas no effect when CDP is disabled (cdpGlobalRun = FALSE).")
cdpInterfaceMessageInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 254))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdpInterfaceMessageInterval.setDescription("The interval at which CDP messages are to be generated\non this interface.  The default value is 60 seconds.")
cdpInterfaceGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpInterfaceGroup.setDescription("This object is only relevant to interfaces which are\nrepeater ports on 802.3 repeaters.  In this situation,\nit indicates the RFC1516 group number of the repeater\nport which corresponds to this interface.")
cdpInterfacePort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpInterfacePort.setDescription("This object is only relevant to interfaces which are\nrepeater ports on 802.3 repeaters.  In this situation,\nit indicates the RFC1516 port number of the repeater\nport which corresponds to this interface.")
cdpInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 1, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpInterfaceName.setDescription("The name of the local interface as advertised by\nCDP in the Port-ID TLV")
cdpInterfaceExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 1, 2))
if mibBuilder.loadTexts: cdpInterfaceExtTable.setDescription("This table contains the additional CDP configuration on\nthe device's interfaces.")
cdpInterfaceExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 1, 2, 1)).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cdpInterfaceExtEntry.setDescription("An entry in the cdpInterfaceExtTable contains the values\nconfigured for Extented Trust TLV and COS (Class of Service)\nfor Untrusted Ports TLV on an interface which supports the\nsending of these TLVs.")
cdpInterfaceExtendedTrust = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 1, 2, 1, 1), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("trusted", 1), ("noTrust", 2), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdpInterfaceExtendedTrust.setDescription("Indicates the value to be sent by Extended Trust TLV.\n\nIf trusted(1) is configured, the value of Extended Trust TLV\nis one byte in length with its least significant bit equal to\n1 to indicate extended trust. All other bits are 0.\n\nIf noTrust(2) is configured, the value of Extended Trust TLV\nis one byte in length with its least significant bit equal to\n0 to indicate no extended trust. All other bits are 0.")
cdpInterfaceCosForUntrustedPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 1, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdpInterfaceCosForUntrustedPort.setDescription("Indicates the value to be sent by COS for Untrusted Ports TLV.")
cdpCache = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2))
cdpCacheTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1))
if mibBuilder.loadTexts: cdpCacheTable.setDescription("The (conceptual) table containing the cached\ninformation obtained via receiving CDP messages.")
cdpCacheEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1)).setIndexNames((0, "CISCO-CDP-MIB", "cdpCacheIfIndex"), (0, "CISCO-CDP-MIB", "cdpCacheDeviceIndex"))
if mibBuilder.loadTexts: cdpCacheEntry.setDescription("An entry (conceptual row) in the cdpCacheTable,\ncontaining the information received via CDP on one\ninterface from one device.  Entries appear when\na CDP advertisement is received from a neighbor\ndevice.  Entries disappear when CDP is disabled\non the interface, or globally.")
cdpCacheIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: cdpCacheIfIndex.setDescription("Normally, the ifIndex value of the local interface.\nFor 802.3 Repeaters for which the repeater ports do not\nhave ifIndex values assigned, this value is a unique\nvalue for the port, and greater than any ifIndex value\nsupported by the repeater; the specific port number in\nthis case, is given by the corresponding value of\ncdpInterfacePort.")
cdpCacheDeviceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: cdpCacheDeviceIndex.setDescription("A unique value for each device from which CDP messages\nare being received.")
cdpCacheAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 3), CiscoNetworkProtocol()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpCacheAddressType.setDescription("An indication of the type of address contained in the\ncorresponding instance of cdpCacheAddress.")
cdpCacheAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 4), CiscoNetworkAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpCacheAddress.setDescription("The (first) network-layer address of the device\nas reported in the Address TLV of the most recently received\nCDP message.  For example, if the corresponding instance of\ncacheAddressType had the value 'ip(1)', then this object \nwould be an IPv4-address.  If the neighbor device is \nSNMP-manageable, it is supposed to generate its CDP messages\nsuch that this address is one at which it will receive SNMP\nmessages. Use cdpCtAddressTable to extract the remaining\naddresses from the Address TLV received most recently.")
cdpCacheVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpCacheVersion.setDescription("The Version string as reported in the most recent CDP\nmessage.  The zero-length string indicates no Version\nfield (TLV) was reported in the most recent CDP\nmessage.")
cdpCacheDeviceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpCacheDeviceId.setDescription("The Device-ID string as reported in the most recent CDP\nmessage.  The zero-length string indicates no Device-ID\nfield (TLV) was reported in the most recent CDP\nmessage.")
cdpCacheDevicePort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpCacheDevicePort.setDescription("The Port-ID string as reported in the most recent CDP\nmessage.  This will typically be the value of the ifName\nobject (e.g., 'Ethernet0').  The zero-length string\nindicates no Port-ID field (TLV) was reported in the\nmost recent CDP message.")
cdpCachePlatform = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpCachePlatform.setDescription("The Device's Hardware Platform as reported in the most\nrecent CDP message.  The zero-length string indicates\nthat no Platform field (TLV) was reported in the most\nrecent CDP message.")
cdpCacheCapabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpCacheCapabilities.setDescription("The Device's Functional Capabilities as reported in the\nmost recent CDP message.  For latest set of specific\nvalues, see the latest version of the CDP specification.\nThe zero-length string indicates no Capabilities field\n(TLV) was reported in the most recent CDP message.")
cdpCacheVTPMgmtDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpCacheVTPMgmtDomain.setDescription("The VTP Management Domain for the remote device's interface, \nas reported in the most recently received CDP message.\nThis object is not instantiated if no VTP Management Domain field\n(TLV) was reported in the most recently received CDP message.")
cdpCacheNativeVLAN = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 11), VlanIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpCacheNativeVLAN.setDescription("The remote device's interface's native VLAN, as reported in the \nmost recent CDP message.  The value 0 indicates\nno native VLAN field (TLV) was reported in the most\nrecent CDP message.")
cdpCacheDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 12), Integer().subtype(subtypeSpec=SingleValueConstraint(3,1,2,)).subtype(namedValues=NamedValues(("unknown", 1), ("halfduplex", 2), ("fullduplex", 3), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpCacheDuplex.setDescription("The remote device's interface's duplex mode, as reported in the \nmost recent CDP message.  The value unknown(1) indicates\nno duplex mode field (TLV) was reported in the most\nrecent CDP message.")
cdpCacheApplianceID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpCacheApplianceID.setDescription("The remote device's Appliance ID, as reported in the \nmost recent CDP message. This object is not instantiated if\nno Appliance VLAN-ID field (TLV) was reported in the most\nrecently received CDP message.")
cdpCacheVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 14), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpCacheVlanID.setDescription("The remote device's VoIP VLAN ID, as reported in the \nmost recent CDP message. This object is not instantiated if\nno Appliance VLAN-ID field (TLV) was reported in the most\nrecently received CDP message.")
cdpCachePowerConsumption = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpCachePowerConsumption.setDescription("The amount of power consumed by remote device, as reported\nin the most recent CDP message. This object is not instantiated\nif no Power Consumption field (TLV) was reported in the most\nrecently received CDP message.")
cdpCacheMTU = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpCacheMTU.setDescription("Indicates the size of the largest datagram that can be\nsent/received by remote device, as reported in the most recent\nCDP message. This object is not instantiated if no MTU field\n(TLV) was reported in the most recently received CDP message.")
cdpCacheSysName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 17), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpCacheSysName.setDescription("Indicates the value of the remote device's sysName MIB object.\nBy convention, it is the device's fully qualified domain name.\nThis object is not instantiated if no sysName field (TLV) was\nreported in the most recently received CDP message.")
cdpCacheSysObjectID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 18), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpCacheSysObjectID.setDescription("Indicates the value of the remote device's sysObjectID MIB\nobject. This object is not instantiated if no sysObjectID field\n(TLV) was reported in the most recently received CDP message.")
cdpCachePrimaryMgmtAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 19), CiscoNetworkProtocol()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpCachePrimaryMgmtAddrType.setDescription("An indication of the type of address contained in the\ncorresponding instance of cdpCachePrimaryMgmtAddress.")
cdpCachePrimaryMgmtAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 20), CiscoNetworkAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpCachePrimaryMgmtAddr.setDescription("This object indicates the (first) network layer\naddress at which the device will accept SNMP messages\nas reported in the first address in the \nManagement-Address TLV of the most recently received\nCDP message.  If the corresponding instance of \ncdpCachePrimaryMgmtAddrType has the value 'ip(1)',\nthen this object would be an IP-address. If the \nremote device is not currently manageable via any \nnetwork protocol, then it reports the special value \nof the IPv4 address 0.0.0.0, and that address is \nrecorded in this object.  If the most recently received\nCDP message did not contain the Management-Address\nTLV, then this object is not instanstiated.")
cdpCacheSecondaryMgmtAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 21), CiscoNetworkProtocol()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpCacheSecondaryMgmtAddrType.setDescription("An indication of the type of address contained in the\ncorresponding instance of cdpCacheSecondaryMgmtAddress.")
cdpCacheSecondaryMgmtAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 22), CiscoNetworkAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpCacheSecondaryMgmtAddr.setDescription("This object indicates the alternate network layer\naddress at which the device will accept SNMP messages\nas reported in the second address in the \nManagement-Address TLV of the most recently received\nCDP message.  If the corresponding instance of\ncdpCacheSecondaryMgmtAddrType has the value 'ip(1)',\nthen this object would be an IP-address. If the \nremote device reports the special value of the \nIPv4 address 0.0.0.0, that address is recorded in \nthis object.  If the most recently received CDP\nmessage did not contain the Management-Address\nTLV, or if that TLV contained only one address, then\nthis object is not instanstiated.")
cdpCachePhysLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 23), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpCachePhysLocation.setDescription("Indicates the physical location, as reported by the most recent\nCDP message, of a connector which is on, or physically connected\nto, the remote device's interface over which the CDP packet is\nsent. This object is not instantiated if no Physical Location\nfield (TLV) was reported by the most recently received CDP\nmessage.")
cdpCacheLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 24), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpCacheLastChange.setDescription("Indicates the time when this cache entry was last changed.\nThis object is initialised to the current time when the entry\ngets created and updated to the current time whenever the value\nof any (other) object instance in the corresponding row is\nmodified.")
cdpCtAddressTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 2))
if mibBuilder.loadTexts: cdpCtAddressTable.setDescription("The (conceptual) table containing the list of \nnetwork-layer addresses of a neighbor interface,\nas reported in the Address TLV of the most recently\nreceived CDP message. The first address included in\nthe Address TLV is saved in cdpCacheAddress.  This\ntable contains the remainder of the addresses in the\nAddress TLV.")
cdpCtAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 2, 1)).setIndexNames((0, "CISCO-CDP-MIB", "cdpCacheIfIndex"), (0, "CISCO-CDP-MIB", "cdpCacheDeviceIndex"), (0, "CISCO-CDP-MIB", "cdpCtAddressIndex"))
if mibBuilder.loadTexts: cdpCtAddressEntry.setDescription("An entry (conceptual row) in the cdpCtAddressTable,\ncontaining the information on one address received via CDP \non one interface from one device.  Entries appear \nwhen a CDP advertisement is received from a neighbor\ndevice, with an Address TLV.  Entries disappear when\nCDP is disabled on the interface, or globally. An entry \nor entries would also disappear if the most recently\nreceived CDP packet contain fewer address entries in the\nAddress TLV, than are currently present in the CDP cache.")
cdpCtAddressIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: cdpCtAddressIndex.setDescription("The index of the address entry for a given \ncdpCacheIfIndex,cdpCacheDeviceIndex pair. It\nhas the value N-1 for the N-th address in the\nAddress TLV")
cdpCtAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 2, 1, 4), CiscoNetworkProtocol()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpCtAddressType.setDescription("An indication of the type of address contained in the\ncorresponding instance of cdpCtAddress.")
cdpCtAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 2, 1, 5), CiscoNetworkAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpCtAddress.setDescription("The N-th network-layer address of the device as reported\nin the most recent CDP message's Address TLV, where N-1 is\ngiven by the value of cdpCtAddressIndex. For example, if\nthe the corresponding instance of cdpCtAddressType had the\nvalue 'ip(1)', then this object would be an IPv4-address.\nNOTE - The 1st address received in the Address TLV is\n       available using cdpCacheAddress")
cdpGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 3))
cdpGlobalRun = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 3, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdpGlobalRun.setDescription("An indication of whether the Cisco Discovery Protocol\nis currently running.  Entries in cdpCacheTable are\ndeleted when CDP is disabled.")
cdpGlobalMessageInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 254)).clone(60)).setMaxAccess("readwrite").setUnits("seconds")
if mibBuilder.loadTexts: cdpGlobalMessageInterval.setDescription("The interval at which CDP messages are to be generated.\nThe default value is 60 seconds.")
cdpGlobalHoldTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 255)).clone(180)).setMaxAccess("readwrite").setUnits("seconds")
if mibBuilder.loadTexts: cdpGlobalHoldTime.setDescription("The time for the receiving device holds CDP message.\nThe default value is 180 seconds.")
cdpGlobalDeviceId = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 3, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpGlobalDeviceId.setDescription("The device ID advertised by this device. The format of this\ndevice id is characterized by the value of \ncdpGlobalDeviceIdFormat object.")
cdpGlobalLastChange = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 3, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpGlobalLastChange.setDescription("Indicates the time when the cache table was last changed. It\nis the most recent time at which any row was last created,\nmodified or deleted.")
cdpGlobalDeviceIdFormatCpb = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 3, 6), Bits().subtype(namedValues=NamedValues(("serialNumber", 0), ("macAddress", 1), ("other", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpGlobalDeviceIdFormatCpb.setDescription("Indicate the Device-Id format capability of the device.\n\nserialNumber(0) indicates that the device supports using\nserial number as the format for its DeviceId.\n\nmacAddress(1) indicates that the device supports using\nlayer 2 MAC address as the format for its DeviceId.\n\nother(2) indicates that the device supports using its\nplatform specific format as the format for its DeviceId.")
cdpGlobalDeviceIdFormat = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 3, 7), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,3,)).subtype(namedValues=NamedValues(("serialNumber", 1), ("macAddress", 2), ("other", 3), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdpGlobalDeviceIdFormat.setDescription("An indication of the format of Device-Id contained in the\ncorresponding instance of cdpGlobalDeviceId. User can only\nspecify the formats that the device is capable of as\ndenoted in cdpGlobalDeviceIdFormatCpb object.\n\nserialNumber(1) indicates that the value of cdpGlobalDeviceId \nobject is in the form of an ASCII string contain the device\nserial number. \n\nmacAddress(2) indicates that the value of cdpGlobalDeviceId \nobject is in the form of Layer 2 MAC address.\n\nother(3) indicates that the value of cdpGlobalDeviceId object\nis in the form of a platform specific ASCII string contain\ninfo that identifies the device. For example: ASCII string\ncontains serialNumber appended/prepened with system name.")
ciscoCdpMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 23, 2))
ciscoCdpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 1))
ciscoCdpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 2))

# Augmentions

# Groups

ciscoCdpMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 2, 1)).setObjects(*(("CISCO-CDP-MIB", "cdpCacheCapabilities"), ("CISCO-CDP-MIB", "cdpCacheVersion"), ("CISCO-CDP-MIB", "cdpCachePlatform"), ("CISCO-CDP-MIB", "cdpCacheDevicePort"), ("CISCO-CDP-MIB", "cdpInterfaceEnable"), ("CISCO-CDP-MIB", "cdpInterfaceMessageInterval"), ("CISCO-CDP-MIB", "cdpCacheAddressType"), ("CISCO-CDP-MIB", "cdpCacheDeviceId"), ("CISCO-CDP-MIB", "cdpCacheAddress"), ) )
if mibBuilder.loadTexts: ciscoCdpMIBGroup.setDescription("A collection of objects for use with the Cisco\nDiscovery Protocol.")
ciscoCdpMIBGroupV11R01 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 2, 2)).setObjects(*(("CISCO-CDP-MIB", "cdpCacheCapabilities"), ("CISCO-CDP-MIB", "cdpInterfaceEnable"), ("CISCO-CDP-MIB", "cdpCacheDeviceId"), ("CISCO-CDP-MIB", "cdpCacheDevicePort"), ("CISCO-CDP-MIB", "cdpInterfacePort"), ("CISCO-CDP-MIB", "cdpInterfaceGroup"), ("CISCO-CDP-MIB", "cdpCacheAddressType"), ("CISCO-CDP-MIB", "cdpCacheVersion"), ("CISCO-CDP-MIB", "cdpCachePlatform"), ("CISCO-CDP-MIB", "cdpInterfaceMessageInterval"), ("CISCO-CDP-MIB", "cdpCacheAddress"), ) )
if mibBuilder.loadTexts: ciscoCdpMIBGroupV11R01.setDescription("A collection of objects for use with the Cisco\nDiscovery Protocol.")
ciscoCdpMIBGroupV11R02 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 2, 3)).setObjects(*(("CISCO-CDP-MIB", "cdpCacheCapabilities"), ("CISCO-CDP-MIB", "cdpInterfaceEnable"), ("CISCO-CDP-MIB", "cdpCacheDeviceId"), ("CISCO-CDP-MIB", "cdpCacheDevicePort"), ("CISCO-CDP-MIB", "cdpInterfacePort"), ("CISCO-CDP-MIB", "cdpInterfaceGroup"), ("CISCO-CDP-MIB", "cdpCacheAddressType"), ("CISCO-CDP-MIB", "cdpGlobalHoldTime"), ("CISCO-CDP-MIB", "cdpGlobalRun"), ("CISCO-CDP-MIB", "cdpCacheVersion"), ("CISCO-CDP-MIB", "cdpCachePlatform"), ("CISCO-CDP-MIB", "cdpGlobalMessageInterval"), ("CISCO-CDP-MIB", "cdpCacheAddress"), ) )
if mibBuilder.loadTexts: ciscoCdpMIBGroupV11R02.setDescription("A collection of objects for use with the Cisco\nDiscovery Protocol.")
ciscoCdpMIBGroupV12R02 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 2, 5)).setObjects(*(("CISCO-CDP-MIB", "cdpInterfaceGroup"), ("CISCO-CDP-MIB", "cdpCacheCapabilities"), ("CISCO-CDP-MIB", "cdpGlobalHoldTime"), ("CISCO-CDP-MIB", "cdpCachePlatform"), ("CISCO-CDP-MIB", "cdpInterfaceEnable"), ("CISCO-CDP-MIB", "cdpCacheAddressType"), ("CISCO-CDP-MIB", "cdpCacheDuplex"), ("CISCO-CDP-MIB", "cdpGlobalDeviceId"), ("CISCO-CDP-MIB", "cdpCacheVTPMgmtDomain"), ("CISCO-CDP-MIB", "cdpGlobalRun"), ("CISCO-CDP-MIB", "cdpCacheVersion"), ("CISCO-CDP-MIB", "cdpCacheDevicePort"), ("CISCO-CDP-MIB", "cdpCacheNativeVLAN"), ("CISCO-CDP-MIB", "cdpGlobalMessageInterval"), ("CISCO-CDP-MIB", "cdpInterfacePort"), ("CISCO-CDP-MIB", "cdpCacheDeviceId"), ("CISCO-CDP-MIB", "cdpCacheAddress"), ) )
if mibBuilder.loadTexts: ciscoCdpMIBGroupV12R02.setDescription("A collection of objects for use with the Cisco\nDiscovery Protocol.")
ciscoCdpV2MIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 2, 6)).setObjects(*(("CISCO-CDP-MIB", "cdpCacheSecondaryMgmtAddr"), ("CISCO-CDP-MIB", "cdpCacheLastChange"), ("CISCO-CDP-MIB", "cdpCachePrimaryMgmtAddr"), ("CISCO-CDP-MIB", "cdpGlobalLastChange"), ("CISCO-CDP-MIB", "cdpCachePrimaryMgmtAddrType"), ("CISCO-CDP-MIB", "cdpCacheVlanID"), ("CISCO-CDP-MIB", "cdpGlobalDeviceIdFormat"), ("CISCO-CDP-MIB", "cdpCacheSysName"), ("CISCO-CDP-MIB", "cdpGlobalDeviceIdFormatCpb"), ("CISCO-CDP-MIB", "cdpCacheMTU"), ("CISCO-CDP-MIB", "cdpCacheSysObjectID"), ("CISCO-CDP-MIB", "cdpCacheSecondaryMgmtAddrType"), ("CISCO-CDP-MIB", "cdpCacheApplianceID"), ("CISCO-CDP-MIB", "cdpCachePowerConsumption"), ("CISCO-CDP-MIB", "cdpCachePhysLocation"), ) )
if mibBuilder.loadTexts: ciscoCdpV2MIBGroup.setDescription("A collection of objects for use with the Cisco\nDiscovery Protocol version 2.")
ciscoCdpV2IfExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 2, 7)).setObjects(*(("CISCO-CDP-MIB", "cdpInterfaceExtendedTrust"), ("CISCO-CDP-MIB", "cdpInterfaceCosForUntrustedPort"), ) )
if mibBuilder.loadTexts: ciscoCdpV2IfExtGroup.setDescription("A collection of objects for use with the Cisco\nDiscovery Protocol version 2 to configure the value\nfor Extended Trust TLV and COS for Untrusted Port TLV.")
ciscoCdpCtAddressGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 2, 8)).setObjects(*(("CISCO-CDP-MIB", "cdpCtAddress"), ("CISCO-CDP-MIB", "cdpCtAddressType"), ) )
if mibBuilder.loadTexts: ciscoCdpCtAddressGroup.setDescription("A collection of objects for use with the Cisco\nDiscovery Protocol to obtain the addresses from\nthe Address TLV of a received CDP packet.")
ciscoCdpMIBGroupV12R03 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 2, 9)).setObjects(*(("CISCO-CDP-MIB", "cdpInterfaceGroup"), ("CISCO-CDP-MIB", "cdpInterfaceName"), ("CISCO-CDP-MIB", "cdpGlobalHoldTime"), ("CISCO-CDP-MIB", "cdpCacheCapabilities"), ("CISCO-CDP-MIB", "cdpCachePlatform"), ("CISCO-CDP-MIB", "cdpInterfaceEnable"), ("CISCO-CDP-MIB", "cdpCacheAddressType"), ("CISCO-CDP-MIB", "cdpCacheDuplex"), ("CISCO-CDP-MIB", "cdpGlobalDeviceId"), ("CISCO-CDP-MIB", "cdpCacheVTPMgmtDomain"), ("CISCO-CDP-MIB", "cdpGlobalRun"), ("CISCO-CDP-MIB", "cdpCacheVersion"), ("CISCO-CDP-MIB", "cdpCacheDevicePort"), ("CISCO-CDP-MIB", "cdpCacheNativeVLAN"), ("CISCO-CDP-MIB", "cdpGlobalMessageInterval"), ("CISCO-CDP-MIB", "cdpInterfacePort"), ("CISCO-CDP-MIB", "cdpCacheDeviceId"), ("CISCO-CDP-MIB", "cdpCacheAddress"), ) )
if mibBuilder.loadTexts: ciscoCdpMIBGroupV12R03.setDescription("A collection of objects for use with the Cisco\nDiscovery Protocol.")

# Compliances

ciscoCdpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 1, 1)).setObjects(*(("CISCO-CDP-MIB", "ciscoCdpMIBGroup"), ) )
if mibBuilder.loadTexts: ciscoCdpMIBCompliance.setDescription("The compliance statement for the CDP MIB.")
ciscoCdpMIBComplianceV11R01 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 1, 2)).setObjects(*(("CISCO-CDP-MIB", "ciscoCdpMIBGroupV11R01"), ) )
if mibBuilder.loadTexts: ciscoCdpMIBComplianceV11R01.setDescription("The compliance statement for the CDP MIB.")
ciscoCdpMIBComplianceV11R02 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 1, 3)).setObjects(*(("CISCO-CDP-MIB", "ciscoCdpMIBGroupV11R02"), ) )
if mibBuilder.loadTexts: ciscoCdpMIBComplianceV11R02.setDescription("The compliance statement for the CDP MIB.")
ciscoCdpMIBComplianceV12R02 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 1, 4)).setObjects(*(("CISCO-CDP-MIB", "ciscoCdpMIBGroupV12R02"), ) )
if mibBuilder.loadTexts: ciscoCdpMIBComplianceV12R02.setDescription("The compliance statement for the CDP MIB.")
ciscoCdpMIBCompliance5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 1, 5)).setObjects(*(("CISCO-CDP-MIB", "ciscoCdpMIBGroupV12R02"), ) )
if mibBuilder.loadTexts: ciscoCdpMIBCompliance5.setDescription("The compliance statement for the CDP MIB.")
ciscoCdpMIBComplianceV12R03 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 1, 6)).setObjects(*(("CISCO-CDP-MIB", "ciscoCdpMIBGroupV12R03"), ("CISCO-CDP-MIB", "ciscoCdpV2IfExtGroup"), ("CISCO-CDP-MIB", "ciscoCdpCtAddressGroup"), ("CISCO-CDP-MIB", "ciscoCdpV2MIBGroup"), ) )
if mibBuilder.loadTexts: ciscoCdpMIBComplianceV12R03.setDescription("The compliance statement for the CDP MIB.")

# Exports

# Module identity
mibBuilder.exportSymbols("CISCO-CDP-MIB", PYSNMP_MODULE_ID=ciscoCdpMIB)

# Objects
mibBuilder.exportSymbols("CISCO-CDP-MIB", ciscoCdpMIB=ciscoCdpMIB, ciscoCdpMIBObjects=ciscoCdpMIBObjects, cdpInterface=cdpInterface, cdpInterfaceTable=cdpInterfaceTable, cdpInterfaceEntry=cdpInterfaceEntry, cdpInterfaceIfIndex=cdpInterfaceIfIndex, cdpInterfaceEnable=cdpInterfaceEnable, cdpInterfaceMessageInterval=cdpInterfaceMessageInterval, cdpInterfaceGroup=cdpInterfaceGroup, cdpInterfacePort=cdpInterfacePort, cdpInterfaceName=cdpInterfaceName, cdpInterfaceExtTable=cdpInterfaceExtTable, cdpInterfaceExtEntry=cdpInterfaceExtEntry, cdpInterfaceExtendedTrust=cdpInterfaceExtendedTrust, cdpInterfaceCosForUntrustedPort=cdpInterfaceCosForUntrustedPort, cdpCache=cdpCache, cdpCacheTable=cdpCacheTable, cdpCacheEntry=cdpCacheEntry, cdpCacheIfIndex=cdpCacheIfIndex, cdpCacheDeviceIndex=cdpCacheDeviceIndex, cdpCacheAddressType=cdpCacheAddressType, cdpCacheAddress=cdpCacheAddress, cdpCacheVersion=cdpCacheVersion, cdpCacheDeviceId=cdpCacheDeviceId, cdpCacheDevicePort=cdpCacheDevicePort, cdpCachePlatform=cdpCachePlatform, cdpCacheCapabilities=cdpCacheCapabilities, cdpCacheVTPMgmtDomain=cdpCacheVTPMgmtDomain, cdpCacheNativeVLAN=cdpCacheNativeVLAN, cdpCacheDuplex=cdpCacheDuplex, cdpCacheApplianceID=cdpCacheApplianceID, cdpCacheVlanID=cdpCacheVlanID, cdpCachePowerConsumption=cdpCachePowerConsumption, cdpCacheMTU=cdpCacheMTU, cdpCacheSysName=cdpCacheSysName, cdpCacheSysObjectID=cdpCacheSysObjectID, cdpCachePrimaryMgmtAddrType=cdpCachePrimaryMgmtAddrType, cdpCachePrimaryMgmtAddr=cdpCachePrimaryMgmtAddr, cdpCacheSecondaryMgmtAddrType=cdpCacheSecondaryMgmtAddrType, cdpCacheSecondaryMgmtAddr=cdpCacheSecondaryMgmtAddr, cdpCachePhysLocation=cdpCachePhysLocation, cdpCacheLastChange=cdpCacheLastChange, cdpCtAddressTable=cdpCtAddressTable, cdpCtAddressEntry=cdpCtAddressEntry, cdpCtAddressIndex=cdpCtAddressIndex, cdpCtAddressType=cdpCtAddressType, cdpCtAddress=cdpCtAddress, cdpGlobal=cdpGlobal, cdpGlobalRun=cdpGlobalRun, cdpGlobalMessageInterval=cdpGlobalMessageInterval, cdpGlobalHoldTime=cdpGlobalHoldTime, cdpGlobalDeviceId=cdpGlobalDeviceId, cdpGlobalLastChange=cdpGlobalLastChange, cdpGlobalDeviceIdFormatCpb=cdpGlobalDeviceIdFormatCpb, cdpGlobalDeviceIdFormat=cdpGlobalDeviceIdFormat, ciscoCdpMIBConformance=ciscoCdpMIBConformance, ciscoCdpMIBCompliances=ciscoCdpMIBCompliances, ciscoCdpMIBGroups=ciscoCdpMIBGroups)

# Groups
mibBuilder.exportSymbols("CISCO-CDP-MIB", ciscoCdpMIBGroup=ciscoCdpMIBGroup, ciscoCdpMIBGroupV11R01=ciscoCdpMIBGroupV11R01, ciscoCdpMIBGroupV11R02=ciscoCdpMIBGroupV11R02, ciscoCdpMIBGroupV12R02=ciscoCdpMIBGroupV12R02, ciscoCdpV2MIBGroup=ciscoCdpV2MIBGroup, ciscoCdpV2IfExtGroup=ciscoCdpV2IfExtGroup, ciscoCdpCtAddressGroup=ciscoCdpCtAddressGroup, ciscoCdpMIBGroupV12R03=ciscoCdpMIBGroupV12R03)

# Compliances
mibBuilder.exportSymbols("CISCO-CDP-MIB", ciscoCdpMIBCompliance=ciscoCdpMIBCompliance, ciscoCdpMIBComplianceV11R01=ciscoCdpMIBComplianceV11R01, ciscoCdpMIBComplianceV11R02=ciscoCdpMIBComplianceV11R02, ciscoCdpMIBComplianceV12R02=ciscoCdpMIBComplianceV12R02, ciscoCdpMIBCompliance5=ciscoCdpMIBCompliance5, ciscoCdpMIBComplianceV12R03=ciscoCdpMIBComplianceV12R03)
