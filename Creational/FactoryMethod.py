# http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Factory.html
from enum import Enum


class LoggingProviders(Enum):
    Enterprise = 1
    Log4Net = 2


# Logger Interface
class Logger:
    def log_message(self, message):
        pass

    def log_error(self):
        pass

    def log_verbose_information(self):
        pass


# Concrete Logger
class EnterpriseLogger(Logger):
    def log_message(self, message):
        print("{0} : {1}".format("Enterprise", message))

    def log_error(self):
        raise NotImplementedError()

    def log_verbose_information(self):
        raise NotImplementedError()


# Concrete Logger
class Log4NetLogger(Logger):
    def log_message(self, message):
        print("{0} : {1}".format("Log4Net ", message))

    def log_error(self):
        raise NotImplementedError()

    def log_verbose_information(self):
        raise NotImplementedError()


# Provider
class LoggerProviderFactory:
    def get_loggin_provider(self, logging_provider):
        if logging_provider == LoggingProviders.Enterprise:
            return EnterpriseLogger()
        elif logging_provider == LoggingProviders.Log4Net:
            return Log4NetLogger()
        else:
            return EnterpriseLogger()


if __name__ == '__main__':
    provider = LoggingProviders.Enterprise
    logger = LoggerProviderFactory().get_loggin_provider(provider)
    logger.log_message("Hello World")

    provider = LoggingProviders.Log4Net
    logger = LoggerProviderFactory().get_loggin_provider(provider)
    logger.log_message("Hello World")
