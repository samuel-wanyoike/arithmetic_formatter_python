import re


def arithmetic_arranger(problems, solve=False):

  if (len(problems) > 5):
    return ('error: too many problems')
  first = ''
  second = ''
  Lines = ''
  sumx = ''
  string = ''

  for problem in problems:
    if (re.search('[^\s0-9.+-]', problem)):
      if (re.search('[/]', problem) or re.search('[/]', problem)):
        return ('error: operator must be plus or sign')
      return ('error: numbers must only contain digits')

    firstNumber = problem.split(' ')[0]
    operator = problem.split(' ')[1]
    secondNumber = problem.split(' ')[2]

    if (len(firstNumber) >= 5 or len(secondNumber) >= 5):
      return ('error: number cannot have more than 5 digits')

    sum = ''

    if (operator == '+'):
      sum = str(int(firstNumber) + int(secondNumber))
    elif (operator == '-'):
      sum = str(int(firstNumber) - int(secondNumber))

    length = max(len(firstNumber), len(secondNumber)) + 2
    top = str(firstNumber).rjust(length)
    bottom = operator + str(secondNumber).rjust(length - 1)
    line = ''
    res = str(sum).rjust(length)

    for i in range(length):
      line += '-'

    if problem != problem[-1]:
      first += top + '    '
      second += bottom + '    '
      Lines += line + '    '
      sumx += res + '    '

    else:
      first += top
      second += bottom
      Lines+= line
      sumx += res

  if solve:
    string = first + '\n' + second + '\n' + Lines + '\n' + sumx
  else:
    string = first + '\n' + second + '\n' + Lines
  return string
