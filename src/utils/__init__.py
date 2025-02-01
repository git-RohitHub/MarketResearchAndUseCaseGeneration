from crewai_tools import SerperDevTool , ScrapeWebsiteTool
from crewai import LLM
from pydantic import BaseModel
from dotenv import load_dotenv
from typing import Dict, Tuple
import yaml
from src.exception import CustomException
from src.logger import logger
import sys
import json
import os 
load_dotenv()

# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["SERPERAPI_KEY"] = os.getenv("SERPER_API_KEY")

class CompanyDetails(BaseModel):
  Name : str
  Goal : str
  Industry : str
  KeyAreas : str
  MainFocus : str
  OtherImportantInformation:str

class MainUtils:
    def __init__(self) -> None:
        pass

    def read_yaml_file(self, filename: str) -> dict:
        logger.info(":) READING YAML FILE :)")
        try:
            with open(filename, "r") as yaml_file:
                return yaml.safe_load(yaml_file)

        except Exception as e:
            raise CustomException(e, sys) from e
        
    def extracting_agent(self,filepath,agentname:str,data:str):
      logger.info(f":) LOADING AGENT : {agentname} Data :)")
      try:
        completedata = self.read_yaml_file(filepath) 
        for agent in completedata['agents']:
          if agent['name']==agentname:
            return agent[f'{data}']
      except Exception as e:
         raise CustomException(e,sys)
        
    def extracting_tasks(self,filepath,taskname:str,data:str):
      logger.info(f":) LOADING TASK : {taskname} DATA ;)")
      try:
        completedata = self.read_yaml_file(filepath) 
        for task in completedata['tasks']:
          if task['name']==taskname:
            return task[data]
      except Exception as e:
         raise CustomException(e,sys)
        
        
    def load_tools(self):
      logger.info(":) LOADING TOOLS :)")
      try:
        self.search_tool = SerperDevTool()
        self.scrape_tool = ScrapeWebsiteTool()
        return self.search_tool,self.scrape_tool
      except Exception as e:
         raise CustomException(e,sys)
    
    def load_llm(self,model:str,temperature:float=0.7):
      logger.info(":) LOADING LLM :)")
      try:
        llm = LLM(
        model = model,
        temperature=temperature,
        )
        return llm
      except Exception as e:  
         raise CustomException(e,sys)

    
    def load_json_file(self,filepath):
      logger.info(":) LOADING JSON FILE :)")
      try:
        with open(filepath,'r') as file : 
          data = json.load(file)
        return data
      except Exception as e:
         raise CustomException(e,sys)
    
    def convert_json_md(self,json_file_path):
      logger.info(":) CONVERTION JSON TO MD :)")
      try:
        filename = json_file_path.split('.')[0]
        data = self.load_json_file(json_file_path)
        with open(f"{filename}.md",'a') as f:
          for keys in data.keys():
            f.write(f"**{keys}** : {data[keys]} \n\n")
      
      except Exception as e:
         raise CustomException(e,sys)
    def extract_company_first_name(company_name):
       return company_name.split(' ')[0]
       
    




    


        



        
 








  