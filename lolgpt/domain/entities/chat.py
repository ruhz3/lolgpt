from dataclasses import dataclass


@dataclass
class Chat:
    chat_id: str
    user_id: str
    start_time: str
    update_time: str
