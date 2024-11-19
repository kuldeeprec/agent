from utils.openai_helper import query_openai
from utils.agent_communication import AgentCommunicationChannel

class ErrorHandlingAgent:
    def __init__(self, comm_channel: AgentCommunicationChannel):
        self.comm_channel = comm_channel

    def handle_error(self, error_message: str) -> str:
        # Log the error for traceability and communication
        self.comm_channel.send_message("ErrorHandlingAgent", "AllAgents", f"Handling error: {error_message}")

        # Generate an error correction suggestion using OpenAI
        prompt = (
            f"Given the following error message, suggest possible corrections and steps to resolve it:\n"
            f"Error Message: {error_message}\n"
            "Provide a detailed explanation and actionable steps."
        )
        correction_suggestion = query_openai(prompt)

        # Log the suggested correction for traceability and further actions
        self.comm_channel.send_message("ErrorHandlingAgent", "AllAgents", f"Correction Suggestion: {correction_suggestion}")

        return correction_suggestion

