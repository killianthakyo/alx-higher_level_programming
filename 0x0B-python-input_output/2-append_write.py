#!/usr/bin/python3
def append_write(filename="", text=""):
    """
    Append and return number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return(f.write(text))
