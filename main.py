def getInput():
    print("Enter the equation")
    calculation = input()
    return calculation

def parseExpression(calculation):
    expression = []
    for element in calculation:
        if expression.__len__() == 0:
            expression.append(element)
        elif expression[-1].isnumeric():
            if element.isdigit():
                lastEl = expression.pop()
                number = lastEl + element
                expression.append(number)
            else:
                expression.append(element)
        else:
            expression.append(element)

    return expression

def precedence(element):

    if element == "^":
        return 3
    elif element == "*" or element == "/":
        return 2
    elif element == "+" or element == "-":
        return 1
    else:
        return -1

def convertToPostFix(expression):
    stack = ["#"]
    postfixExpression = []
    for element in expression:
        if element.isnumeric():
            postfixExpression.append(element)

        elif element == "(":
            stack.append(element)

        elif element == ")":
            while stack[-1] != "(" :
                postfixExpression.append(stack.pop())
            stack.pop()

        else:
            if precedence(stack[-1])  >= precedence(element):
                while precedence(stack[-1]) >= precedence(element):
                    postfixExpression.append(stack.pop())
                stack.append(element)
            else:
                stack.append(element)

    while stack[-1] != "#":
        postfixExpression.append(stack.pop())

    return postfixExpression

def strToNum(postfixExpression):
    for i in range(0,postfixExpression.__len__()):
        if postfixExpression[i].isnumeric():
            postfixExpression[i] = int(postfixExpression[i])
    return postfixExpression

def solveExpression(num1,num2,operation):
    if operation == "^":
        return num1**num2
    if operation == "*":
        return num1*num2
    if operation == "/":
        return num1/num2
    if operation == "+":
        return num1+num2
    if operation == "-":
        return num1-num2


def solve(postfixExpression):
    i=0
    while i < postfixExpression.__len__():
        if type(postfixExpression[i]) != int:
            postfixExpression[i-2] = solveExpression(postfixExpression[i-2],postfixExpression[i-1],postfixExpression[i])
            postfixExpression.pop(i)
            postfixExpression.pop(i-1)
            i = i -2
        i +=1
    return postfixExpression

def main():
    calculation = getInput()
    expression = parseExpression(calculation)
    postfixExpression = convertToPostFix(expression)
    postfixExpression = strToNum(postfixExpression)
    print(solve(postfixExpression))

main()
