# import the py file to call the functions from that file
import helloFunctionsInput
import leapYear
import typeConversion

if __name__ == '__main__':
    # print the return value from the function
    """
      multiple line comment
    """
    # Functions
    # name = helloFunctionsInput.func()

    # sting manipulation methods
    # typeConversion.stringManipulation(name)
    # escape sequence example
    # print(' hello,\n ' + name)

    # format print with f
    # print(f"hello, {name}")

    # year = input('enter year: ')
    # Function for Leap Year
    # print((leapYear.leapYear(int(year))))

    # Type Conversion
    # typeConversion.numberStringConversion('2345')

    # all Type Conversion
    var1 = float(input('value of variable 1'))
    var1 = str(input('value of variable 1'))
    var1 = int(input('value of variable 1'))
    typeConversion.allTypeConversion(var1)
