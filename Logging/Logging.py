# %% [markdown]
# # Module: Logging Assignments
# ## Lesson: Logging
# ### Assignment 1: Basic Logging
# 
# 1. Write a Python function to create a basic logger that logs messages to a file named `app.log`.

# %%
import logging

def basic_logger():
    logging.basicConfig(filename='app.log', level=logging.DEBUG)
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')

# Test the function
basic_logger()

# %% [markdown]
# 2. Modify the function to log messages of levels: DEBUG, INFO, WARNING, ERROR, and CRITICAL.

# %%
# The modification is already included in the above function.

# %% [markdown]
# ### Assignment 2: Logging with Different Handlers
# 
# 1. Write a Python function to create a logger that logs messages to both a file named `app.log` and the console.

# %%
def logger_with_handlers():
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)
    
    file_handler = logging.FileHandler('app.log')
    console_handler = logging.StreamHandler()
    
    file_handler.setLevel(logging.DEBUG)
    console_handler.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')

# Test the function
logger_with_handlers()

# %% [markdown]
# 2. Modify the function to use different logging levels for the file and console handlers.

# %%
# The modification is already included in the above function.

# %% [markdown]
# ### Assignment 3: Formatting Log Messages
# 
# 1. Write a Python function to create a logger with a custom log message format that includes the timestamp, logging level, and message.

# %%
def logger_with_custom_format():
    logger = logging.getLogger('custom_logger')
    logger.setLevel(logging.DEBUG)
    
    file_handler = logging.FileHandler('custom_app.log')
    console_handler = logging.StreamHandler()
    
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')

# Test the function
logger_with_custom_format()

# %% [markdown]
# 2. Modify the function to use different formats for the file and console handlers.

# %%
def logger_with_different_formats():
    logger = logging.getLogger('multi_format_logger')
    logger.setLevel(logging.DEBUG)
    
    file_handler = logging.FileHandler('multi_format_app.log')
    console_handler = logging.StreamHandler()
    
    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)
    console_handler.setFormatter(console_formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')

# Test the function
logger_with_different_formats()

# %% [markdown]
# ### Assignment 4: Rotating Log Files
# 
# 1. Write a Python function to create a logger that uses a rotating file handler, which creates a new log file when the current log file reaches a certain size.

# %%
from logging.handlers import RotatingFileHandler

def logger_with_rotating_file_handler():
    logger = logging.getLogger('rotating_logger')
    logger.setLevel(logging.DEBUG)
    
    rotating_handler = RotatingFileHandler('rotating_app.log', maxBytes=2000, backupCount=5)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    rotating_handler.setFormatter(formatter)
    
    logger.addHandler(rotating_handler)
    
    for i in range(100):
        logger.debug('This is debug message number {}'.format(i))

# Test the function
logger_with_rotating_file_handler()

# %% [markdown]
# 2. Modify the function to keep a specified number of backup log files.

# %%
# The modification is already included in the above function with backupCount=5.

# %% [markdown]
# ### Assignment 5: Logging Exceptions
# 
# 1. Write a Python function that logs an exception stack trace to a log file when an exception occurs.

# %%
def log_exception():
    logger = logging.getLogger('exception_logger')
    logger.setLevel(logging.ERROR)
    
    file_handler = logging.FileHandler('exception_app.log')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    
    try:
        1 / 0
    except Exception as e:
        logger.exception("An exception occurred")

# Test the function
log_exception()

# %% [markdown]
# 2. Modify the function to log the stack trace at the ERROR level.

# %%
# The modification is already included in the above function.

# %% [markdown]
# ### Assignment 6: Contextual Logging
# 
# 1. Write a Python function to create a logger that includes contextual information (e.g., function name, line number) in the log messages.

# %%
def logger_with_context():
    logger = logging.getLogger('context_logger')
    logger.setLevel(logging.DEBUG)
    
    file_handler = logging.FileHandler('context_app.log')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(funcName)s - %(lineno)d')
    file_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    
    def test_func():
        logger.debug('This is a debug message')
        logger.info('This is an info message')
        logger.warning('This is a warning message')
        logger.error('This is an error message')
        logger.critical('This is a critical message')
    
    test_func()

# Test the function
logger_with_context()

# %% [markdown]
# 2. Modify the function to include additional contextual information (e.g., user ID, session ID).

# %%
def logger_with_additional_context(user_id, session_id):
    logger = logging.getLogger('additional_context_logger')
    logger.setLevel(logging.DEBUG)
    
    file_handler = logging.FileHandler('additional_context_app.log')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(funcName)s - %(lineno)d - UserID: %(user_id)s - SessionID: %(session_id)s')
    file_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    
    extra = {'user_id': user_id, 'session_id': session_id}
    
    def test_func():
        logger.debug('This is a debug message', extra=extra)
        logger.info('This is an info message', extra=extra)
        logger.warning('This is a warning message', extra=extra)
        logger.error('This is an error message', extra=extra)
        logger.critical('This is a critical message', extra=extra)
    
    test_func()

# Test the function
logger_with_additional_context('user123', 'session456')

# %% [markdown]
# ### Assignment 7: Configuring Logging with a Dictionary
# 
# 1. Write a Python function to configure logging using a dictionary. The configuration should include handlers for both file and console logging.

# %%
import logging.config

def configure_logging_with_dict():
    log_config = {
        'version': 1,
        'formatters': {
            'default': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            },
            'detailed': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(funcName)s - %(lineno)d'
            }
        },
        'handlers': {
            'file': {
                'class': 'logging.FileHandler',
                'filename': 'dict_config_app.log',
                'formatter': 'detailed',
                'level': 'DEBUG'
            },
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'default',
                'level': 'DEBUG'
            }
        },
        'root': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG'
        }
    }
    logging.config.dictConfig(log_config)
    logger = logging.getLogger('')
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')

