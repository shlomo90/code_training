#-*- encoding: utf-8 -*-

'''
복리이자를 퍼센트 단위로 받은 다음, 원리금의 총 2배가 되는데까지 걸리는 기간을
계산하는 프로그램을 작성하라.
공식은 아래와 같다.

 years = 72 / r

r: 연이율

출력 예
What is the rate of return? 0
Sorry. That's not a valid input.
What is the rate of return? ABC
Sorry. That's not a valid input.
What is the rate of return? 4
It will take 18years to double your initial investment.

제약 조건
* 0을 입력하지 않도록 할 것.
* 숫자가 아닌 값을 입력하지 않도록 할 것.
* 잘못된 입력 값을 처리하는 부분을 루프로 구현하여 유효한 값이 입력될 때 까지
  반복 시킬 것.

도전 과제
* 0을 입력했을 때는 다른 에러 메세지가 나타나도록 프로그램을 수정해보자.
'''


