while True:
    num1, num2 = input ('ENTER TWO VARIABLES: ').split()
    try:
        (num1, num2 ==int(num1) , int(num2))
        break
    except:
        print ('Enter a Number')
        continue
while True :
    oper = input ('give operator +,-, /,*,%: ' )
    if oper == '+':
        Add = int (num1) + int (num2)
        print ('{}+{}={}'.format(num1 , num2, Add))
        break
    elif oper == '-' :
        Subs = int(num1) - int(num2)
        print ('{}-{}={}'.format(num1 , num2, Subs))
        break
    elif oper == '*':
        multiply = int(num1) * int(num2)
        print ('{}*{}={}'.format(num1 , num2, multiply))
        break
    elif oper == '/':
        Divide = int (num1) / int(num2)
        print ('{} / {}={}'.format(num1 , num2, Divide))
        break
    elif oper == '%' :
        remaining = int(num1) % int(num2)
        print ('{} % {}={}'.format(num1 , num2, remaining))
        break
    else:
        print ('Give valid operator ')
        continue
    
input ('press a key to exit')


