from app.controllers.controller import ControllerBase
from calc.calculator import Calculator
from csvmanager.read import Read
from csvmanager.write import Write
from flask import render_template, request, flash, redirect, url_for, session

filename = '/csvmanager/webcalculations.csv/'

class CalculatorController(ControllerBase):
    @staticmethod
    def post():
        if request.form['value1'] == '':
            error = 'You must enter a number for value 1'
        elif request.form['value2'] == '':
            error = 'You must enter a number for value 2'
        elif request.form['value1'] == '' and request.form['value2'] == '':
            error = 'You must enter a number for value 1 and value 2'
        else:
            Read.read_calc_history_from_df(filename)
            flash('You successfully entered numbers and calculated! Well done.')
            value1 = request.form['value1']
            value2 = request.form['value2']
            operation = request.form['operation']
            # making the tuple yo
            my_tuple = (value1, value2)
            # this will call the correct operation
            getattr(Calculator, operation)(my_tuple)
            result = str(Calculator.get_last_calc_value())
            Write.write_new_calc_to_history_df(filename, result)
            return render_template('result.html', data=Calculator.get_history(), value1=value1, value2=value2,
                                   operation=operation, result=result)
        return render_template('calculator.html', error=error)

    @staticmethod
    def get():
        return render_template('calculator.html')

    """
    The easy calculator solution
    1.  fix your calculator to read and write calculations to the csv
    2.  fix the controller to read the the csv to history first
    3.  Fix the controller to write the history to csv after you add the calculation to history
    4.  Make a method on the calculator to return the history in the format you want to print in the template

    Optional
       Fix it so that you store the type of calculation and perform the calulation at runtime, 
       so you don't store the raw result

       IF you want to be fancy you can change the delimeter for the file to semicolon and write your tuple of value to the file

       Values, Operation
       1,2,3,4; Addition
       1,2,3,4; Addition

    """
