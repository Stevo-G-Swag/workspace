class Crew:

    def __init__(self, agents):
        self.agents = agents
        self.tasks = []

    def assign_task(self, task):
        self.tasks.append(task)
        return task.execute()
