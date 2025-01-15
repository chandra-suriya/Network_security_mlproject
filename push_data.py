import os
import sys
import json
import certifi
import pandas as pd
import numpy as np
import pymongo
import pymongo.mongo_client
from pymongo.errors import ConnectionFailure
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

ca = certifi.where()


class NetWorkDataExtract():
    def __init__(self):
        try:
            pass

        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def csv_to_json_converter(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True) # reseting the index
            records = list(json.loads(data.T. to_json()).values()) # converting the table data into json values
            return records
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def insert_data_mongodb(self, records, database, collection):
        try:
            self.records = records
            self.database = database
            self.collection = collection
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL, tls=True, tlsAllowInvalidCertificates=True)
            self.database = self.mongo_client[self.database]

            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return len(self.records)

        except ConnectionFailure as e:
            raise NetworkSecurityException(f"Could not connect to MongoDB: {e}", sys)
        except Exception as e:
            raise NetworkSecurityException(e, sys)


if __name__ == '__main__':
    FILE_PATH = "Network_Data\phisingData.csv"
    DATABASE = "CHAN_DB"
    COLLECTION = "NetworkData"
    networkobj = NetWorkDataExtract()
    DATA_RECORD = networkobj.csv_to_json_converter(file_path=FILE_PATH)
    #print(DATA_RECORD)
    no_of_records = networkobj.insert_data_mongodb(DATA_RECORD,DATABASE,COLLECTION)
    print(no_of_records)