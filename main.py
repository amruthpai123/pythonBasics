# import the py file to call the functions from that file
import OOPS
import argparse
import Exceptions
import GifcreationusingPIL
import OOPS.classwithgetterandsetter
import OOPS.classmethods
import Packages
# import Packages
import commandLineArguments
import customExceptions
import fileInputOutputOperations
import formatStringNumber
import generatorsfunctions
import helloFunctionsInput
import leapYear
import libraries
import loops2
import patterns
import regularExpression
import texttospeech
import typeConversion
import sys

import test_leapYear
import unpacking
from OOPS import oopstestingprograms
from OOPS import inheritanceclass
from OOPS import operatorOverloading
from OOPS import typehint
# class fewArgumentException(Exception):
#     def __init__(self,message):
#         super().__init__('too few arguments'+ message)

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
    # var1 = int(input('value of variable 1'))
    # var1 = str(input('value of variable 1'))
    # var1 = int(input('value of variable 1'))
    # typeConversion.allTypeConversion(var1)


    # Change number formats
    # formatStringNumber.changeNumberFormat()
    # patterns.patternPyramid(3)
    # patterns.stringPatter("ABCDEFGHIJKLMNOPQRSTUVWXYZ",3)
    # patterns.matPattern(11,33)
    # patterns.aphabeticRangoli(3)
    # loops2.loops2()
    # print('hello')
    # Exceptions.exceptionTestcases()
    # customExceptions.exception234()
    # libraries.randomFunctions()


    # command line arguments usage
    # try:
    #     if len(sys.argv)<=2:
    #         raise fewArgumentException('')
    #
    #     else:
    #         commandLineArguments.commandLine(sys.argv[2])
    # except fewArgumentException as e:
    #     print(e)

    # list1=[]
    # for arg in sys.argv:
    #     list1.append(arg)
    # print(list1[::-1])

    #argparse
    # parser = argparse.ArgumentParser()
    # parser.add_argument("-n",default=1,help='number of times meow',type=int)
    # parser.add_argument("-f",help="file name",type=str)
    # arg=parser.parse_args()
    # for _ in range(arg.n):
    #     print("meow")
    # print(arg.f)





    #Packages
    # using packages and API's
    # Packages.packagesExperiment(sys.argv)


    # unit testing
    # test_leapYear.unitTestcase()


    # file i/o
    # fileInputOutputOperations.fileiooperations()



    #gif creation
    # GifcreationusingPIL.gifcreation(sys.argv)


    #Regular expression
    # regularExpression.regularExpressionex()
    # regularExpression.reformatdata()
    # regularExpression.extractinformation()


    #oops
    # oopstestingprograms.testing()
    # OOPS.classwithgetterandsetter.classworks()
    # OOPS.classmethods.methodsinclass()
    # OOPS.inheritanceclass.infunction()
    # OOPS.operatorOverloading.operatorOverloading()


    #type hint
    # number :int=int(input())
    # print(OOPS.typehint.typehintopeationfunction((number)))


    #unpacking variables
    # unpacking.unpacking123()
    # name=["amruth", "akshath", "sharath"]
    # names=[{"name":"amruth","address":"telegana","salary":200},
    #        {"name": "akshath", "address": "chennail", "salary": 300},
    #        {"name": "sharath", "address": "kerala", "salary": 400},
    #        {"name": "subu", "address": "bangalore", "salary": 200},
    #        {"name": "chiranth", "address": "delhi", "salary": 300}
    #        ]
    # unpacking.func(*names)

    # parser=argparse.ArgumentParser()
    # parser.add_argument("-n",help='number of sheeps',default=1,type=int)
    # arg=parser.parse_args()
    # generatorsfunctions.genfunctions(arg.n)
    # parser=argparse.ArgumentParser()
    # parser.add_argument("-n",help="number of elements",type=int)
    # parser.add_argument("-he",help='help in instructions',type=str)
    # arg=parser.parse_args()
    # print(arg.he)
    texttospeech.texttospeech()
