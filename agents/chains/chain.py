class Chain:

    def __init__(self, links):
        self.links = links

    def execute(self):
        result = None
        for link in self.links:
            try:
                result = link.execute()
                print(f"Executing link: {link.description} - Success")
            except Exception as e:
                print(f"Error executing link: {link.description}. Error: {e}")
                raise e
        return result