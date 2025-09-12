from .agent_base import IDEAgent

class CodeCompletionAgent(IDEAgent):
    """
    Example agent for code completion.
    """
    def __init__(self):
        super().__init__("CodeCompletionAgent")

    def run(self, context: dict) -> dict:
        # Placeholder: returns a static completion
        code = context.get("code", "")
        completion = code + "\n# TODO: Complete this function"
        return {"completion": completion}