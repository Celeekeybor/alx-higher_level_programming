#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import hidden_4

    names = dir(hidden_4)
    for name in range(0, len(names)):
        if names[name][:2] != "__":
            print("{}" .format(names[name]))
