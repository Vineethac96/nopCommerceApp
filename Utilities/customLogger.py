'''What is Logging?
Logging is a process that takes applications to a newer level with information logs on how the applications may or may not have performed/executed.
It gives an exact idea of software performance, including any shortcomings.
Logger Class – To fully use the logger, create an instance for a logger class where all the generic methods will be at the user’s disposal, required to use Log4j.
Log Levels – These are the methods that will be used to print the log messages. There are primarily only a few log levels that are used in a script.
ALL – This level will prioritize and include everything in the logs.
ERROR – This level will show messages that inform users about error events that may not stop the application.
WARN – This level will show information regarding warnings, that may not stop the execution but may still cause problems.
DEBUG – This level will log debugging information.
INFO – This level will log the progress of the application.'''


import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="C:/Users/Vineetha c/PycharmProjects/PYTEST_PROJECT/Logs",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

