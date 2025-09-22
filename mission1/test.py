import pytest
import pytest_mock
from attendance import main
from mission1.constant import INPUT_FILE


def test_result(capsys):
    main()
    captured = capsys.readouterr()

    with open("result.txt", encoding='utf-8') as f:
        assert captured.out == f.read()

