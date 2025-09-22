import os
import pytest
from pytest_mock import MockerFixture
from attendance import AttendanceManager
from constant import INPUT_FILE
from file_handler import FileHandler


def test_result(capsys):
    manager = AttendanceManager()
    manager.run()
    captured = capsys.readouterr()

    with open("result.txt", encoding='utf-8') as f:
        assert captured.out == f.read()


def test_file_handler_write_and_read():
    file_path = "test.txt"
    file_handler = FileHandler("test.txt")
    target_line = "hi, good"

    file_handler.write(target_line)
    line = file_handler.read()
    if os.path.exists(file_path):
        os.remove(file_path)

    assert line == target_line


def test_attendance_manager_file_not_found(capsys):
    manager = AttendanceManager()

    manager.run(target_file="tes.txt")
    captured = capsys.readouterr()

    assert "파일을 찾을 수 없습니다." in captured.out

def test_attendance_manager_run(mocker: MockerFixture):
    process_input_file_spy = mocker.spy(AttendanceManager, '_process_input_file')
    cal_bonus_score_spy = mocker.spy(AttendanceManager, '_cal_bonus_score')
    rate_grade_spy = mocker.spy(AttendanceManager, '_rate_grade')
    manager = AttendanceManager()

    manager.run()

    process_input_file_spy.assert_called_with(manager, INPUT_FILE)
    cal_bonus_score_spy.assert_called_once()
    rate_grade_spy.assert_called_once()