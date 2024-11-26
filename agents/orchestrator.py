from agents.brd_parser import BRDParsingAgent
from agents.json_generator import JSONGeneratorAgent
from agents.error_handler import ErrorHandlingAgent
from utils.agent_communication import AgentCommunicationChannel

class Orchestrator:
    def __init__(self):
        self.comm_channel = AgentCommunicationChannel()
        self.brd_parser = BRDParsingAgent(self.comm_channel)
        self.json_generator = JSONGeneratorAgent(self.comm_channel)
        self.error_handler = ErrorHandlingAgent(self.comm_channel)

    def run(self, brd_text: str):
        brd_model = self.brd_parser.parse_brd(brd_text)
        json_data = self.json_generator.generate_json(brd_model)
        if json_data is None:
            print("JSON generation failed.")
            return

        print("JSON generated successfully:", json_data)