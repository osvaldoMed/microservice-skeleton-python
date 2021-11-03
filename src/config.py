import os
from dataclasses import dataclass
from enum import Enum
from dotenv import load_dotenv

load_dotenv() # will look for the .env file in the current working directory or any parent directories

class Environment(Enum):
    """Environment is an enumeration of the differents environments
    that the application can be deployed to"""

    PROD = 'production'
    DEV = 'development'
    TEST = 'test'

# set environment, default to development
try: 
    ENVIRONMENT = Environment(os.getenv('ENVIRONMENT'))
except:
    ENVIRONMENT = Environment.DEV


class _Config(object):
    """Base config"""
    ENVIRONMENT = ENVIRONMENT.value
    TESTING = False
    APP_NAME = os.getenv('APP_NAME')

class ProductionConfig(_Config):
    """Production config, uses production database"""
    DB_SERVER = 'localhost'

class DevelopmentConfig(_Config):
    """development config, uses ..."""
    DB_SERVER = 'localhost'
    DEBUG = True
    
class TestingConfig(_Config):
    """Testing config, uses ...."""
    DB_SERVER = 'localhost'
    TESTING = True


# set Config object for import from main app, default to development config.
if ENVIRONMENT == Environment.PROD:
    Config = ProductionConfig()
elif ENVIRONMENT == Environment.DEV:
    Config = DevelopmentConfig()
elif ENVIRONMENT == Environment.TEST:
    Config = TestingConfig()
else:
    Config = DevelopmentConfig()

if __name__ == '__main__':
    print(f'Config: {Config}')


