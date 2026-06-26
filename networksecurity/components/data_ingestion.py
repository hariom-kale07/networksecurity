from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
##configurtion for the 

from networksecurity.entity.config_entity import DataIngestionConfig

import os
import pymongo
import numpy as np
import sys
from typing import List
from sklearn.model_selection import train_test_split
from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")