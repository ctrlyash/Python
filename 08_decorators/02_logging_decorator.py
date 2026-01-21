# Logging using a decorator means:
#  Automatically recording (printing or saving) information about a function—such as
# when it is called
# what arguments it receives
# what it returns
# —without changing the function’s actual code.

from functools import wraps

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"🚀Calling: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"✅ Finished: {func.__name__}")
        return result
    return wrapper

@log_activity
def brew_chai(type, milk="no"):
    print(f"Brewing {type} chai and milk status {milk}")


brew_chai("Masala")  

# 🚀Calling: brew_chai
# Brewing Masala chai and milk status no
# ✅ Finished: brew_chai