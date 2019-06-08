#python problem 1.
'''
출력 예

What is your name? Brian
Hello, Brian. nice to meet you!

제약조건
* 입력 부분, 문자열 연결 부분, 출력 부분을 별도로 작성한다.

도전과제
* 변수를 사용하지 않는 새로운 버전을 작성하라.
* 사람들마다 서로 다른 인사말이 나타나도록 프로그램을 작성하라.
'''

# input part
name = raw_input("what is your name? ")

# concat strings part
msg = 'Hello, ' + name + '. nice to meet you!'

# print string part
print(msg)
