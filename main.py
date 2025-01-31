from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig
from networksecurity.entity.config_entity import  TrainingPipeLineConfig
from networksecurity.components.data_transformation import DataTransformation 

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
        data_transformation_config = DataTransformationConfig(trainingpipelineconfig)
        logging.info("Data Transformation started")
        data_transformation = DataTransformation(data_validation_artifact, data_transformation_config)
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("Data Transformation Completed")

        logging.info("Model Training started")
        model_trainer_config = ModelTrainerConfig(trainingpipelineconfig)
        model_trainer = ModelTrainer(model_trainer_config=model_trainer_config, 
                                     data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact = model_trainer.initiate_model_trainer()
        logging.info("Model Training artifact created")

    
    except Exception as e:
        raise NetworkSecurityException(e,sys)