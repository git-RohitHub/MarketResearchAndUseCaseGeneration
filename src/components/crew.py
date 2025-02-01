from src.components.agents import AgentCollections
from src.components.tasks import TaskCollection
from src.constants import *
from src.utils import MainUtils
from crewai import Crew
from crewai import Process
from src.exception import CustomException
from src.logger import logger
import os 
import sys

class CreateCrew:
    def __init__(self,company_name):
        self.agents = AgentCollections()
        self.tasks = TaskCollection()
        self.utils = MainUtils()
        self.CompanyAnalysisTask,self.UseCaseAdvisorTask,self.FeasibilityCheckerTask,self.ResourceAssetCollectionTask = self.tasks.getTasks(company_name)
        self.CompanyAnalystAgent,self.UseCaseAdvisorAgent,self.FeasibilityCheckerAgent,self.ResourceAssetCollectionAgent =  self.agents.getAgents()  

    def getCrew(self):
        logger.info(":) LOADING CREW :) ")
        try:
            crew = Crew(
                agents = [self.CompanyAnalystAgent,self.UseCaseAdvisorAgent,self.FeasibilityCheckerAgent,self.ResourceAssetCollectionAgent],
                tasks = [self.CompanyAnalysisTask,self.UseCaseAdvisorTask,self.FeasibilityCheckerTask,self.ResourceAssetCollectionTask],
                process = Process.hierarchical,
                manager_llm = self.utils.load_llm(model=model_name,temperature=temperature),
                memory = True
            )
            return crew
        except Exception as e:
            raise CustomException(e,sys)


