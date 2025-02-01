import streamlit as st
import os
import time
from src.components import crewKickoff
from src.utils import MainUtils
from src.logger import logger

utils = MainUtils()

# Function to load file content
def load_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return file.read()
    return f"**{file_path} not found. It might be generated after execution.**"

# Streamlit Application
def main():
    # Sidebar for OpenAI API key input
    st.sidebar.title("Settings")
    openai_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password",placeholder="Don't worry we are not storing your key")
    os.environ["OPENAI_API_KEY"] = openai_key
    st.title("🚀 Market Research & Use Cases Generator")
    st.markdown("""
    **Generate detailed feasibility reports, use case insights, and resource asset reports for any company.**
    """)
    
    # Input section
    st.header("📌 Enter Company Details")
    company = st.text_input("🏢 Company Name", placeholder="Enter company name for use case generation")
    company_url = st.text_input("🔗 Company Website URL", placeholder="Enter company website link")
    
    if st.button("✨ Generate Reports"):
        if not openai_key:
            st.sidebar.error("⚠️ OpenAI API Key is required!")
        else:
            with st.spinner("🔄 Processing... Please wait while we generate insights!"):
                time.sleep(2)  # Simulating processing delay
                input_details = {"company": company, "company_url": company_url}
                company_name = input_details['company']
                crewKickoff(input_details, company_name)
                
                st.success("✅ Inputs submitted successfully! Generating reports...")
                time.sleep(1)
                
                # Display output files
                st.header("📊 Output Reports")
                
                json_file = f"{company_name}/reports/company_details.json"
                if os.path.exists(json_file):
                    utils.convert_json_md(json_file)
                
                feasibility_report = load_file(f"{company_name}/reports/feasiblity_report.md")
                use_case_report = load_file(f"{company_name}/reports/use_cases.md")
                resource_assets_report = load_file(f"{company_name}/reports/resource_assets.md")
                company_details = load_file(f"{company_name}/reports/company_details.md")
                
                # Tabs for different outputs
                tab1, tab2, tab3, tab4 = st.tabs([
                    "🏢 Company Details", "📌 Use Case Report", "📊 Feasibility Report", "📂 Resource Assets"
                ])
                
                with tab1:
                    st.subheader("🏢 Company Details")
                    st.write(company_details)
                
                with tab2:
                    st.subheader("📌 Use Case Report")
                    st.write(use_case_report)
                
                with tab3:
                    st.subheader("📊 Feasibility Report")
                    st.write(feasibility_report)
                
                with tab4:
                    st.subheader("📂 Resource Assets")
                    st.write(resource_assets_report)

if __name__ == "__main__":
    logger.info("Execution starts ")
    main()