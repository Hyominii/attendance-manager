from constant import Score, INPUT_FILE, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY, \
    BONUS_SCORE
from file_handler import FileHandler
from grade import GradeFactory, NormalGrade
from player import Player
from algorithm import TrainingDayAlgorithm, WeekdayAlgorithm, WeekendAlgorithm


class AttendanceManager:
    def __init__(self):
        self._id_cnt = 0
        self._team_roster = dict()
        self._players_info = list()

    def run(self):
        try:
            self._process_input_file()
        except FileNotFoundError:
            print("파일을 찾을 수 없습니다.")
        else:
            self._cal_bonus_score()
            self._rate_grade()
            self._print_attendance_score()
            self._print_removed_player()

    def _process_attendance(self, team_roster: dict, name: str, day_of_the_week: str):
        # team_roster: key -> name, value -> uniform number(id)
        if name not in team_roster:
            self._id_cnt += 1
            self._players_info.append(Player(self._id_cnt, name))
            self._team_roster[name] = self._id_cnt

        uniform_number = self._team_roster[name]
        player_index = uniform_number - 1

        self._cal_player_score(day_of_the_week, player_index)

    # strategy pattern
    def _cal_player_score(self, day_of_the_week, player_index):
        player = self._players_info[player_index]

        if day_of_the_week in (MONDAY, TUESDAY, THURSDAY, FRIDAY):
            WeekdayAlgorithm.cal_score(player)
        elif day_of_the_week in (SATURDAY, SUNDAY):
            WeekendAlgorithm.cal_score(player)
        elif day_of_the_week == WEDNESDAY:
            TrainingDayAlgorithm.cal_score(player)

    def _process_input_file(self):
        file_handler = FileHandler(INPUT_FILE)
        file_content = file_handler.read_all_lines()
        for line in file_content:
            parts = line.strip().split()
            if len(parts) == 2:
                self._process_attendance(self._team_roster, parts[0], parts[1])

    def _print_removed_player(self):
        print("\nRemoved player")
        print("==============")

        for i in range(len(self._players_info)):
            player = self._players_info[i]
            if self._should_be_removed(player):
                print(self._players_info[i].name)

    def _should_be_removed(self, player: Player) -> bool:
        return isinstance(player.grade,
                          NormalGrade) and player.training_attendance == 0 and player.weekend_attendance == 0

    def _print_attendance_score(self):
        for i in range(len(self._players_info)):
            print(self._players_info[i])

    def _rate_grade(self):
        for i in range(len(self._players_info)):
            self._players_info[i].grade = GradeFactory.generate_grade(self._players_info[i].point)

    def _cal_bonus_score(self):
        for i in range(len(self._players_info)):
            if self._players_info[i].training_attendance >= 10:  # 트레이닝 데이 출석이 10회 이상일 경우 추가 점수
                self._players_info[i].point += BONUS_SCORE
            if self._players_info[i].weekend_attendance >= 10:  # 주말 출석이 10회 이상일 경우 추가 점수
                self._players_info[i].point += BONUS_SCORE


if __name__ == "__main__":
    manager = AttendanceManager()
    manager.run()
