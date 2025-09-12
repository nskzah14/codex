class IDEAgent:
    """
    Base class for IDE Agents.
    Agents can implement code completion, error detection, automation, image analysis, or other IDE tasks.
    """
    def __init__(self, name: str):
        self.name = name

    def run(self, context: dict) -> dict:
        """
        Run the agent with the given context.
        Should be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses must implement this method.")