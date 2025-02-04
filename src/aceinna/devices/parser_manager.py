from .parsers.rtk330l_message_parser import UartMessageParser as Rtk330lUartMessageParser
from .parsers.beidou_message_parser import UartMessageParser as beidouUartMessageParser
from .parsers.ins401_message_parser import EthernetMessageParser as INS401EthernetMessageParser

class ParserManager:
    '''
    Manage Parser
    '''
    device_list = []

    # TODO: communicator_type should be used to generate the parser
    @staticmethod
    def build(device_type, communicator_type, properties):  # pylint:disable=unused-argument
        '''
        Generate matched parser
        '''
        if device_type == 'INS401' or device_type == 'INS402':
            return INS401EthernetMessageParser(properties)
        elif device_type == 'beidou':
            return beidouUartMessageParser(properties)
        else:
            return Rtk330lUartMessageParser(properties)