# Test the function
configure_logging_with_dict()

# %% [markdown]
# 2. Modify the dictionary to include different logging levels and formats for each handler.

# %%
# The modification is already included in the above function.

# %% [markdown]
# ### Assignment 8: Logging in a Multi-Module Application
# 
# 1. Write a Python script that sets up logging for a multi-module application. Each module should have its own logger.

# %% [markdown]
# #### File: `main.py`

# %%
import logging
from module_a import module_a_function
from module_b import module_b_function

def setup_logging():
    log_config = {
        'version': 1,
        'formatters': {
            'default': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            }
        },
        'handlers': {
            'file': {
                'class': 'logging.FileHandler',
                'filename': 'multi_module_app.log',
                'formatter': 'default',
                'level': 'DEBUG'
            },
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'default',
                'level': 'DEBUG'
            }
        },
        'root': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG'
        }
    }
    logging.config.dictConfig(log_config)

# Main script
if __name__ == '__main__':
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Main module started')
    module_a_function()
    module_b_function()
    logger.info('Main module finished')

# %% [markdown]
# #### File: `module_a.py`

# %%
import logging

def module_a_function():
    logger = logging.getLogger(__name__)
    logger.info('Module A function started')
    logger.debug('This is a debug message from Module A')
    logger.info('Module A function finished')

# %% [markdown]
# #### File: `module_b.py`

# %%
import logging

def module_b_function():
    logger = logging.getLogger(__name__)
    logger.info('Module B function started')
    logger.debug('This is a debug message from Module B')
    logger.info('Module B function finished')

# %% [markdown]
# 2. Modify the script to propagate log messages from each module's logger to a root logger that handles logging to a file.

# %% [markdown]
# ### Assignment 9: Logging Performance
# 
# 1. Write a Python script to benchmark the performance of logging with different handlers (e.g., file handler, console handler, rotating file handler).

# %%
import logging
import time
from logging.handlers import RotatingFileHandler

def benchmark_logging_performance():
    logger = logging.getLogger('performance_logger')
    logger.setLevel(logging.DEBUG)

    # File handler
    file_handler = logging.FileHandler('performance_file.log')
    file_handler.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)

    start_time = time.time()
    for i in range(10000):
        logger.debug('This is a debug message')
    end_time = time.time()
    print('File handler logging time: {} seconds'.format(end_time - start_time))
    logger.removeHandler(file_handler)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    logger.addHandler(console_handler)

    start_time = time.time()
    for i in range(10000):
        logger.debug('This is a debug message')
    end_time = time.time()
    print('Console handler logging time: {} seconds'.format(end_time - start_time))
    logger.removeHandler(console_handler)

    # Rotating file handler
    rotating_handler = RotatingFileHandler('performance_rotating.log', maxBytes=2000, backupCount=5)
    rotating_handler.setLevel(logging.DEBUG)
    logger.addHandler(rotating_handler)

    start_time = time.time()
    for i in range(10000):
        logger.debug('This is a debug message')
    end_time = time.time()
    print('Rotating file handler logging time: {} seconds'.format(end_time - start_time))
    logger.removeHandler(rotating_handler)

# Test the function
benchmark_logging_performance()

# %% [markdown]
# 2. Modify the script to compare the performance of logging with and without message formatting.

# %%
def benchmark_logging_formatting_performance():
    logger = logging.getLogger('formatting_performance_logger')
    logger.setLevel(logging.DEBUG)

    # File handler without formatting
    file_handler = logging.FileHandler('performance_no_format.log')
    file_handler.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)

    start_time = time.time()
    for i in range(10000):
        logger.debug('This is a debug message')
    end_time = time.time()
    print('File handler logging time without formatting: {} seconds'.format(end_time - start_time))
    logger.removeHandler(file_handler)

    # File handler with formatting
    file_handler = logging.FileHandler('performance_with_format.log')
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    start_time = time.time()
    for i in range(10000):
        logger.debug('This is a debug message')
    end_time = time.time()
    print('File handler logging time with formatting: {} seconds'.format(end_time - start_time))
    logger.removeHandler(file_handler)

# Test the function
benchmark_logging_formatting_performance()

# %% [markdown]
# ### Assignment 10: Advanced Logging Configuration
# 
# 1. Write a Python function to configure logging using an external configuration file (e.g., `logging.conf`). The configuration should include handlers for file and console logging.

# %% [markdown]
# #### File: `logging.conf`

# %%
[loggers]
keys=root

[handlers]
keys=fileHandler,consoleHandler

[formatters]
keys=defaultFormatter

[logger_root]
level=DEBUG
handlers=fileHandler,consoleHandler

[handler_fileHandler]
class=FileHandler
level=DEBUG
formatter=defaultFormatter
args=('advanced_logging_app.log', 'a')

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=defaultFormatter
args=(sys.stdout,)

[formatter_defaultFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s

# %% [markdown]
# #### File: `main.py`

# %%
import logging.config

def setup_logging_from_file():
    logging.config.fileConfig('logging.conf')
    logger = logging.getLogger(__name__)
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')

# Test the function
setup_logging_from_file()

# %% [markdown]
# 2. Modify the configuration file to use different logging levels and formats for each handler.


