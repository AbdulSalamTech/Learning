def announce(f):
    def wrapper():
        print("about to run")
        f()
        print("executed")
    return wrapper

@announce
def hello():
    print("hello world")

hello()