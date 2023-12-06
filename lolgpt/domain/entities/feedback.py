from dataclasses import dataclass


@dataclass
class Feedback:
    turn_id: str
    feedback_id: str
    comment: str
    is_positive: bool
    create_time: str
