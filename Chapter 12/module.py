def myFunc():
    print("This is a function in module.py")
    

if __name__ == "__main__":
    # If this code is directly executed by running the file its present in
    print("We are directly running this code")
    myFunc()
    print(__name__ )