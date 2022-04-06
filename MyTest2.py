import time
#import LG  #1번째경우  LG.py문서
#from 파일이름  import  함수이름,필드이름
from LG  import userID, userPWD, gram, star    #2째경우  LG.py문서


print('MyTest2.py 복사해서 생성한 MyTest2.py...')

time.sleep(2)

print(userID)
print(userPWD)
time.sleep(1)

print('-' * 30)
print('-' * 30)
gram()
star()

