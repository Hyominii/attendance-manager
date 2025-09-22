from abc import ABC, abstractmethod
from constant import Score, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY
from player import Player


class AlgorithmFactory:
    @staticmethod
    def generate_algorithm(day_of_the_week: str, player: Player):
        if day_of_the_week in (MONDAY, TUESDAY, THURSDAY, FRIDAY):
            WeekdayAlgorithm.cal_score(player)
        elif day_of_the_week in (SATURDAY, SUNDAY):
            WeekendAlgorithm.cal_score(player)
        elif day_of_the_week == WEDNESDAY:
            TrainingDayAlgorithm.cal_score(player)


class Algorithm(ABC):
    @staticmethod
    @abstractmethod
    def cal_score(player: Player):
        ...


class TrainingDayAlgorithm(Algorithm):
    def cal_score(player: Player):
        player.point += Score.training
        player.training_attendance += 1


class WeekdayAlgorithm(Algorithm):
    def cal_score(player: Player):
        player.point += Score.normal


class WeekendAlgorithm(Algorithm):
    def cal_score(player: Player):
        player.point += Score.weekend
        player.weekend_attendance += 1
