
import os, sys, json
from pathlib import Path
import math


DEBUG=True
unused_variable = "I am not used"


def calculate_average(numbers=[]):
    total=0
    for n in numbers:
        total+=n
    if len(numbers)==0:
        return None
    return total/len(numbers)


def greet(name):
    message = "Hello, " + name + "!"
    print(message)
    return message


class dataProcessor:
    def __init__(self, data):
        self.data=data

    def process(self):
        result=[]
        for item in self.data:
            if item > 0:
                result.append(item*2)
        return result


def read_file(filename):
    f = open(filename, "r")
    content = f.read()
    f.close()
    return content


def main():
    numbers = [1, 2, 3, 4, 5]
    avg=calculate_average(numbers)
    print("Average:",avg)

    processor=dataProcessor(numbers)
    print(processor.process())

    x = 10
    if x == 10:
        print("Ten")

    try:
        value = int("not a number")
    except:
        pass

    print("Done")


if __name__ == "__main__":
    main()
