from crewai import Task
from src.utils import MainUtils
from src.utils import CompanyDetails
from src.components.agents import AgentCollections
from dataclasses import dataclass
from src.constants import *
from src.logger import logger
from src.exception import CustomException
import sys
import os


@dataclass
class TaskConfig:
    yaml_file_path = os.path.join(config_folder,yaml_file_path)
    company_task_output = os.path.join(reports_folder,company_analyst_output)
    user_advisor_output = os.path.join(reports_folder,usecase_advisor_output)
    feasiblity_checker_output = os.path.join(reports_folder,feasiblity_checker_output)
    resource_allocator_output = os.path.join(reports_folder,resource_allocator_output)


class TaskCollection:
    def __init__(self):
        self.utils = MainUtils()
        self.taskconfig = TaskConfig()
        self.agent = AgentCollections()
        self.CompanyAnalystAgent,self.UseCaseAdvisorAgent,self.FeasibilityCheckerAgent,self.ResourceAssetCollectionAgent  = self.agent.getAgents()
        
    def task_description(self,taskname:str,data:str="description"):
        return self.utils.extracting_tasks(taskname=taskname,filepath=self.taskconfig.yaml_file_path,data=data)
    
    def task_expected_output(self,taskname:str,data:str="description"):
        return self.utils.extracting_tasks(taskname=taskname,filepath=self.taskconfig.yaml_file_path,data=data)

    def getTasks(self,company_name):
        logger.info(":) LOADING TASK :) ")  
        try:
            CompanyAnalysisTask = Task(
            description = self.task_description(COMPANY_ANALYST_TASK),
            expected_output=self.task_expected_output(COMPANY_ANALYST_TASK),
            output_json = CompanyDetails,
            output_file=os.path.join(company_name,self.taskconfig.company_task_output+json_extension),
            agent = self.CompanyAnalystAgent
            )
            UseCaseAdvisorTask = Task(
            description = self.task_description(USECASE_ADVISOR_TASK),
            expected_output=self.task_expected_output(USECASE_ADVISOR_TASK),
            output_file=os.path.join(company_name,self.taskconfig.user_advisor_output+readme_extension),
            agent = self.UseCaseAdvisorAgent
            )
            FeasibilityCheckerTask = Task(
            description = self.task_description(FEASIBLITY_CHECKEAR_TASK),
            expected_output=self.task_expected_output(FEASIBLITY_CHECKEAR_TASK),
            output_file=os.path.join(company_name,self.taskconfig.feasiblity_checker_output+readme_extension),
            agent = self.FeasibilityCheckerAgent
            )
            ResourceAssetCollectionTask = Task(
            description = self.task_description(RESOURCE_ALLOCATOR_TASK),
            expected_output=self.task_expected_output(RESOURCE_ALLOCATOR_TASK),
            output_file=os.path.join(company_name,self.taskconfig.resource_allocator_output+readme_extension),
            agent = self.ResourceAssetCollectionAgent
            )
            return CompanyAnalysisTask,UseCaseAdvisorTask,FeasibilityCheckerTask,ResourceAssetCollectionTask
        except Exception as e:
            raise CustomException(e,sys)
        























