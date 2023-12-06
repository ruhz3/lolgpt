from lolgpt.application.interfaces.chat_data_access import ChatDataAccess
from dataclasses import dataclass
from abc import ABC, abstractmethod
import uuid
from datetime import datetime


# InputDTO
@dataclass
class NewChatInputDto:
    user_id: str


# InputBoundary
class NewChatInputBoundary(ABC):
    @abstractmethod
    def create_chat(self, input_dto: NewChatInputDto) -> None:
        pass


# UseCase
class NewChatUseCase(NewChatInputBoundary):
    def __init__(self, chat_dao: ChatDataAccess):
        self._data_access = chat_dao

    def create_chat(self, input_dto: NewChatInputDto) -> None:
        self._data_access.create_chat(
            chat_id=str(uuid.uuid4()),
            user_id=input_dto.user_id,
            start_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
