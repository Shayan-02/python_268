s = {"ali" : 19, "reza" : 15, "mohammad" : 20}
def deco(func):
    def inner(name):
        if name == "ali":
          print("invalid")  
        else:
            func(name)
    return inner

@deco
def A(name):
    print("score: ", s[name])
A("reza")