import sys
from us_visa.exception import USvisaException
from us_visa.pipline.training_pipeline import TrainPipeline
try:
    pipeline = TrainPipeline()
    pipeline.run_pipeline(ddd)
except Exception as e:
    raise USvisaException(e,sys)
