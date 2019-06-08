# -*- encoding: utf-8 -*-
'''
연습 문제 4 Mad Libs

명사, 동사, 형용사, 부사에 해당하는 단어를 입력 받은 후 여러 분이 만든 이야기에
넣어 완성된 이야기를 출력해보자.

출력 예
Enter a noun: dog
Enter a verb: walk
Enter an adjective: blue
Enter an adverb: quickly
Do you walk your blue dog quickly? That's hilarious!

제약 조건
* 이 프로그램에서는 한 개의 출력문만 사용할 것.
* 만일 사용하는 프로그래밍 언어가 문자열 보간이나 문자열 대체를 지원하는 경우,
  출력문을 만드는데 활용할 것.

도전 과제
* 입력할 수 있는 단어를 더 늘려 이야기를 확장시켜보자.
* 대답에 따라 이야기가 만들어지는 브랜칭 스토리(Branching story)를 구현해보자.

'''
import sys

dic_words = {}
total_words = ''
words = ['Do', 'you', 'verb', 'your', 'adjective', 'noun', 'adverb']
# aa = sys.stdin.readline()
dic_words['noun'] = raw_input('Enter a noun: ')
dic_words['verb'] = raw_input('Enter a verb: ')
dic_words['adjective'] = raw_input('Enter an adjective: ')
dic_words['adverb'] = raw_input('Enter an adverb: ')

for word in words:
    dic_data = dic_words.get(word)
    if (dic_data is None):
        total_words += word
    else:
        total_words += dic_data

    total_words += ' '

print(total_words)
