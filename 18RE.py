#18RE.py

import re

def passwdValidationCheck(pwd):
    """
    비밀번호 유효성검사하는 함수
    비밀번호에 영문, 숫자로 6~12자리만 OK
    영문에는 반드시 대문자와 소문자가 함께 포함되어 있어야 한다.
    :param pwd:
    :return:
        True : if valid pwd
        False : if invalid pwd
    """
    if len(re.findall("^[A-Za-z0-9]{6,12}$", pwd)) ==0:
        print(pwd, "의 패턴이 잘못되었습니다.")
        return False

    if len(re.findall("[A-Z]", pwd)) == 0 or len(re.findall("[a-z]", pwd)) == 0:
        print(pwd, "는 영문 대소문자가 섞여있지 않습니다.")
        return False

    print(pwd, "는 비밀번호로 적당합니다.")
    return True


print("xxxxxxxxxxxxxxxxxxxx")

if __name__ == "__main__":
    passwdValidationCheck("abcd1234")
    passwdValidationCheck("AbCd")
    passwdValidationCheck("AbCd1234")
    passwdValidationCheck("AbCd@1223")
    passwdValidationCheck("@AbCd1223#")

"""
def checkEmailValiation(email):
    이메일 패턴 [\w.-]+@[\w.-]+\.\w+
    :param email:
    :return:
   
"""

