from models.schemas import Ticket

TASKS = {
    "easy": {
        "description": "Classify the ticket correctly",
        "goal": "Set correct category"
    },
    "medium": {
        "description": "Classify and assign priority",
        "goal": "Set category and priority"
    },
    "hard": {
        "description": "Fully resolve the ticket",
        "goal": "Classify, respond, and resolve"
    }
}


def generate_ticket():
    return Ticket(
        id=1,
        text="Payment failed but money deducted"
    )