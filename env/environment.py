from models.schemas import *
from tasks.tasks import TASKS, generate_ticket
from graders.grader import *
import random


class SupportEnv:

    def __init__(self, task_type="easy"):
        self.state = None
        self.task_type = task_type

    def reset(self):
        ticket = generate_ticket()

        self.state = EnvironmentState(
            current_ticket=ticket,
            steps_taken=0,
            done=False
        )

        return Observation(
            ticket_id=ticket.id,
            ticket_text=ticket.text,
            last_agent_message=None,
            status="open"
        )

    def step(self, action: Action):
        self.state.steps_taken += 1
        ticket = self.state.current_ticket

        reward = 0.0
        msg = action.message.lower()

        # Simulate classification
        if "payment" in msg:
            ticket.category = "billing"
            reward += 0.2

        if "urgent" in msg:
            ticket.priority = "high"
            reward += 0.2

        if "resolved" in msg or "fixed" in msg:
            ticket.resolved = True
            reward += 0.5
            self.state.done = True

        # Grading
        if self.task_type == "easy":
            final_score = grade_easy(ticket)
        elif self.task_type == "medium":
            final_score = grade_medium(ticket)
        else:
            final_score = grade_hard(ticket)

        # End condition
        if self.state.steps_taken >= 5:
            self.state.done = True

        return {
            "observation": Observation(
                ticket_id=ticket.id,
                ticket_text=ticket.text,
                last_agent_message=action.message,
                status="resolved" if ticket.resolved else "open"
            ),
            "reward": reward,
            "done": self.state.done,
            "info": {"score": final_score}
        }

    def state(self):
        return self.state