# function that takes another function as an argument and returns a new function that modifies the behaviourof origional function


def greet(fx):
    def mfx():

        print("good morning")
        fx()
        print("thanks for using this functon")
    return mfx


@greet
def hello():
    print("hello world")


hello()
# greet(hello)()