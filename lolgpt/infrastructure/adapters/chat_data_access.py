from lolgpt.application.interfaces.chat_data_access import ChatDataAccess
from abc import ABC

from lolgpt.domain.entities.chat import Chat


class PostgresChatDataAccess(ChatDataAccess):
    def __init__(self, config):
        pass

    def read_chat(self, chat_id: str) -> Chat:
        pass

    def create_chat(self, chat_id: str, user_id: str, start_time: str) -> None:
        pass

    def update_chat(self, start_time) -> None:
        pass
