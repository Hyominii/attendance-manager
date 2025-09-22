import pytest
import pytest_mock
from attendance import AttendanceManager
from constant import INPUT_FILE


def test_result(capsys):
    manager = AttendanceManager()
    manager.run()
    captured = capsys.readouterr()

    with open("result.txt", encoding='utf-8') as f:
        assert captured.out == f.read()

