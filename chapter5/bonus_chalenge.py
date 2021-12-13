def getFirstOperand() -> float:
    print("Please enter first operand: ", end="")
    return float(input())

def getSecondOperand() -> float:
    print("Please enter second operand: ", end="")
    return float(input())

def printResult(result: float):
    print("Result: %f" % result)

print("Please enter a symbol for operation: ", end="")
operation:str = input()
if operation != "+" and operation != "-" and operation != "*" and operation != "/":
    print("Operation is incorrect!")
    exit(1)

firstOperand:float = getFirstOperand()
secondOperand:float = getSecondOperand()

if operation == "+":
    printResult(firstOperand + secondOperand)
    exit(0)
if operation == "-":
    printResult(firstOperand - secondOperand)
    exit(0)
if operation == "*":
    printResult(firstOperand * secondOperand)
    exit(0)
if operation == "/":
    printResult(firstOperand / secondOperand)
    exit(0)
