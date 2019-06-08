#-*- encoding:utf-8 -*-
'''
사용자로 하여금 https:/goo.gl 처럼 긴 url 을 입력 받아 축약한 형태의 url을
만드는 웹 에플리케이션을 작성하라.

* 프로그램은 긴 url을 받을 수 있는 양식을 가지고 있어야 한다.
* 프로그램은 /abc12234와 같은 축약된 형태의 url을 생성하여 짧은 url과 긴 url을
  지속되는 데이터 저장소에 함께 저장해야 한다.
* 짧은 url을 입력받으면 프로그램은 긴 url로 이동시켜야 한다.
* 프로그램은 짧은 url을 사용한 횟수를 기록해야 한다.
* 프로그램은 /abc1234/stats 와 같은 짧은 url을 위한 통계 페이지를 제공한다.
  그래서 이 통계 페이지는 짧은 url 및 긴 url과 함께 짧은 url이 사용된 횟수를
  보여준다.

 제약 조건
* 이 앱은 반드시 지속적으로 유지되는 데이터 저장소를 사용하여 다른 사람들도
  사용할 수 있도록 해야한다. 즉, 로컬 시스템이나 인메모리 시스템을 사용하면
  안된다.
* 유요하지 않은 url이 입력되지 않도록 한다.

도전 과제
* 중복된 url을 탐지하도록 하라.
  즉, 이미 짧은 url이 존재하는 긴 url에 대해 짧은 url을 추가로 생성하면 안된다.
* 데이터 저장소로 Redis를 사용하라.
    download: http://download.redis.io/releases/redis-4.0.11.tar.gz
* 데이터 저장소로 RavenDB를 사용하라.
* 짧은 url이 사용될 때마다 날짜와 시각을 저장하여 통계 페이지에 접속하였을 때
  그래픽 라이브러리를 사용하여 그래프 형태로 사용횟수를 나타내도록 하라.
'''

from URLGen.URLGen import URL, ShortCutService

if __name__ == "__main__":
    url = URL(raw_input("URL: "))

    svc = ShortCutService(url=url)
    if svc.is_long_url():
        long_url = url.get_url()
        shorten_url = svc.get_shorten_url(long_url)
        if shorten_url:
            print "shorten_url {}".format(shorten_url)
        else:
            print "shorten_url {}".format(svc.generate_shorten())
    else:
        short_url = url.get_url()
        elem = svc.find_url(short_url, opt='short_url')
        if elem:
            #increase the count
            elem['count'] += 1
            svc.update(short_url, elem, opt="short_url")
        print "shorten_url {}".format(short_url)
