from pydantic import BaseModel
from typing import Optional, List

class Ticket(BaseModel):
    id: int
    text: str
    category: Optional[str] = None
    priority: Optional[str] = None
    resolved: bool = False


class Action(BaseModel):
    message: str


class Observation(BaseModel):
    ticket_id: int
    ticket_text: str
    last_agent_message: Optional[str]
    status: str


class Reward(BaseModel):
    value: float


class EnvironmentState(BaseModel):
    current_ticket: Ticket
    steps_taken: int
    done: bool