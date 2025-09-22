from abc import ABC, abstractmethod
from constant import Score
from player import Player


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
