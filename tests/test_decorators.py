import pytest
from src.decorators import log

@log()
def faulty_function(x, y):
    return x / y


def test_faulty_function_logs_error(capsys):
    faulty_function(1, 0)
    captured = capsys.readouterr()
    assert "faulty_function error: division by zero" in captured.out


def test_log_with_filename('mylog_test.txt'):
    @log('mylog_test.txt')
    def my_fanc(x, y):
        return x + y
    my_fanc(15, 10)
    with open ('mylog_test.txt', 'r') as file:
        content = file.read()
        assert content == 'my_fanc 25'
