from dataclasses import dataclass
from constant import BASE_ATTENDANCE, BASE_SCORE
from grade import Grade, NormalGrade


@dataclass
class Player:
    _id: int
    name: str
    point: int = BASE_SCORE
    _grade: Grade = NormalGrade
    training_attendance: int = BASE_ATTENDANCE
    weekend_attendance: int = BASE_ATTENDANCE

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, target_grade: Grade):
        self._grade = target_grade

    def __repr__(self):
        return f"NAME : {self.name}, POINT : {self.point}, GRADE : {self.grade}"
