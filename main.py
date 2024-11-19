from agents.orchestrator import Orchestrator
if __name__ == "__main__":
    brd_text = """
    Title: Online Store Project
    Description: A system to manage an online store
    Requirements:
    - User authentication
    - Product catalog management
    - Payment integration
    """
    orchestrator = Orchestrator()
    orchestrator.run(brd_text)
