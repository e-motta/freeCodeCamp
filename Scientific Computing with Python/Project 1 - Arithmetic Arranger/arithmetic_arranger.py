def arithmetic_arranger(problems, display_answers=False):
    """Return arithmetic problems arranged vertically side-by-side.
    
    Arguments:
        problems {list} -- list of strings with arithmetic problems
        display_answers {boolean}

    Returns:
        Str
    """

    ## Separate input in lists check if input conforms to rules
    first_operands = []
    second_operands = []
    operators = []

    if len(problems) > 5:
        return 'Error: Too many problems.'

    for problem in problems:
        # Check 4 digits max
        first_operand = problem.split()[0]
        operator = problem.split()[1]
        second_operand = problem.split()[2]
        if len(first_operand) > 4 or len(second_operand) > 4:
            return 'Error: Numbers cannot be more than four digits.'
            break
        # Separate operands and check only digits
        try:
            first_operands.append(int(first_operand))
            second_operands.append(int(second_operand))
        except ValueError:
            return 'Error: Numbers must only contain digits.'
        # Separate operators
        if operator == '*' or operator == '/':
            return "Error: Operator must be '+' or '-'."
        else:
            operators.append(operator)

    ## Perform the calculation(s)
    results = []

    for count in range(len(first_operands)):
        if operators[count] == '+':
            results.append(first_operands[count] + second_operands[count])
        else:
            results.append(first_operands[count] - second_operands[count])

    ## Draw the arranged problems
    
    for count, item in enumerate(first_operands):
        if len(str(first_operands[count])) > len(str(second_operands[count])):
            max_operand_length = len(str(first_operands[count]))
        else:
            max_operand_length = len(str(second_operands[count]))
        
        if count == 0:
            first_line = '  ' + (max_operand_length - len(str(first_operands[count]))) * ' ' + str(first_operands[count])
            second_line = operators[count] + ' ' + (max_operand_length - len(str(second_operands[count]))) * ' ' + str(second_operands[count])
            third_line = '--' + max_operand_length * '-'
            fourth_line = (max_operand_length + 2 - len(str(results[count]))) * ' ' + str(results[count])
        else:
            first_line += '    ' + '  ' + (max_operand_length - len(str(first_operands[count]))) * ' ' + str(first_operands[count])
            second_line += '    ' + operators[count] + ' ' + (max_operand_length - len(str(second_operands[count]))) * ' ' + str(second_operands[count])
            third_line += '    ' + '--' + max_operand_length * '-'
            fourth_line += '    ' + (max_operand_length + 2 - len(str(results[count]))) * ' ' + str(results[count])

    arranged_problems = first_line + '\n' + second_line + '\n' + third_line

    ## Return the arranged problems

    if display_answers:
        arranged_problems += '\n' + fourth_line

    return arranged_problems
