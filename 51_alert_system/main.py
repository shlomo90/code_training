#-*- encoding: utf-8 -*-

import TimeServer
import sys

'''
외부 서비스를 사용하는 것도 한가지 방법이지만, 자신만의 서비스를
만들어 다른 사람들이 소비하도록 만드는 것은 다른 개발자들이
여러분이 제공하는 서비스를 사용하고 싶어하도록 만들 수 있다는 점이
중요하다.

  현재 시각을 JSON 데이터로 알려주는 간단한 웹 서비스를 만들어보자.
이때 제공하는 데이터 형식은 다음과 같다.
{"currentTime": "2050-01-24 15:06:26}

그리고 클라이언트 애플리케이션을 작성하여 웹 서비스에 접속하고 결과를
파싱한 다음 현재 시각을 출력하자.

출력 예
The current time is 15:06:26 UTC January 4 2050.

제약 조건
* 서버 애플리케이션은 요청에 대한 응답을 전송할 때 콘텐트 타입을 반드시
  application/json으로 할 것

* 최소한의 코드를 사용하여 서버 애플리케이션을 제작할 것

도전 과제
* 무작위의 내용을 보내는 새로운 서버를 하나 만들어보자. 이를 위해 여러
  문구를 배열에 저장한 다음 무작위로 하나를 선택하도록 한다.

* 클라이언트 쪽에서 서버로부터 받은 문구를 출력하기 위해 서버에서 사용한
  언어와 다른 언어로 클라이언트 프로그램을 작성하라.
'''


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("please input action! (start, stop, restart)")
        sys.exit(1)
    else:
        action = sys.argv[1]

    if action == "start":
        print("TimeServer started!")
        t = TimeServer.TimeServer()
        t.init()
        t.run()
    elif action == "stop":
        print("TimeServer stopped")
        t.stop()
    elif action == "restart":
        print("TimeServer restarted")
        t.stop()
        t.init()
        t.run()
    else:
        print("not implemented")
        sys.exit(2)
