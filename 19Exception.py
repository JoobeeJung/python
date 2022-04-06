# 19Exception.py
import traceback


def exceptionTest():
    try:
        age = int(input("Insert Age : "))
        age = age + 1
        print("Next Year : " , age)
    except Exception as err:
        print("Exception !!!")
        traceback.print_exc()

#exceptionTest()
#exceptionTest()

def exceptionFile(path):
    try:
        fp = open(path, "r")

    except IOError:
        print("Cannot Open File : ", path)
    else:
        print("File has ", len(fp.readlines()), "lines")
        fp.close()
    finally:
        print("End of File ...")

exceptionFile("d:/test1.txt")
