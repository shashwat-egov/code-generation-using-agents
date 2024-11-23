#!/usr/bin/env python
# src/latest_ai_development/main.py
import os
import sys
from dotenv import load_dotenv
from latest_ai_development.crew import LatestAiDevelopmentCrew

def run():
    """
    Run the crew to build a Spring Boot application using the provided API contract.
    """
    # Load environment variables from .env file
    load_dotenv()

    # Get the API contract path from the .env file
    api_contract_path = os.getenv('API_CONTRACT_PATH')
    print(api_contract_path)
    print(f"Resolved API contract path: {api_contract_path}")
    
    if not api_contract_path:
        print("Error: The environment variable 'API_CONTRACT_PATH' is not set in the .env file.")
        sys.exit(1)
    
    # Validate the file exists
    if not os.path.isfile(api_contract_path):
        print(f"Error: The file at path '{api_contract_path}' does not exist.")
        sys.exit(1)
    
    # Define inputs for the crew
    inputs = {
        'api_contract_path': api_contract_path
    }
    
    # Initialize and kickoff the crew
    LatestAiDevelopmentCrew().crew().kickoff(inputs={'api_contract_path': './open_api.yaml'})

if __name__ == "__main__":
    run()