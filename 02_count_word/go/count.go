/*
# problem 2. counting words
#-*- encoding:utf-8 -*-

글자 수 세기

문자열을 입력 받은 다음 입력 받은 문자열과 문자열의
글자수를 출력하는 프로그램을 작성하라.

출력 예
What is the input string? Homer
Homer has 5 characters.

제약조건
* (V) 출력 결과에는 입력 받은 문자열이 그대로 나타나도록 할 것.
* (V) 출력을 위해 하나의 출력문을 사용할 것.
* (V) 문자열의 길이를 구하기 위해 프로그래밍 언어에서 제공하는 내장 함수를 사용할 것

도전과제
* (V) 사용자가 아무 것도 입력하지 않은 채로 엔터 키를 치면 무엇이라도 입력하라는 메세지를 나타내보자.
*/

package main

import "fmt"

func main() {
	var input string

	for {
		fmt.Printf("What is the input string? ")
		fmt.Scanf("%s", &input)
		if len(input) == 0 {
			fmt.Printf("input something!\n")
		} else {
			break
		}
	}
	fmt.Printf("%s has %d characters\n", input, len(input))
}
