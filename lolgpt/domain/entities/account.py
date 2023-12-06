from dataclasses import dataclass


@dataclass
class Account:
    id: str
    password: str
    email: str
    create_time: str
