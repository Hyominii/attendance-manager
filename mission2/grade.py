from abc import ABC
from dataclasses import dataclass
from constant import GOLD_THRESHOLD, SILVER_THRESHOLD


class GradeFactory:
    @staticmethod
    def generate_grade(point: int):
        if point >= GOLD_THRESHOLD:
            return GoldGrade()
        elif point >= SILVER_THRESHOLD:
            return SilverGrade()
        else:
            return NormalGrade()


class Grade(ABC):

    def __repr__(self):
        return self._repr_str


class GoldGrade(Grade):
    def __init__(self):
        self._repr_str = "GOLD"


class SilverGrade(Grade):
    def __init__(self):
        self._repr_str = "SILVER"


class NormalGrade(Grade):
    def __init__(self):
        self._repr_str = "NORMAL"
