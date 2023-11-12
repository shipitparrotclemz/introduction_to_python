from datetime import datetime
from typing import Any, Callable


def timeit(func: Callable[[...], Any]) -> Any:
    """
    This is a magic wand that edits a magic wand
    To print out how long it takes
    """
    def timed_function(*args, **kwargs) -> Any:
        start: datetime = datetime.utcnow()
        result: Any = func(*args, **kwargs)
        end: datetime = datetime.utcnow()
        total_seconds: int = (end - start).total_seconds()
        print(f"{func.__name__} took {total_seconds} seconds")
    return timed_function

@timeit
def list_append() -> None:
    """
    Define a list of 1,000,000 eggs
    Then call append magic wand to add one egg to the back
    """
    my_list: list[str] = ["Mocha"] * 1000000
    my_list.append("Tea")
    # print(my_list)

@timeit
def list_redefinition() -> None:
    my_list: list[str] = ["Mocha"] * 1000000
    my_list = ["Mocha"] * 1000000 + ["Tea"]
    # print(my_list)

list_redefinition()
list_append()