def basic_operations(num1,num2):
    print("1. for addition")
    print("2. for subtraction")
    print("3. for multiplication")
    print("4. for division")
    operation = int(input("enter the operation: "))
    result = None
    if operation==1:
        result = num1+num2
    elif operation==2:
        result = num1-num2
    elif operation==3:
        result = num1*num2
    elif operation==4:
        if num2==0:
            print("undefined")
        else:
            result = num1/num2
    else:
        print("invalid operation")
    return{
        "num1": num1,
        "num2": num2,
        "result": result
    }
#operation_result = basic_operations(4,6)
#print(operation_result)

def power_operation(base, exponent, **kwargs):
    if 'modulo' in kwargs :
        result = pow(base, exponent, kwargs['modulo'])
    else:
        result = pow(base,exponent)
    return {"result": result}
