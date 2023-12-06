from dataclasses import dataclass


@dataclass
class Step:
    turn_id: str
    step_id: str
    step_num: str
    input: str
    create_time: str
