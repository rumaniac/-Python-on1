# input data
# show the input and the result
# if they type wrong type error message

num1 = input('enter num 1')
operator = input ('enter a math operator')
num2 = input('enter num 2')

num1 = int(num1)
num2 = int(num2)

#now to put do the function and what to show when different function is input
if operator == '+':
    print("{} + {} = {}". format(num1, num2, num1 + num2))
elif operator == '-':
    print("{} - {} = {}". format(num1, num2, num1 - num2))
elif operator == '*':
    print("{} * {} = {}". format(num1, num2, num1 * num2))
elif operator == '/':
    print("{} / {} = {}". format(num1, num2, num1 / num2))
elif operator == '%':
    print("{} % {} = {}". format(num1, num2, num1 % num2))
else:
    print('please enter a valid data or ADD, SUBS, DIV, MULTIPLY , R2mainter')
input('input a key to exit')
