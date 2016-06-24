from cloudshell.cli.command_template.command_template import CommandTemplate

SAVE_CONFIGURATION_DATATYPE = CommandTemplate('transfer upload datatype {0}', [r'.+'],
                                              ['Wrong configuration type'])
SAVE_CONFIGURATION_MODE = CommandTemplate('transfer upload mode {0}', [r'.+'],
                                          ['Wrong upload mode'])
SAVE_CONFIGURATION_SERVERIP = CommandTemplate('transfer upload serverip {0}', [r'.+'],
                                              ['Wrong upload serverip'])
SAVE_CONFIGURATION_PORT = CommandTemplate('transfer upload port {0}', [r'.+'],
                                          ['Wrong upload port'])
SAVE_CONFIGURATION_PATH = CommandTemplate('transfer upload path {0}', [r'.+'],
                                          ['Wrong upload path'])
SAVE_CONFIGURATION_FILENAME = CommandTemplate('transfer upload filename {0}', [r'.+'],
                                              ['Wrong upload filename'])
SAVE_CONFIGURATION_START = CommandTemplate('transfer upload start')
