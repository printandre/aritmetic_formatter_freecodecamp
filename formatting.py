def calculate(a, sign, b):
    a = int(a.strip())
    sign = sign.strip()
    b = int(b.strip())

    if sign == '+':
        result = a + b
    elif sign == '-':
        result = a - b

    return result

def formatter(first_value, sign, second_value, sum = None):
    output_lines = []  # Create an empty list to store formatted lines

    format_length_1 = len(first_value)
    format_length_2 = len(second_value)

    #len grater number + space + sign
    max_index_length = max(format_length_1, format_length_2) + 2 

    #6 is the maximum due to 4 number ciphers, space and sign
    first_line = "{:>{}}".format(first_value, max_index_length) 
    output_lines.append(first_line)

    second_line = "{}{:>{}}".format(sign,second_value, (max_index_length-1)) 
    output_lines.append(second_line)

    dashes_line = "-" * (max_index_length)
    output_lines.append(dashes_line)
    
    if sum != None:
        sum_line = "{:{}}".format(sum, max_index_length)
        output_lines.append(sum_line)

    return output_lines  # Return the list of formatted lines

    return output_lines  # Return the list of formatted lines
