#-*- encoding:utf-8 -*-

'''
피트니스 프로그램을 시작할 때 보통 목표 심박수를 지정하여 운동을 과하게 하지
않도록 한다.
카르보넨 심박수 공식은 여러분의 심박수를 결정하기 위해 사용된다.
나이와 평상시의 심박수를 입력 받은 다음카르보넨 공식을 사용하여 최대 심박수의
55%에서 95%에 해당하는 심박수를 구하는 프로그램을 작성하라.
이때 출력, 예와 같이 표 형태로 출력해야 한다.

카르보넨 심박수 공식은 다음과 같다

TargetHeartRate = (((220-age) - restingHR)*intensity)+restingHR

출력 예

Resting Pulse: 65 Age: 22
Intensity   | Rate
------------------------
55%         | 138 bpm
60%         | 145 bpm
:
90%         | 185 bpm
95%         | 191 bpm


제약 조건
* 퍼센트를 하드코딩하지 말 것. 대신 루프를 사용하여 퍼센트를 55에서 95까지
  증가하게 할 것.
* 나이와 심박수는 숫자로만 받ㄷ을 수 있도록 하여 숫자가 입력될 대가지 진행되지
  않도록 할 것
* 결과는 표 형태로 출력할 것

'''

class person(object):
    def __init__(self, rp, age):
        self.rate = 0
        self.age = int(age)
        self.rp = float(rp) # Resting Pulse.

    def _get_target_heart_rate(self, intensity):
        ''' get_target_heart_rate는 사람의 나이, 심박수와 강도에 따라
        카르보넨심박수를 구한다.
        intensity: float 형으로 0 ~ 1 사이 값으로 들어온다.
        결과값: 카르보넨 심박수
        '''
        rp = float(self.rp)
        age = float(self.age)

        if not rp:
            raise ValueError("There is no RestingHR")
        if not age:
            raise ValueError("There is no Age")

        ret = (((220 - age) - rp) * intensity) + rp
        return ret

    def _make_two_column_line(self, c1, c2, delim):
        width = 14

        line1 = " {}".format(c1) + ' ' * (width - len(c1))
        line2 = " {}".format(c2) + ' ' * (width - len(c2))
        line = line2 + delim + line1
        return line

    def show_karvonen_table(self, f, t, unit):
        row_delim = '---------------------------'
        c1 = 'intensity'
        c2 = 'rate'

        line_list = []
        line_list.append(
            self._make_two_column_line(c1, c2, '|'))
        line_list.append(row_delim)

        for i in range(f, t, unit):
            c1 = str(int(self._get_target_heart_rate(float(i)/100))) + ' rpm'
            i = str(i) + '%'
            c2 = i
            line_list.append(
                self._make_two_column_line(c1, c2, '|'))
        result = "\n".join(line_list)
        print(result)


if __name__ == "__main__":
    rp = raw_input("Resting Pulse: ")
    age = raw_input("Age: ")
    tester = person(rp, age)
    tester.show_karvonen_table(f=55, t=95, unit=5)
