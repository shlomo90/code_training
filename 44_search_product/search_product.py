#-*- encoding:utf-8 -*-

import json

'''
파일에서 데이터를 추출한 다음 복잡한 자료 구조에 넣는 것은 파싱을 더 단순하게
만든다. 많은 프로그래밍 언어가 JSON 형식을 지원하는데, JSON은 데이터를 표현하는
인기있는 방법이다.

  제품 이름을 입력 받아 제품 이름에 해당하는 현재 가격과 수량을 조회하는
프로그램을 작성하라. 제품 데이터는 데이터 파일에 JSON 형태로 저장되는데,
그 형식은 다음과 같다.

{
  "products" : [
    {"name": "Widget", "price": 25.00, "quantity": 5 },
    {"name": "Thing", "price": 15.00, "quantity": 5 },
    {"name": "Doodad", "price": 5.00, "quantity": 10 }
  ]
}


제품을 찾는 경우에는 제품 이름, 가격 수량을 출력하고, 제품을 찾지 못하는 경우
에는 제품이 없다는 문구를 출력해보자.

출력 예
What is the product name? iPad
Sorry, that product was not found in our inventory.
What is the product name? Widget
Name: Widget
Price: $25.00
Quantity on hand: 5

제약 조건
* 이 파일은 JSON 형식을 취하고 있으므로, JSON 파서를 이용하여 파일의 내용을
  가져오도록 구현할 것
* 검색된 내용이 없을 때는 다시 입력을 받도록 구현할 것

도전 과제
* 제품 검색 시 대소문자를 구분하지 않도록 프로그램을 수정해보자.
* 제품 검색에 실패하였을 때, 검색한 제품을 추가할 것인지를 질문하도록 하자.
  만일, yes라고 대답한다면, 가격과 수량을 추가로 입력 받은 다음 JSON 파일에
  저장한다. 이때 새로 추가하는 제품 정보는 프로그램을 재시작 하지 않고도 조회가
  가능해야 한다.

'''
'''
Class JSON.
    variable:
        key
        fpath


    function:
        write_json(file)
        update_json()
        parser()


'''

class Products(object):
    def __init__(self, fpath):
        self.file_path = fpath
        self.obj = self._parse_json()
        for name, _ in self.obj.iteritems():
            self.name = name
            break

    def _parse_json(self):
        with open(self.file_path, "r") as f:
            obj = json.load(f)

        return obj

    def write_json(self):
        json_data = json.dumps(self.obj)

        with open(self.file_path, "w") as f:
            f.write(json_data)

    def search(self, name, opt=''):
        options = list(opt)
        if 'i' in options:
            name = name.lower()

        l = self.obj[self.name]
        for dic in l:
            if dic['name'] == name:
                return dic

        print "Sorry, that product was not found in our inventory."
        ans = raw_input("Would you like add the product? ")

        if ans in ['yes', 'y']:
            name = raw_input("name: ")
            price = raw_input("price: ")
            quantity = raw_input("quantity: ")

            #TODO: 하드코딩이지만, 파일에서 읽어서 쓸수 있도록 하자.
            ret = {"name": name, "price": price, "quantity": quantity}
            self.obj[self.name].append(ret)
            self.write_json()
        return False

if __name__ == "__main__":
    p = Products("./sample.json")

    while(True):
        pname = raw_input("What is the product name? ")
        ret = p.search(pname, 'i')
        if ret:
            #TODO: 하드코딩 하지 않도록 하자.
            print "Name: {}".format(ret['name'])
            print "Price: {}".format(ret['price'])
            print "Quantity: {}".format(ret['quantity'])
