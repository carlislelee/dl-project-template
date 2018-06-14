import json
import logging
import logging.handlers


class ServerLogger(object):

    def __init__(self, logger_name, logger_file, logger_level=logging.DEBUG):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logger_level)

        formatter = logging.Formatter('%(asctime)s\t[%(levelname)s]\t%(message)s', '%Y-%m-%d %H:%M:%S')
        # log file conf
        if not logger_file:
            raise Exception('logger_file must be given')
        self._handler = logging.handlers.TimedRotatingFileHandler(logger_file, when='D', interval=1, backupCount=365)
        self._handler.setFormatter(formatter)
        self._handler.setLevel(logger_level)
        self.logger.addHandler(self._handler)
        # console print conf
        self._console = logging.StreamHandler()
        self._console.setFormatter(formatter)
        self._console.setLevel(logger_level)
        logging.getLogger('').addHandler(self._console)

    def get_logger(self):
        return self.logger

    def debug(self, string):
        self.logger.debug(string)

    def info(self, string):
        self.logger.info(string)

    def warn(self, string):
        self.logger.warn(string)

    def error(self, string):
        self.logger.error(string)

    def critical(self, string):
        self.logger.critical(string)

    def server_logging(self, interface, remote_addr, method, info, response_time):
        if method == 'POST':
            info_dict = dict()
            for k in info:
                info_dict[k] = info[k]
            message = '[%s][POST] ' % remote_addr + json.dumps(info_dict, ensure_ascii=False)
        else:
            message = '[ERROR] Error Request Type'
        self.logger.info('%s\t%s\t%s' % (interface, response_time, message))

    def destroy(self):
        self.logger.removeHandler(self._handler)
        self.logger.removeHandler(self._console)


if __name__ == '__main__':
    logger = ServerLogger('embedding_server', 'logs/faiss_server.log', logging.DEBUG)
    logger.debug('debuggggggggggg')
    logger.info('Log Testing')
    logger.warn('Log Warn')
    logger.error('ERROR!')
