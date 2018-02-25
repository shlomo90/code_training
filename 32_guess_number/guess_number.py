# -*- encoding: utf-8 -*-

'''
세 단계의 난이도로 구성된 숫자 맞추기 게잉믈 만들어보자. 첫 번째 단계에서는
1 부터 10까지의 숫자를, 두 번째 단계에서는 1부터 100까지의 숫자를, 세 번째
단계에서는 1부터 1000가지의 숫자를 맞추어야 한다.
  먼저 난이도를 입력 받은 후 게임을 시작한다. 컴퓨터는 범위 내에서 무작위로
숫자를 하나 선택한 후 숫자를 맞추라고 표시한다. 플레이어가 숫자를 입력할 때마다
컴퓨터는 맞추어야 하는 숫자와 비교하여 입력한 숫자가 더 큰지 작은지를 알려준다.
또한 컴퓨터는 맞추는 횟수를 기록하여 플레이어가 숫자를 맞추었을 때 그 동안
추리한 횟수를 알려준다. 그리고는 게임을 다시 할 것인지를 묻는다.

출력 예
Let's play Guess The Number.
Pick a difficulty level (1, 2, or 3): 1
I have my number. What's your guess: 1
Too low. Guess Again: 5
Too high. Guess again: 2
You got it in 3 guesses!
Play again? n
Goodbye!

제약 조건
* 숫자가 아닌 값을 입력하지 않도록 구현할 것
* 게임이 진행되는 동안 숫자가 아닌 값을 입력할 때마다 잘못된 입력으로 카운트
  하도록 할 것.

도전 과제
* 추리한 횟수에 따라 다음과 같은 메세지를 출력할 것
    - 1회       : "You're a mind reader!"
    - 2-4회     : "Most impressive."
    - 5-6회     : "You can do better than that."
    - 7회이상   : "Better luck next time."
* 사용자가 입력한 숫자를 모두 기록하여 이미 추리했던 숫자를 다시 입력했을 때
  이를 알리도록 하라. 물론, 이 때도 추리한 횟수로 인정하여 카운트 한다.
'''

from random import *


LEVEL = {1: [1, 10], # default
         2: [1, 100],
         3: [1, 1000],
         }


class GameError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


class GameSetError(GameError):
    pass


class RangeError(GameSetError):
    pass


class GetRandomNumberError(GameSetError):
    pass


class GuessGame(object):
    def __init__(self):
        self._reset_game()

    def start_game(self):
        ret = self._set_game_config()
        if ret is False:
            return

        while (True):
            try:
                u_num = int(raw_input("I have my number. What's your guess: "))
            except ValueError:
                print("please input Number")
                continue
            break

        self._process_match_number(u_num)
        print("You got it in {} guesses!".format(len(self.u_history) + 1))
        self._evaluate_message()

        redo = raw_input("Play again? ")
        if redo in ['No', 'n', 'N']:
            return
        elif redo in ['Yes', 'y', 'Y']:
            self._reset_game()
            self.start_game()
        return

    def _reset_game(self):
        self.target_num = 0
        self.u_history = []  # the list of numbers An user already said.

    def _evaluate_message(self):
        tries = len(self.u_history) + 1

        if tries in range(1, 1):
            print("You're a mind reader!")
        elif tries in range(2, 4):
            print("Most impressive.")
        elif tries in range(5, 6):
            print("You can do better than that.")
        else:
            print("Better luck next time")

    def _get_random_number(self, level):

        if level == 1:
            ret = randint(1, 10)
        elif level == 2:
            ret = randint(1, 100)
        elif level == 3:
            ret = randint(1, 1000)
        else:
            raise RangeError("Level should be in 1~ 3")

        return ret

    def _set_game_config(self):
        print("Let's play Guess The Number.")
        while (True):
            try:
                self.level = \
                    int(raw_input("Pick a difficulty level (1, 2, or 3): "))
            except ValueError:
                print("Please Input Number")
                continue
            break
        self.target_num = self._get_random_number(self.level)

    def _process_match_number(self, u_num):
        # first number.
        while (True):
            try:
                if (u_num > self.target_num):
                    u_num = int(raw_input("Too high. Guess Again: "))
                    if u_num in self.u_history:
                        print("You already said this number")
                    self.u_history.append(u_num)
                    continue
                elif (u_num < self.target_num):
                    u_num = int(raw_input("Too low. Guess Again: "))
                    if u_num in self.u_history:
                        print("You already said this number")
                    self.u_history.append(u_num)
                    continue
                else:
                    return True
            except ValueError:
                print("please Input Number!")
                continue

    def end_game(self):
        print("Goodbye!")
        return True


if __name__ == '__main__':
    user = GuessGame()
    user.start_game()
