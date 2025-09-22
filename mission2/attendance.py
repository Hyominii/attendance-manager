from constant import Score, INPUT_FILE, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY, \
    BONUS_SCORE, Grade, BASE_SCORE, NAME, WEEKEND_ATTENDANCE, POINT, TRAINING_ATTENDANCE, GRADE, \
    BASE_ATTENDANCE, GOLD_THRESHOLD, SILVER_THRESHOLD
from file_handler import FileHandler
from mission2.grade import GradeFactory


class AttendanceManager:
    def __init__(self):
        self._id_cnt = 0

    def run(self):
        team_roster = {}
        players_info = list()
        try:
            self._process_input_file(team_roster, players_info)
        except FileNotFoundError:
            print("파일을 찾을 수 없습니다.")
        else:
            self._cal_bonus_score(players_info)
            self._rate_grade(players_info)
            self._print_attendance_score(players_info)
            self._print_removed_player(players_info)

    def _process_attendance(self, team_roster: dict, players_info: list, name: str, day_of_the_week: str):
        # team_roster: key -> name, value -> uniform number(id)
        if name not in team_roster:
            self._id_cnt += 1
            players_info.append({
                "name": name,
                "id": self._id_cnt,
                "point": BASE_SCORE,
                "grade": Grade.normal,
                "training_attendance": BASE_ATTENDANCE,
                "weekend_attendance": BASE_ATTENDANCE
            })
            team_roster[name] = self._id_cnt

        uniform_number = team_roster[name]
        player_index = uniform_number - 1

        self._cal_player_score(day_of_the_week, player_index, players_info)

    def _cal_player_score(self, day_of_the_week, player_index, players_info):
        add_point = 0

        if day_of_the_week == MONDAY:
            add_point += Score.normal
        elif day_of_the_week == TUESDAY:
            add_point += Score.normal
        elif day_of_the_week == WEDNESDAY:
            add_point += Score.training
            players_info[player_index][TRAINING_ATTENDANCE] += 1
        elif day_of_the_week == THURSDAY:
            add_point += Score.normal
        elif day_of_the_week == FRIDAY:
            add_point += Score.normal
        elif day_of_the_week == SATURDAY:
            add_point += Score.weekend
            players_info[player_index][WEEKEND_ATTENDANCE] += 1
        elif day_of_the_week == SUNDAY:
            add_point += Score.weekend
            players_info[player_index][WEEKEND_ATTENDANCE] += 1

        players_info[player_index][POINT] += add_point

    def _process_input_file(self, team_roster: dict, players_info: list):
        file_handler = FileHandler(INPUT_FILE)
        file_content = file_handler.read_all_lines()
        for line in file_content:
            parts = line.strip().split()
            if len(parts) == 2:
                self._process_attendance(team_roster, players_info, parts[0], parts[1])

    def _print_removed_player(self, players_info: list):
        print("\nRemoved player")
        print("==============")

        for i in range(len(players_info)):
            if (players_info[i][GRADE] not in (Grade.gold, Grade.silver)
                    and players_info[i][TRAINING_ATTENDANCE] == 0
                    and players_info[i][WEEKEND_ATTENDANCE] == 0):
                print(players_info[i][NAME])

    def _print_attendance_score(self, players_info: list):
        for i in range(len(players_info)):
            print(f"NAME : {players_info[i][NAME]}, POINT : {players_info[i][POINT]}, GRADE : ", end="")
            print(players_info[i][GRADE])

    def _rate_grade(self, players_info: list):
        for i in range(len(players_info)):
            players_info[i][GRADE] = GradeFactory.generate_grade(players_info[i][POINT])

    def _cal_bonus_score(self, players_info: list):
        for i in range(len(players_info)):
            if players_info[i][TRAINING_ATTENDANCE] >= 10:  # 트레이닝 데이 출석이 10회 이상일 경우 추가 점수
                players_info[i][POINT] += BONUS_SCORE
            if players_info[i][WEEKEND_ATTENDANCE] >= 10:  # 주말 출석이 10회 이상일 경우 추가 점수
                players_info[i][POINT] += BONUS_SCORE


if __name__ == "__main__":
    manager = AttendanceManager()
    manager.run()
