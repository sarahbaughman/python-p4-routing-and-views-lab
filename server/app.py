#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    # print (f'{parameter}')
    print(parameter)
    # return f'{parameter}'
    return parameter

@app.route('/count/<int:number>')
def count(number):
    count = f''
    for n in range(number):
        count += f'{n}\n' 
    #     # /n is what creates the line break, if  you swap it out with anything else,
    #     # even another number it doesn't work, stays in one line 
    return count

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == '/':
        return str(num1 / num2)
    else:
        return "Looks like you didn't use the right operator in your URL."


if __name__ == '__main__':
    app.run(port=5555, debug=True)