from pytest import fixture
@fxture
def greet():
    return "hello world"
def test_greet(greet):
    assert "hello world" == greet