'''
    This script will run everything required to generate a working model for the project. This includes data extraction,
    data transformation, feature generation, model training, and model testing
'''
from src.data import pull
from src.data import clean
from src.data import featurize
from src.models import train
from src.models import test
from src.models import predict

import ConfigParser
config = ConfigParser.ConfigParser()
config.read("config.txt")
azure_key = config.get("Azure","key1")