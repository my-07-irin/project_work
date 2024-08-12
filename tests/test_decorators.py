def test_decorator_log(capsys):
    decorator_log(predicate: Callable, error_message: str):
    captured = capsys.readouterr()
    assert captured.out == f"Вызвана функция:example"
