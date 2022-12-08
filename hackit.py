import inspect
from business import Something


def decorator(fn):
    def wrapper(*args, **kwargs):
        print("before...")
        fn(*args, **kwargs)
        print("after...")
    return wrapper


for name, fn in inspect.getmembers(Something, inspect.isfunction):
    setattr(Something, name, decorator(fn))
