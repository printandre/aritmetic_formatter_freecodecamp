import re
from formatting import formatter, calculate

def arithmetic_arranger(problems, value = False):
  #first, look if the list have more than 5 problems
  if len(problems) > 5:
    return "Error: Too many problems."
  
  arranged_problems = list()
  for problem in problems:
    #Second, look if there are  * or / operators (if not, index is -1)
    if problem.find("*") != -1 or problem.find("/") != -1:
      return "Error: Operator must be '+' or '-'."
      break
    #Third, look if there are characters different tham integers, "+", "-" or "s = white spaces"
    elif re.search(r'[^0-9\+\-\s]', problem):
        return "Error: Numbers must only contain digits."
        break
    else:
      part = problem.split(" ")
      #fourth, look if there are numbers > 4 digits (0 and 2 substrings)
      if len(part[0]) > 4 or len(part[2]) > 4:
        return "Error: Numbers cannot be more than four digits."
        break
      else:
        if value == True:
          formatted_lines = formatter(part[0], part[1], part[2], calculate(part[0], part[1], part[2]))
          # Concatenate the lines from each formatted problem
        else:
           formatted_lines = formatter(part[0], part[1], part[2], None)
        arranged_problems.append(formatted_lines)

  combined_lines = ""
  # Print the arranged problems in the same line
  for i in range(len(arranged_problems[0])): #index 0 for seeing the elements inside the list
      for problem_lines in arranged_problems:
        combined_lines += problem_lines[i] + "    "
      combined_lines += "\n"
    
  return combined_lines