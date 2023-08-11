if __name__ == "__name__":
    """print all the hidden files"""

    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print(name)
