

import logging
class Log:
    logging.basicConfig(level=logging.DEBUG)

    @staticmethod
    def debug(debug):
        print(debug)
        # logging.debug(debug)

    @staticmethod
    def info(info):
        print(info)
        # logging.info(info)