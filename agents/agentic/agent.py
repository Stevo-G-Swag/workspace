class Agent:

    def __init__(self,
                 role,
                 goal,
                 backstory,
                 tools=None,
                 verbose=False,
                 allow_delegation=True):
        self.role = role
        self.goal = goal
        self.backstory = backstory
        self.tools = tools if tools else []
        self.verbose = verbose
        self.allow_delegation = allow_delegation
        self.tasks = []

    def perform_task(self, task):
        if self.verbose:
            print(f"Agent {self.role} is performing task: {task.description}")

        task_result = None
        if task.description == 'analyze':
            task_result = self._analyze()
        elif task.description == 'plan':
            task_result = self._plan()
        elif task.description == 'execute':
            task_result = self._execute()
        else:
            if self.allow_delegation:
                task_result = self._delegate(task)
            else:
                raise ValueError(f"Unsupported task: {task.description}")

        if not any(t.description == task.description for t in self.tasks):
            self.tasks.append(task)
        return task_result

    def _analyze(self):
        if self.verbose:
            print(f"{self.role} is analyzing.")
        return "Analysis Result"

    def _plan(self):
        if self.verbose:
            print(f"{self.role} is planning.")
        return "Plan Result"

    def _execute(self):
        if self.verbose:
            print(f"{self.role} is executing.")
        return "Execution Result"

    def _delegate(self, task):
        if self.verbose:
            print(f"{self.role} is delegating task: {task.description}")
        return f"Delegated {task.description}"