from src.wind_prediction.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.wind_prediction.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.wind_prediction.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.wind_prediction.pipeline.stage_04_model_trainer import ModelTrainerPipeline
from src.wind_prediction.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline
from src.wind_prediction import logger



stage_name = "Data Ingestion stage"

try:
        logger.info(f"******{stage_name} started******")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"******{stage_name} completed******")
    
except Exception as e:
        logger.info(e)


stage_name = "Data Validation stage"

try:
        logger.info(f"******{stage_name} started******")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f"******{stage_name} completed******")
    
except Exception as e:
        logger.info(e)


stage_name = "Data Transformation stage"

try:
        logger.info(f"******{stage_name} started******")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f"******{stage_name} completed******")
    
except Exception as e:
        logger.info(e)

stage_name = "Model Trainer stage"

try:
        logger.info(f"******{stage_name} started******")
        obj = ModelTrainerPipeline()
        obj.main()
        logger.info(f"******{stage_name} completed******")
    
except Exception as e:
        logger.info(e)


stage_name = "Model Evaluation stage"

try:
        logger.info(f"******{stage_name} started******")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f"******{stage_name} completed******")
    
except Exception as e:
        logger.info(e)
