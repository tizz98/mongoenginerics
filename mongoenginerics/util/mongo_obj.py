import functools
import json


def to_json(fn):
    @functools.wraps(fn)
    def wrapper(self, *args, **kwargs):
        return json.loads(fn(self, *args, **kwargs).to_json())
    return wrapper


def save(fn):
    @functools.wraps(fn)
    def wrapper(self, *args, **kwargs):
        return fn(self, *args, **kwargs).save()
    return wrapper


def delete(fn):
    @functools.wraps(fn)
    def wrapper(self, *args, **kwargs):
        fn(self, *args, **kwargs).delete()
        return {"deleted": True, "id": args[0]}
    return wrapper
