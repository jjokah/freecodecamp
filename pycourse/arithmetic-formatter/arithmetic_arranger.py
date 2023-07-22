def arithmetic_arranger(problems, show_results=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    top = []
    bottom = []
    lines = []
    results = []
    valid_operators = ["+", "-"]

    for problem in problems:
        operand1, operator, operand2 = problem.split()

        if operator not in valid_operators:
            return "Error: Operator must be '+' or '-'."
        if not (operand1.isdigit() and operand2.isdigit()):
            return "Error: Numbers must only contain digits."
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        max_length = max(len(operand1), len(operand2))

        top.append(operand1.rjust(max_length + 2))
        bottom.append(operator + operand2.rjust(max_length + 1))
        lines.append("-" * (max_length + 2))
        results.append(str(eval(operand1 + operator + operand2)).rjust(max_length + 2))

    arranged_problems = (
        f"{'    '.join(top)}\n{'    '.join(bottom)}\n{'    '.join(lines)}"
    )

    if show_results:
        arranged_problems = f"{'    '.join(top)}\n{'    '.join(bottom)}\n{'    '.join(lines)}\n{'    '.join(results)}"

    return arranged_problems


print(
    arithmetic_arranger(
        ["32 + 6g8", "3801 - 2", "45 + 43", "123 + 49", "13 + 49"], True
    )
)
