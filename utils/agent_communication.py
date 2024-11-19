class AgentCommunicationChannel:
    def __init__(self):
        self.message_log = []

    def send_message(self, sender: str, receiver: str, message: str):
        print(f"{sender} -> {receiver}: {message}")
        self.message_log.append((sender, receiver, message))

    def get_messages(self):
        return self.message_log
