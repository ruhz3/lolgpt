from dataclasses import dataclass


@dataclass
class Turn:
    chat_id: str
    turn_id: str
    user_message: str
    ai_message: str
    create_time: str
