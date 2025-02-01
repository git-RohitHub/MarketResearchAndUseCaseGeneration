# 🚀 Market Research & Use Cases Generator
##### live link : 
         https://marketresearchandusecasegeneration.onrender.com/
## 📌 Overview
The **Market Research & Use Cases Generator** is a powerful AI-driven application designed to analyze companies, generate AI/ML use cases, assess feasibility, and collect relevant resources. This tool leverages **LLMs, web scraping, and automation** to streamline the market research process and provide valuable insights.

## 🎯 Features
✅ **Company Analysis**: Scrapes and analyzes company details, including industry trends and key focus areas.  
✅ **AI/ML Use Case Generation**: Proposes industry-specific AI/ML applications to enhance business operations.  
✅ **Feasibility Assessment**: Evaluates economic and technical feasibility of proposed AI/ML use cases.  
✅ **Resource Collection**: Identifies datasets, tools, and frameworks to implement AI solutions.  
✅ **Interactive UI**: Built with **Streamlit** for an intuitive user experience.  
✅ **Automated Report Generation**: Outputs structured **JSON & Markdown** reports.  

## 🏗️ Project Architecture
The project follows a **modular AI-driven architecture** using multiple agents and tools. The workflow is structured as follows:

1. **User Input**: Company details (name & website) are provided through the Streamlit UI.
2. **Agent-Based Processing**:
   - `CompanyAnalystAgent`: Extracts company details and industry insights.
   - `UseCaseAdvisorAgent`: Suggests AI/ML applications tailored to the company.
   - `FeasibilityCheckerAgent`: Evaluates implementation feasibility.
   - `ResourceAssetCollectionAgent`: Gathers necessary datasets & tools.
3. **Data Retrieval & Processing**:
   - Uses `SerperDevTool` for web search and `ScrapeWebsiteTool` for extracting content.
   - Runs LLM (`GPT-4o-mini`) for text generation & summarization.
4. **Report Generation**:
   - Outputs structured **JSON and Markdown** reports.
   - Displays insights in multiple tabs within Streamlit UI.

## 📂 Directory Structure
```
project_root/
│── app.py  # Main Streamlit Application
│── requirements.txt  # Dependencies
│── .env  # Environment Variables
│
├── config/
│   ├── system.yaml  # Agent & Task Configurations
│
├── reports/  # Generated Reports
│   ├── company_details.json
│   ├── use_cases.md
│   ├── feasibility_report.md
│   ├── resource_assets.md
│
├── src/
│   ├── components/  # Core Logic
│   │   ├── agents.py  # Defines AI Agents
│   │   ├── crew.py  # Manages AI Crew & Execution
│   │   ├── tasks.py  # Defines Task Assignments
│   │   ├── constants/
│   │   │   ├── __init__.py  # Static Configurations
│   │
│   ├── utils/  # Utility Functions
│   │   ├── __init__.py  # Handles Data Processing & LLM Loading
│   │   ├── logger.py  # Logging Mechanism
│   │   ├── exception.py  # Custom Exception Handling
│
└── README.md  # Project Documentation
```

## 🚀 Installation & Setup
### **1️⃣ Prerequisites**
Ensure you have the following installed:
- Python 3.8+
- pip (Python package manager)

### **2️⃣ Clone the Repository**
```sh
git clone https://github.com/your-repo/market-research-use-cases.git
cd market-research-use-cases
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Set Up Environment Variables**
Create a `.env` file and add your API keys:
```
OPENAI_API_KEY=your_openai_key
SERPER_API_KEY=your_serperapi_key
```

### **5️⃣ Run the Application**
```sh
streamlit run app.py
```

## 📊 How It Works
1. Enter **Company Name** and **Website URL** in the Streamlit UI.
2. Click **Generate Reports** to initiate AI-driven analysis.
3. View generated reports in multiple tabs:
   - **Company Details**
   - **Use Case Report**
   - **Feasibility Report**
   - **Resource Assets**

## 🛠️ Technologies Used
- **Streamlit** - Interactive UI framework
- **CrewAI** - AI-driven task automation
- **OpenAI API** - LLM-powered text generation
- **SerperDevTool** - AI-based web search
- **ScrapeWebsiteTool** - Web content extraction
- **Pydantic** - Data validation
- **YAML, JSON, Markdown** - Data formats

## 📌 Future Improvements
🔹 Add support for **more AI/ML models** for use case generation.  
🔹 Enhance **search capabilities** with additional data sources.  
🔹 Optimize report **formatting & visualization**.  

## 💡 Contributing
We welcome contributions! Feel free to **fork** this repository, submit **issues**, or create **pull requests**.

## 📜 License
This project is licensed under the **MIT License**.

For any inquiries or support, reach out via:
📧 Email: rohit2852001@gmail.com
---
🎯 **Built for AI-driven Business Insights!** 🚀

