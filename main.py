from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import  TrainingPipeLineConfig

import sys

if __name__ == "__main__":
    try:
        trainingpipelineconfig = TrainingPipeLineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        dataIngestion =  DataIngestion(dataingestionconfig)
        logging.info("initiated the  data ingestion")
        dataIngestionartifact = dataIngestion.initiate_data_ingestion()
        print(dataIngestionartifact)
    
    except Exception as e:
        raise NetworkSecurityException(e,sys)