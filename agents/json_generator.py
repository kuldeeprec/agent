import json
from utils.openai_helper import query_openai
from models.json_schema import GeneratedJSON
from utils.agent_communication import AgentCommunicationChannel

class JSONGeneratorAgent:
    def __init__(self, comm_channel: AgentCommunicationChannel):
        self.comm_channel = comm_channel

    def generate_json(self, brd_model):
        self.comm_channel.send_message("JSONGeneratorAgent", "ValidationAgent", "Starting JSON generation")

        # Use OpenAI to generate JSON
        prompt = f"Create a JSON structure based on the following requirements:\n{brd_model.requirements}"
        response = query_openai(prompt,response_format=GeneratedJSON)

        if not response:
            error_message = "Received empty response from OpenAI."
            self.comm_channel.send_message("JSONGeneratorAgent", "ErrorHandlingAgent", error_message)
            return None
        else:
           return response
