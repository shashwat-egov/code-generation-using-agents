import yaml
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileReadTool, FileWriterTool

@CrewBase
class LatestAiDevelopmentCrew:
    """LatestAiDevelopment crew"""
    
    def __init__(self):
        # Load agents_config and tasks_config from YAML files
        with open("D:/latest_ai_development/src/latest_ai_development/config/agents.yaml", "r") as agents_file:
            self.agents_config = yaml.safe_load(agents_file)
        
        with open("D:/latest_ai_development/src/latest_ai_development/config/tasks.yaml", "r") as tasks_file:
            self.tasks_config = yaml.safe_load(tasks_file)

        # Debugging: Print loaded configurations
        print("Loaded Agents Config:", self.agents_config)
        print("Loaded Tasks Config:", self.tasks_config)
    
    @agent
    def tech_lead(self) -> Agent:
        if 'tech_lead' not in self.agents_config:
            raise KeyError("Missing configuration for 'tech_lead' in agents_config.")
        return Agent(
            config=self.agents_config['tech_lead'],
            allow_delegation=True,
            verbose=True,
            tools=[FileReadTool(file_path='D:/latest_ai_development/openapi.yaml')],
            memory=True
        )

    @agent
    def controller_developer(self) -> Agent:
        if 'controller_developer' not in self.agents_config:
            raise KeyError("Missing configuration for 'controller_developer' in agents_config.")
        return Agent(
            config=self.agents_config['controller_developer'],
            allow_delegation=False,
            verbose=True
        )

    @agent
    def service_developer(self) -> Agent:
        if 'service_developer' not in self.agents_config:
            raise KeyError("Missing configuration for 'service_developer' in agents_config.")
        return Agent(
            config=self.agents_config['service_developer'],
            allow_delegation=False,
            verbose=True
        )
    
    @agent
    def repository_developer(self) -> Agent:
        if 'repository_developer' not in self.agents_config:
            raise KeyError("Missing configuration for 'repository_developer' in agents_config.")
        return Agent(
            config=self.agents_config['repository_developer'],
            allow_delegation=False,
            verbose=True
        )

    @agent
    def qa_engineer(self) -> Agent:
        if 'qa_engineer' not in self.agents_config:
            raise KeyError("Missing configuration for 'qa_engineer' in agents_config.")
        return Agent(
            config=self.agents_config['qa_engineer'],
            allow_delegation=False,
            verbose=True
        )

    @agent
    def project_writer(self) -> Agent:
        if 'project_writer' not in self.agents_config:
            raise KeyError("Missing configuration for 'project_writer' in agents_config.")
        return Agent(
            config=self.agents_config['project_writer'],
            allow_delegation=False,
            verbose=True,
            tools=[FileWriterTool()]
        )

    @task
    def parse_api_contract(self) -> Task:
        if 'parse_api_contract' not in self.tasks_config:
            raise KeyError("Missing configuration for 'parse_api_contract' in tasks_config.")
        return Task(
            config=self.tasks_config['parse_api_contract'],
            agent=self.tech_lead()
        )

    @task
    def implement_controller(self) -> Task:
        if 'implement_controller' not in self.tasks_config:
            raise KeyError("Missing configuration for 'implement_controller' in tasks_config.")
        return Task(
            config=self.tasks_config['implement_controller'],
            agent=self.controller_developer()
        )

    @task
    def implement_service(self) -> Task:
        if 'implement_service' not in self.tasks_config:
            raise KeyError("Missing configuration for 'implement_service' in tasks_config.")
        return Task(
            config=self.tasks_config['implement_service'],
            agent=self.service_developer()
        )
    
    @task
    def implement_repository(self) -> Task:
        if 'implement_repository' not in self.tasks_config:
            raise KeyError("Missing configuration for 'implement_repository' in tasks_config.")
        return Task(
            config=self.tasks_config['implement_repository'],
            agent=self.repository_developer()
        )
    
    @task
    def perform_testing(self) -> Task:
        if 'perform_testing' not in self.tasks_config:
            raise KeyError("Missing configuration for 'perform_testing' in tasks_config.")
        return Task(
            config=self.tasks_config['perform_testing'],
            agent=self.qa_engineer()
        )
    
    @task
    def write_project_task(self) -> Task:
        if 'write_project_task' not in self.tasks_config:
            raise KeyError("Missing configuration for 'write_project_task' in tasks_config.")
        return Task(
            config=self.tasks_config['write_project_task'],
            agent=self.project_writer()
        )

    @crew
    def crew(self) -> Crew:
        """Creates the LatestAiDevelopment crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )