if __name__ == "__main__":
    """print the number and list of arguments"""
    import sys

    counter = len(sys.argv) - 1
    if counter == 0:
        print("0 argument.")
    elif counter == 1:
        print("0 argument:")
    else:
        print("{} arguments:".format(counter))
    for i in range(counter):
        print("{}: {}".format(counter, sys.arg[i +1]))
