from utils.openai_helper import query_openai
from models.brd_model import BRDModel
from utils.agent_communication import AgentCommunicationChannel
import json
class BRDParsingAgent:
    def __init__(self, comm_channel: AgentCommunicationChannel):
        self.comm_channel = comm_channel

    def parse_brd(self, brd_text: str) -> BRDModel:
        self.comm_channel.send_message("BRDParsingAgent", "JSONGeneratorAgent", "Starting BRD Parsing")
        prompt = f"Extract the title, description, and key requirements from the following BRD:\n\n{brd_text}"
        response = query_openai(prompt,response_format=BRDModel)
        self.comm_channel.send_message("BRDParsingAgent", "JSONGeneratorAgent", f"Parsed BRD: {response}")
        return response
