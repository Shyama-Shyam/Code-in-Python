"""
Logging in programming refers to the process of recording information about 
the execution of a program, usually for debugging, monitoring, or auditing purposes. 
The logging module in Python provides a flexible and standardized way to incorporate
 logging into your applications. Here's an overview of the key concepts and components 
 related to logging in Python:

Key Components:
Logging Levels:

Logging supports different levels, indicating the severity of messages. 
Common levels, in increasing order of severity, are DEBUG, INFO, WARNING, ERROR, and CRITICAL.
Messages at or above a specified level will be included in the log output.
Loggers:

A logger is an object responsible for emitting log messages.
Loggers are organized hierarchically based on their names, forming a tree-like structure. Each logger inherits settings from its ancestors.
Handlers:

Handlers determine where log messages are sent. Examples include writing to a
 file, printing to the console, or sending messages to a network socket.
Loggers can have multiple handlers, allowing messages to be processed in different ways simultaneously.
Formatters:

Formatters specify the layout of log records, including the content and structure of the log messages.
Formatters are associated with handlers, defining how messages are presented in the output.
"""
import logging

logging.basicConfig(level=logging.INFO) #id we dont write this line then default root logger will be used of security level at WARNING

logging.info("20 users online")
logging.critical('system crash')

print('next-example'.center(40, '-'))
#creating logger
logger = logging.getLogger("my logger")
logger.setLevel(logging.DEBUG)

#create handler
handler = logging.FileHandler('Advanced\log_file.log')
handler.setLevel(logging.INFO)
logger.addHandler(handler)

formatter = logging.Formatter("%(levelname)s - %(asctime)s : %(message)s")
handler.setFormatter(formatter)
#logger is set to debug but handler is set to info 

logger.debug("x is 30")
logger.info("20 users online")
logger.warning("server is overloaded")
logger.error("some users crashed")
logger.critical('system crash')
