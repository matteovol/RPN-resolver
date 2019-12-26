#!/usr/bin/python3

from sys import argv

class Stack:

    def __init__(self):
        self.__stack = []

    def __str__(self):
        s = ""
        for i in self.__stack:
            s += str(i) + " "
        return s

    def push(self, toPush):
        self.__stack.append(toPush)

    def pop(self):
        if len(self.__stack) == 0: return
        temp = self.__stack[-1]
        del self.__stack[-1]
        return temp

class Parser:

    def __init__(self, calc):
        self.__calc = calc
        self.__index = 0
        self.__stack = Stack()

    def parse(self):
        while not self.__index >= len(self.__calc):

            if self.isDigit(self.__calc[self.__index]):
                self.__stack.push(int(self.eat()))

            elif self.__calc[self.__index] == '+':
                nb2 = self.__stack.pop()
                nb1 = self.__stack.pop()
                self.__stack.push(nb1 + nb2)
                self.__index += 1

            elif self.__calc[self.__index] == '-':
                nb2 = self.__stack.pop()
                nb1 = self.__stack.pop()
                self.__stack.push(nb1 - nb2)
                self.__index += 1

            elif self.__calc[self.__index] == "*":
                nb2 = self.__stack.pop()
                nb1 = self.__stack.pop()
                self.__stack.push(nb1 * nb2)
                self.__index += 1

            elif self.__calc[self.__index] == "/":
                nb2 = self.__stack.pop()
                nb1 = self.__stack.pop()
                self.__stack.push(nb1 / nb2)
                self.__index += 1

            self.__index += 1
            #print(self.__calc[self.__index:])
            #print(self.__stack)

        return self.__stack.pop()

    def eat(self):
        i = self.__index
        while self.__calc[i] != ' ':
            i += 1
        temp = self.__index
        self.__index = i
        return self.__calc[temp:i]

    def isDigit(self, char):
        return ord(char) >= 48 and ord(char) <= 57

def main(args):
    if len(args) != 2:
        print("Nope")
        exit(1)
    p = Parser(args[1])
    print(p.parse())

if __name__ == "__main__":
    main(argv)
