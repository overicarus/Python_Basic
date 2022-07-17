#!/usr/bin/env python
# coding: utf-8

# In[21]:


print("숫자 게임 시작합니다!")
number = 62

#input은 사용자로부터 값을 입력 받기 위해서 사용된다.
#int()를 이용하여 문자열로 입력받은 값을 정수형의 숫자로 변환한다.
guess = input("1에서 100 사이의 숫자를 추측해보세요! \n기회는 단 한 번입니다! \n")
if type(guess) == int:
    guess_num = int(guess)
    if 1 <= guess_num <= 100 :
        print("입력하신 숫자는 %d 입니다."%(guess_num))
        if guess_num == number:
            print("정답입니다!")
        else:
            print("오답입니다!")
    else:
        print("정보를 잘못 입력하셨습니다.")
else:
    print("정보를 잘못 입력하셨습니다.")
        

print("게임을 종료합니다.")


# In[ ]:




