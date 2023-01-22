try:
    x = 7 + "dave"
    print(x)
except TypeError:
    print("X is the wrong data type")
except:
    print("Something else went wrong.")