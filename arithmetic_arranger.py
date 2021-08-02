def arranged_problems(a,b,c,d,e): 
#     Output:
# ```
#   32         1      9999      523
# +  8    - 3801    + 9999    -  49
# ----    ------    ------    -----
#   40     -3800     19998      474
# ```
    a_first_digit, a_operator, a_second_digit = a
    b_first_digit, b_operator, b_second_digit = b
    c_first_digit, c_operator, c_second_digit = c
    d_first_digit, d_operator, d_second_digit = d
 
    #getting the biggest length
    a_get_biggest_length =(lambda a,b : len(a) if(len(a) > len(b)) else len(b))(a_first_digit,a_second_digit)
    b_get_biggest_length =(lambda a,b : len(a) if(len(a) > len(b)) else len(b))(b_first_digit,b_second_digit)
    c_get_biggest_length =(lambda a,b : len(a) if(len(a) > len(b)) else len(b))(c_first_digit,c_second_digit)
    d_get_biggest_length =(lambda a,b : len(a) if(len(a) > len(b)) else len(b))(d_first_digit,d_second_digit)
    
    #creating the dashes that will be down of the operation
    a_dashes = "-"*(a_get_biggest_length+2)
    b_dashes = "-"*(b_get_biggest_length+2)
    c_dashes = "-"*(c_get_biggest_length+2)
    d_dashes = "-"*(d_get_biggest_length+2)

    #getting the solution
    a_solution = str((lambda a,b: int(a)+int(b) if(a_operator == "+") else int(a)-int(b))(a_first_digit,a_second_digit))
    b_solution = str((lambda a,b: int(a)+int(b) if(b_operator == "+") else int(a)-int(b))(b_first_digit,b_second_digit))
    c_solution = str((lambda a,b: int(a)+int(b) if(c_operator == "+") else int(a)-int(b))(c_first_digit,c_second_digit))
    d_solution = str((lambda a,b: int(a)+int(b) if(d_operator == "+") else int(a)-int(b))(d_first_digit,d_second_digit))

    #printing the first digit
    print(" "*2 + " "*(a_get_biggest_length-len(a_first_digit)) + a_first_digit + " "*4 + " "*2 + " "*(b_get_biggest_length-len(b_first_digit)) + b_first_digit + " "*4 + " "*2 + " "*(c_get_biggest_length-len(c_first_digit)) + c_first_digit + " "*4 + " "*2 + " "*(d_get_biggest_length-len(d_first_digit)) + d_first_digit)

    #printint the operator with the second digit
    print(a_operator + " " + " "*(a_get_biggest_length-len(a_second_digit)) + a_second_digit + " "*4 + b_operator + " " + " "*(b_get_biggest_length-len(b_second_digit)) + b_second_digit + " "*4 + c_operator + " " + " "*(c_get_biggest_length-len(c_second_digit)) + c_second_digit + " "*4 + d_operator + " " + " "*(d_get_biggest_length-len(d_second_digit)) + d_second_digit)

    #printing the dashes
    print(a_dashes + " "*4 + b_dashes + " "*4 + c_dashes + " "*4 + d_dashes)
    
    #outputing the solution if e is set to true
    if(e is True):
        print(" "*((a_get_biggest_length+2)-len(a_solution)) + a_solution + " "*4 + " "*((b_get_biggest_length+2)-len(b_solution)) + b_solution + " "*4 + " "*((c_get_biggest_length+2)-len(c_solution)) + c_solution +  " "*4 + " "*((d_get_biggest_length+2)-len(d_solution)) + d_solution)

def arithmetic_arranger(problems,solve=False):
    class Error():
        def test_too_many_problems(self):#checking if the problem entered is more than 4
            if(len(problems) > 4): return True
            return False

        def test_incorrect_operator(self):#checking if the operator entered in any of the operation is not (+ or -)
            test_incorrect_operator = False
            for i in problems:
                operator = i.split()[1]#getting the operator
                if((operator != "+") and (operator != "-")):
                        test_incorrect_operator = True
            return test_incorrect_operator

        def test_only_digits(self):#check if the operation contain only digit
            for i in problems:
                first_digit, operator, second_digit = i.split()
                if(not(first_digit.isdigit()) or not(second_digit.isdigit())):
                    return True
            return False
        def test_too_many_digits(self):
            for i in problems:
                first_digit, operator, second_digit = i.split()
                if(len(first_digit) > 4 or len(second_digit) > 4):
                    return True
            return False

    first_problem =  problems[0].split()
    second_problem = problems[1].split()
    third_problem =  problems[2].split()
    fourth_problem = problems[3].split()
    getError = Error()
    if(getError.test_too_many_problems() ) :
        return "Error: Too many problems."
    elif(getError.test_incorrect_operator()):
        return "Error: Operator must be '+' or '-'."
    elif(getError.test_only_digits()):
        return "Error: Numbers must only contain digits."
    elif(getError.test_too_many_digits()):
        return "Error: Numbers cannot be more than four digits."
    else:
        return arranged_problems(first_problem,second_problem,third_problem,fourth_problem,solve)