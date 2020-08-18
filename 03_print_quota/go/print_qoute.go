/*
# problem 3 print quotation mark.
#-*- encoding: utf-8 -*-
'''
출력 예
What is the quote? There aren't the droids you're looking for
Who said it? Obi-wan Kenobi
Obi-Wan Kenobi says, "There aren't the droids you're looking for."

제약 조건
* (V) 한 개의 출력문만 사용하여 결과를 출력할 것. 이때 따옴표를 출력하기 위해
적절한 확장문자를 사용해야한다.
* (V) 만일 사용하는 프로그래밍 언언가 문자열 보간이나, 문자열 대체를 지원하는
경우라도 이 기능들을 사용하지 말고 그냥 문자열 연결을 사용할 것.
'''
*/

package main

import (
	"bytes"
	"fmt"
)

func main() {
	/* bytes.Buffer is for concatenating strings with better performance. */
	var b bytes.Buffer
	b.WriteString("What is the quote? There aren't the droids you're looking for\n")
	b.WriteString("Who said it? Obi-wan Kenobi\n")
	b.WriteString("Obi-Wan Kenobi says, \"There aren't the droids you're looking for.\"\n")
	/* Print All string */
	fmt.Printf("%s", b.String())
}
