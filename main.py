from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig
from networksecurity.entity.config_entity import  TrainingPipeLineConfig

import sys

if __name__ == "__main__":
    try:
        trainingpipelineconfig = TrainingPipeLineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        dataIngestion =  DataIngestion(dataingestionconfig)
        logging.info("initiated the  data ingestion")
        dataIngestionartifact = dataIngestion.initiate_data_ingestion()
        logging.info("Data Ingestion Completed")
        print(dataIngestionartifact)
        data_validation_config = DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(dataIngestionartifact, data_validation_config)
        logging.info("Intitate the data validation")
        data_validation_artifact = data_validation.initate_data_validation()
        logging.info("Data validation Completed")
        print(data_validation_artifact)
        
    
    except Exception as e:
        raise NetworkSecurityException(e,sys)