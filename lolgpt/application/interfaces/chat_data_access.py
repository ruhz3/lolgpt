from lolgpt.domain.entities.chat import Chat
from abc import ABC, abstractmethod


class ChatDataAccess(ABC):
    @abstractmethod
    def read_chat(
            self,
            chat_id: str
    ) -> Chat:
        pass

    @abstractmethod
    def create_chat(
            self,
            chat_id: str,
            user_id: str,
            start_time: str
    ) -> None:
        pass

    @abstractmethod
    def update_chat(
            self,
            start_time
    ) -> None:
        pass
