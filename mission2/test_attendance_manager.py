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
    file_handler = FileHandler("test.txt")
    target_line = "hi, good"

    file_handler.write(target_line)
    line = file_handler.read()

    assert line == target_line


def test_attendance_manager_file_not_found(capsys):
    manager = AttendanceManager()

    manager.run(target_file="tes.txt")
    captured = capsys.readouterr()

    assert "파일을 찾을 수 없습니다." in captured.out

