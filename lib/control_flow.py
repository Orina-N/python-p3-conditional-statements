#!/usr/bin/env python3

def admin_login(username, password):
    if (username == 'admin' or username == 'ADMIN') and password == '12345':
        return 'Access granted'
    else:
        return 'Access denied'

def hows_the_weather(temperature):
    if temperature > 85:
        return "It's too dang hot out there!"
    elif 65 >= temperature >= 40:
        return "It's a little chilly out there!"
    elif temperature < 40:
        return "It's brisk out there!"

    return "It's perfect out there!"
    
def fizzbuzz(num):
    result = ""

    if num % 3 == 0:
        result += 'Fizz'
    if num % 5 == 0:
        result += 'Buzz'

    if result:
        return result  

    return num  

    
    
def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2

    print("Invalid operation!")
    return None
