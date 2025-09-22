from dataclasses import dataclass
from constant import BASE_ATTENDANCE, BASE_SCORE, Grade


@dataclass
class Player:
    _name: str
    _id: int
    _point: int = BASE_SCORE
    _grade: Grade = Grade.normal
    _training_attendance: int = BASE_ATTENDANCE
    _weekend_attendance: int = BASE_ATTENDANCE
