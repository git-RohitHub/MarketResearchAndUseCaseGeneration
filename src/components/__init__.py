from src.components.crew import CreateCrew
from src.exception import CustomException
from src.logger import logger
import sys


def crewKickoff(inputs,company_name):
     try:
          logger.info(":) Crew Kickoff Successfully :) ")
          crew = CreateCrew(company_name)
          crew_usecase = crew.getCrew()
          result = crew_usecase.kickoff(inputs = inputs)
          return result
     except Exception as e:
          raise CustomException(e,sys)
