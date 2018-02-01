# -*- encoding: utf-8 -*-

'''
두 개의 문자열을 비교하여 서로가 애너그램(anagram)인지를 검사하는 프로그램을
작성하라. 프로그램은 두 개의 문자열을 입력 받은 후 다음의 출력 예와 같이 출력
해야 한다.

출력 예
Enter two strings and I'll tell you if they are anagrams:
Enter the first string: note
Enter the second string: tone
"note" and "tone" are anagrams.

제약 조건
* isAnagram이라는 함수를 사용하여 프로그램을 작성할 것. isAnagram 함수는 두 개
  의 문자열을 인수로 받은 다음 true 또는 false를 반환한다. 이 함 수를 main
  프로그램에서 호출하도록 할 것.
* 두 단어의 길이가 같은지 확인할 것.

도전 과제
* 프로그래밍 언어에서 제공하는 기능(라이브러리 등)을 이용하지 않고 프로그램을
  작성하라. 즉, 선택, 반복 등의 로직을 사용하여 자신만의 알고리즘을 개발한다.
'''


def isAnagram(first_str, second_str):
    """ Return True or False
    >>> isAnagram(first_str="note", second_str="tone")
    True

    >>> isAnagram(first_str="hello may", second_str="ma yhelfew")
    False

    Anagram이란?
    단어들을 재배열 하거나 다시 만드는 것을 말한다.  전형적으로 기존의 글자들을
    한번씩만 사용하여 다른 단어로 재배치하는 것이다.

    ex:
    "rail safety" = "fairy tales"

    * 특징.
    모든 단어는 중복되서 사용되지않는다.
    띄어쓰기도 단어로 생각.
    반드시 모든 단어를 써야 한다.

    해결 방법.
    1. first, second로 들어온 단어를 리스트화 한다.
    2. second의 단어들을 하나씩 순회하여 first의 리스트에 해당하는 것을 삭제.
    3. 만약 값이 존재하지 않는다고 하면, anagram이 아님.
    4. 순회가 끝나고 first 리스트에 값이 존재하면 anagram이 아님.
    5. first의 값이 없어야만, anagram이다.
    """
    first_str_letters = list(first_str)
    second_str_letters = list(second_str)

    for letter in second_str_letters:
        try:
            if letter in first_str_letters:
                first_str_letters.remove(letter)
        except AttributeError:
            return False
    if first_str_letters:
        return False
    return True


if __name__ == "__main__":
    '''
    import doctest
    doctest.testmod()
    '''
    print("Enter two strings and I'll tell you if they are anagrams:")
    first = raw_input("Enter the first string: ")
    second = raw_input("Enter the second string: ")
    if isAnagram(first, second):
        print('"{}" and "{}" are anagrams.'.format(first, second))
    else:
        print('"{}" and "{}" are not anagrams.'.format(first, second))
