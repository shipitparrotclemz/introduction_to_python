from datetime import datetime
from typing import Callable, Any


def timeit(func: Callable[[...], Any]) -> Any:
    """
    This is a magic wand that edits a magic wand
    To print out how long it takes
    """
    def timed_function(*args, **kwargs) -> Any:
        start: datetime = datetime.utcnow()
        result: Any = func(*args, **kwargs)
        end: datetime = datetime.utcnow()
        total_seconds: float = (end - start).total_seconds()
        print(f"{func.__name__} took {total_seconds} seconds")
        return result
    return timed_function
