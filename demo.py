import sys
from us_visa.exception import USvisaException
from us_visa.pipline.training_pipeline import TrainPipeline


try:
    pipeline = TrainPipeline()
    pipeline.run_pipeline()
except Exception as e:
    print(USvisaException(e,sys))



