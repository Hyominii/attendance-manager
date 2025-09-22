from constant import Score, INPUT_FILE, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY, \
    MAX_INPUT_FILE_LEN, BONUS_SCORE, Grade

team_roster = {}
id_cnt = 0

# dat[사용자ID][요일]
dat = [[0] * 100 for _ in range(100)]
points = [0] * 100
grade = [0] * 100
names = [''] * 100
training_attendance = [0] * 100
weekend_attendance = [0] * 100


def process_attendance(name, day_of_the_week):
    global id_cnt

    # team_roster: key -> name, value -> uniform number(id)
    if name not in team_roster:
        id_cnt += 1
        team_roster[name] = id_cnt
        names[id_cnt] = name

    uniform_number = team_roster[name]

    add_point = 0
    index = 0

    if day_of_the_week == "monday":
        index = 0
        add_point += Score.normal
    elif day_of_the_week == "tuesday":
        index = 1
        add_point += Score.normal
    elif day_of_the_week == "wednesday":
        index = 2
        add_point += Score.training
        training_attendance[uniform_number] += Score.normal
    elif day_of_the_week == "thursday":
        index = 3
        add_point += Score.normal
    elif day_of_the_week == "friday":
        index = 4
        add_point += Score.normal
    elif day_of_the_week == "saturday":
        index = 5
        add_point += 2
        weekend_attendance[uniform_number] += Score.weekend
    elif day_of_the_week == "sunday":
        index = 6
        add_point += 2
        weekend_attendance[uniform_number] += Score.weekend

    dat[uniform_number][index] += 1
    points[uniform_number] += add_point


def main():
    try:
        process_input_file()
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
    else:
        cal_bonus_score()
        rate_grade()
        print_attendance_score()
        print_removed_player()


def process_input_file():
    with open(INPUT_FILE, encoding='utf-8') as f:
        for _ in range(MAX_INPUT_FILE_LEN):
            line = f.readline()
            if not line:
                break
            parts = line.strip().split()
            if len(parts) == 2:
                process_attendance(parts[0], parts[1])


def print_removed_player():
    print("\nRemoved player")
    print("==============")
    for i in range(1, id_cnt + 1):
        if grade[i] not in (1, 2) and training_attendance[i] == 0 and weekend_attendance[i] == 0:
            print(names[i])


def print_attendance_score():
    for i in range(1, id_cnt + 1):
        print(f"NAME : {names[i]}, POINT : {points[i]}, GRADE : ", end="")
        if grade[i] == Grade.gold:
            print("GOLD")
        elif grade[i] == Grade.silver:
            print("SILVER")
        else:
            print("NORMAL")


def rate_grade():
    for i in range(1, id_cnt + 1):
        if points[i] >= 50:
            grade[i] = Grade.gold
        elif points[i] >= 30:
            grade[i] = Grade.silver
        else:
            grade[i] = Grade.normal


def cal_bonus_score():
    for i in range(1, id_cnt + 1):
        if dat[i][2] >= 10:  # 트레이닝 데이 출석이 10회 이상일 경우 추가 점수
            points[i] += BONUS_SCORE
        if dat[i][5] + dat[i][6] >= 10:  # 주말 출석이 10회 이상일 경우 추가 점수
            points[i] += BONUS_SCORE


if __name__ == "__main__":
    main()
