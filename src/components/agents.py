from crewai import Agent
from src.utils import MainUtils
from src.constants import *
from src.logger import logger
from src.exception import CustomException
from dataclasses import dataclass
import sys
import os

class AgentConfig:
    yaml_file_path = os.path.join(config_folder,yaml_file_path)

@dataclass
class AgentCollections:
    def __init__(self):
        self.utils = MainUtils()
        self.config = AgentConfig()
        self.search_tool,self.scrape_tool = self.utils.load_tools()
        self.llm = self.utils.load_llm(model=model_name,temperature=temperature)

    def agent_role(self,agent_name,data='role'):
        return self.utils.extracting_agent(filepath=self.config.yaml_file_path,agentname=agent_name,data=data)
    
    def agent_goal(self,agent_name,data='goal'):
        return self.utils.extracting_agent(filepath=self.config.yaml_file_path,agentname=agent_name,data=data)
    
    def agent_backstory(self,agent_name,data='backstory'):
        return self.utils.extracting_agent(filepath=self.config.yaml_file_path,agentname=agent_name,data=data)
        


    def getAgents(self):
        logger.info(":) LOADING AGENTS :) ")
        try : 
            CompanyAnalystAgent = Agent(
            role = self.agent_role(COMPANY_ANALYST),
            goal = self.agent_goal(COMPANY_ANALYST),
            backstory = self.agent_backstory(COMPANY_ANALYST),
            tools= [self.search_tool,self.scrape_tool],
            llm = self.llm,
            verbose = False,
            agent_delegation = True
            )
            UseCaseAdvisorAgent = Agent(
            role = self.agent_role(USECASE_ADVISOR),
            goal = self.agent_goal(USECASE_ADVISOR),
            backstory = self.agent_backstory(USECASE_ADVISOR),
            tools= [self.search_tool,self.scrape_tool],
            llm = self.llm,
            verbose = False,
            agent_delegation = True
            )
            FeasibilityCheckerAgent = Agent(
            role = self.agent_role(FEASIBLITY_CHECKEAR),
            goal = self.agent_goal(FEASIBLITY_CHECKEAR),
            backstory = self.agent_backstory(FEASIBLITY_CHECKEAR),
            tools= [self.search_tool,self.scrape_tool],
            llm = self.llm,
            verbose = False,
            agent_delegation = True
            )
            ResourceAssetCollectionAgent = Agent(
            role = self.agent_role(RESOURCE_ALLOCATOR),
            goal = self.agent_goal(RESOURCE_ALLOCATOR),
            backstory = self.agent_backstory(RESOURCE_ALLOCATOR),
            tools= [self.search_tool,self.scrape_tool],
            llm = self.llm,
            verbose = False,
            agent_delegation = True
            )
            return CompanyAnalystAgent,UseCaseAdvisorAgent,FeasibilityCheckerAgent,ResourceAssetCollectionAgent
        except Exception as e:
            raise CustomException(e,sys)

