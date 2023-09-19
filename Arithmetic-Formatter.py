
def arithmetic_arranger(problems, answers = False):
  num1 = ""
  num2 = ""
  operator = ""
  result = ""

  top = ""
  bottom = ""
  lines = ""
  result_justified = ""
  arranged_problems = ""

  if (len(problems) >= 5):
    return "Error: Too many problems"
  elif len(problems) < 1:
    return "Error: Program requires input of at least one problem."

  for problem in problems:
    order_split = problem.split(" ")
    num1 = order_split[0]
    operator = order_split[1]
    num2 = order_split[2]

    if operator not in ("+", "-"):
      return "Error: Operator must be '+' or '-'."
    if not num1.isdigit() or not num2.isdigit():
      return "Error: Numbers must only contain digits."
    if len(num1) > 4 or len(num2) > 4:
      return "Error: Numbers cannot be more than four digits."

    lenght = max(len(num1), len(num2)) + 2
    top += str(num1.rjust(lenght)) + "    "
    bottom += operator + str(num2.rjust(lenght - 1)) + "    "
    lines += "-" * lenght + "    "

    if answers:
      if operator == "+":
        result = str(int(num1) + int(num2))
      else:
        result = str(int(num1) - int(num2))
      result_justified += result.rjust(lenght) + "    "

  arranged_problems += top + "\n"
  arranged_problems += bottom + "\n"
  arranged_problems += lines

  if answers:
    arranged_problems += "\n" + result_justified
  return arranged_problems
 
print(arithmetic_arranger(["32 + 8", "1 - 3801"], True))

                           