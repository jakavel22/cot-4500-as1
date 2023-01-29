

#1
def question_1():
    s=0

    
    exponent =10000000111
    a, i=0,0
    while(exponent !=0):
        exp=exponent %10
        a=a+exp*pow(2,i)
        exponent = exponent//10
        i+=1

    
    fraction=str(1110101110010000000000000000000000000000000000000000)
    b=0
    i=1
    for item in fraction:
        b=b+int(item)*(0.5**i)
        i+=1

    
    c=((-1)**s)*(2**(a-1023))*((1+b))
    print(c)
    print("")
    
    return
question_1()


#2
def question_2():
    s=0

    
    exponent =10000000111
    a, i=0,0
    while(exponent !=0):
        exp=exponent %10
        a=a+exp*pow(2,i)
        exponent = exponent//10
        i+=1

    
    fraction=str(1110101110010000000000000000000000000000000000000000)
    b=0
    i=1
    for item in fraction:
        b=b+int(item)*(0.5**i)
        i+=1

    
    c=((-1)**s)*(2**(a-1023))*((1+b))
    print(int(c))
    print('')
    
    return
question_2()

#
def question_3():
    s=0

    
    exponent =10000000111
    a, i=0,0
    while(exponent !=0):
        exp=exponent %10
        a=a+exp*pow(2,i)
        exponent = exponent//10
        i+=1

    
    fraction=str(1110101110010000000000000000000000000000000000000000)
    b=0
    i=1
    for item in fraction:
        b=b+int(item)*(0.5**i)
        i+=1

    
    c=((-1)**s)*(2**(a-1023))*((1+b))
    print(round(c))
    print('')
    
    return
question_3()

#4
def abs_error(precise:float, approximate:float):
    sub_operation=precise-approximate
    return abs(sub_operation)

def rel_error(precise:float, approximate:float):
    sub_operation=abs_error(precise, approximate)
    div_operation=sub_operation/precise
    return div_operation

print(abs_error(491.5625,492))
print(rel_error(491.5625,492))
print('')

#5  
        
def alternating(function_we_got: str):
    term_check = negative_exponent(function_we_got)
    return term_check
def decreasing(function_we_got: str, x: int):
    decreasing_check = True
    k = 1
    starting_val = abs(eval(function_we_got))
    for k in range(2, 100):
        result = abs(eval(function_we_got))
        #print(result)
        if starting_val <= result:
            decreasing_check = False
    return decreasing_check
def negative_exponent(function: str) -> bool:
    if "-1**k" in function:
        return True
    return False

def minimum_term(function:str, x:int, error_term:float):
    n = 0
    k = 1
    
    while(abs(eval(function))>error_term):
        n+=1
        k+=1
    print(n)

if __name__ == "__main__":
    function: str = "(-1**k) * (x**k) / (k**3)"
    x: int = 1
    check1: bool = alternating(function)
    check2: bool = decreasing(function, x)
    #print(check1 and check2)
    minimum_term(function, x, 1e-4)
print('')

    
#6
def question_6(x):
    return x*x*x - x*x + 2
def bisection(left: float, right: float, given_function: str):

    x = left
    intial_left = eval(given_function)
    x=right
    intial_right = eval(given_function)
    if intial_left * intial_right >= 0:
        print("Invalid inputs. Not on opposite sides of the function")
        return
    tolerance: float = .0001
    diff: float = right - left
   

    iteration_counter = 0
    while (diff >= tolerance and iteration_counter <= 20):
        iteration_counter += 1
        mid_point = (left + right) / 2

        evaluated_midpoint = eval(given_function)
        if evaluated_midpoint == 0.0:
            break
        

        evaluated_left_point = eval(given_function)
        
        first_conditional: bool = evaluated_left_point < 0 and evaluated_midpoint >0
        second_conditional: bool = evaluated_left_point > 0 and evaluated_midpoint < 0
        if first_conditional or second_conditional:
            right = mid_point
        else:
            left = mid_point
        
        diff = abs(right - left)
        
    return (iteration_counter)
if __name__ == "__main__":
    left = -4
    right = 7
    function_string = "x**3 + (4*(x**2)) - 10"
    Q6a = bisection(left, right, function_string)
   

def derivative(value):
    return (3 * value* value) + (8 * value)
def newton_raphson(initial_approximation: float, tolerance: float, sequence: str):
    
    iteration_counter = 0
    x = initial_approximation
    f = eval(sequence) 
    f_prime = derivative(initial_approximation)
    
    approximation: float = f / f_prime
    while(abs(approximation) >= tolerance):
        x = initial_approximation
        f = eval(sequence) 
        f_prime = derivative(initial_approximation)
        approximation = f / f_prime
        initial_approximation -= approximation
        iteration_counter += 1
    return(iteration_counter)
if __name__ == "__main__":
    initial_approximation: float = 7
    tolerance: float = .0001
    sequence: str = "x**3 + (4*(x**2)) - 10"
    Q6b = newton_raphson(initial_approximation, tolerance, sequence)
print(Q6a)
print(Q6b)