class Task:

    def __init__(self, description, expected_output, agent):
        self.description = description
        self.expected_output = expected_output
        self.agent = agent

    def execute(self):
        try:
            result = self.agent.perform_task(self)
            print(f"Task '{self.description}' executed successfully.")
            return result
        except Exception as e:
            print(f"Error executing task '{self.description}': {e}")
            raise