import threading


def Singleton(cls):
    _instances = {}
    _lock: threading.Lock = threading.Lock()

    def wrapper():
        with _lock:
            if cls not in _instances:
                _instances[cls] = cls()
        return _instances[cls]
    
    wrapper.__wrapped__ = cls
    return wrapper
    
