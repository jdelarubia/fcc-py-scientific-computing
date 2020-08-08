def arithmetic_arranger(problems: list, show_answers: bool = False) -> str:
    if len(problems) > 5:
        return "Error: Too many problems."

    line1: str = ""
    line2: str = ""
    line3: str = ""
    results: str = ""

    for i, problem in enumerate(problems):
        operand1, operation, operand2 = problem.split(" ")

        valid, message = validate(operand1, operand2, operation)
        if not valid:
            return message


        max_width = max([len(operand1), len(operand2)]) + 2

        blanks = max_width - len(operand1) - 1
        line1 += f"{' ' * blanks} {operand1}"

        blanks = max_width - len(operand2) - 2
        line2 += f"{operation} {' ' * blanks}{operand2}"

        line3 += f"{'-' * max_width}"

        op_result = operate(int(operand1), int(operand2), operation)
        blanks = max_width - len(str(op_result)) - 1
        results += f"{' ' * blanks} {op_result}"

        if i < len(problems) - 1:
            line1 += f"{' ' * 4}"
            line2 += f"{' ' * 4}"
            line3 += f"{' ' * 4}"
            results += f"{' ' * 4}"

    if show_answers:
        return "\n".join([line1, line2, line3, results])
    return "\n".join([line1, line2, line3])

def validate(operand1: int, operand2: int, operation: str) -> tuple:
    if operation not in ["+", "-"]:
        return False, "Error: Operator must be '+' or '-'."
    if len(operand1) > 4 or len(operand2) > 4:
        return False, "Error: Numbers cannot be more than four digits."
    if not operand1.isdigit() or not operand2.isdigit():
        return False, "Error: Numbers must only contain digits."
    
    return True, ""

def operate(operand1: int, operand2: int, operation: str) -> int:
    if operation == "+":
        return operand1 + operand2
    elif operation == "-":
        return operand1 - operand2
    return 0
