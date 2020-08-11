/*
출력 예

What is your name? Brian
Hello, Brian. nice to meet you!

제약조건
* 입력 부분, 문자열 연결 부분, 출력 부분을 별도로 작성한다.

도전과제
* 변수를 사용하지 않는 새로운 버전을 작성하라.
* (V) 사람들마다 서로 다른 인사말이 나타나도록 프로그램을 작성하라.
*/

package main

import (
    "fmt"
)

var greeting = make(map[string]string)

// Call only once
func init() {
    greeting["jay"] = "Good to see you Jay!"
    greeting["brian"] = "Wow, Look at you Brian!"
    greeting["Jonathan"] = "What's the matter?!"
    greeting["default"] = "nice to meet you!"
}

func main() {
    var name string

    fmt.Printf("What is your name? ")
    fmt.Scanf("%s", &name)

    if greeting[name] != "" {
        fmt.Printf("Hello, %s. %s", name, greeting[name])
    } else {
        fmt.Printf("Hello, %s. %s", name, greeting["default"])
    }
}
