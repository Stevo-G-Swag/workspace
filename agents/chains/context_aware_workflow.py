class ContextAwareWorkflow:

    def __init__(self, context, chains):
        self.context = context
        self.chains = chains

    def execute(self):
        print(f"Executing workflow in context: {self.context}")
        for chain in self.chains:
            try:
                chain.execute()
                print(f"Chain executed successfully in context: {self.context}")
            except Exception as e:
                print(f"Error executing chain in context: {self.context}: {e}", exc_info=True)
        print("Workflow executed successfully.")