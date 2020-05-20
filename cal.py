#!/usr/bin/python
# calc.py
# BiYing Pan
# 05.10.18
# This program is to create a calculator that parses an infix expression into postix, then evaluates it


import sys


class Stack:

    # empty stack
    def __init__(self):
        self.s = []

    # display the stack
    def __str__(self):
        return str(self.s)

    # add a new element to top of stack
    def push(self, x):
        self.s.append(x)

    # remove the top elment from stack
    def pop(self):
        return self.s.pop()

    # empty the stack
    def isEmpty(self):
        return self.s == []

    # see what elment is on the top of stack
    def top(self):
        return self.s[-1]

# the precedence of the operators


def precedence(op):
    if op == "(" or op == ")":
        return 1
    if op == "+" or op == "-":
        return 2

    if op == "*" or op == "/" or op == "%":
        return 3


# infix to postfix
def infix2postfix(exp):
    stack = Stack()
    postfix = []
    infix = exp.split()

    for op in infix:
        # if it is a left (, push it to the stack
        if (op == "("):
            stack.push(op)

        elif (op == ")"):
            # pop operators from the stack
            top = stack.pop()

            while (top != "("):
                # append to the postfix
                postfix.append(top)
                top = stack.pop()

        elif (op.isdigit()):
            # append int to the postfix
            postfix.append(op)

        else:
            p = precedence(op)
            # an operator is encountered

            while not stack.isEmpty() and p <= precedence(stack.top()):
                postfix.append(stack.pop())
            stack.push(op)

    while not stack.isEmpty():
        postfix.append(stack.pop())

    return " ".join(postfix)


# evalPostfix
def evalPostfix(exp):
    stack = Stack()
    token = exp.split()

    for op in token:
        if (op.isdigit()):
            stack.push(op)

        else:
            # op1 and op2
            op2 = int(stack.pop())
            op1 = int(stack.pop())

            # cal and push result
            if (op == "+"):
                stack.push(op1 + op2)
            if (op == "-"):
                stack.push(op1 - op2)
            if (op == "*"):
                stack.push(op1 * op2)
            if (op == "/"):
                stack.push(op1 / op2)
            if (op == "%"):
                stack.push(op1 % op2)

    # print result
    print"".join(exp), "=", stack.pop()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        # read stdin
        f = sys.stdin
        # read 120 char each line
        char = f.read(120)
        while char:
            postfix = infix2postfix(char)
            evalPostfix(postfix)
            char = f.read(120)

        f.close()

    else:
        # read file
        f = open(sys.argv[1])

        for l in f:
            lines = l.strip()

            # call infix2postfix() to get postfix
            postfix = infix2postfix(l)
            # call evalPostfix() to get result
            evalPostfix(postfix)

        f.close()
