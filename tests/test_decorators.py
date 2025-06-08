import pytest
from src.decorators import log




def test_faulty_function_logs_error(capsys):
    @log()
    def faulty_function(x, y):
        return x / y
    faulty_function(1, 1)
    captured = capsys.readouterr()
    assert 'faulty_function ok\n' in captured.out


    @log('mylog_test.txt')
    def my_fanc(x, y):
        return x + y

    my_fanc(15, 10)
    captured = capsys.readouterr()
    assert '' in captured.out
