# -*- encoding: utf-8 -*-
'''
    ft 형식으로 input을 받고, 넓이를 계산한 후에,
    m 형식으로 출력을 한다.
'''

import math


def ft_to_m(feet):
    '''
    cal => m^2 = f^2 * 0.09290304
    '''
    convert = 0.09290304
    m = float(feet) * float(feet) * float(convert)
    return float(math.sqrt(m))


if __name__ == "__main__":
    ''' start '''
    length_room_ft = float(raw_input ("What is the length of the room in feet? "))
    width_room_ft = float(raw_input ("What is the width of the room in feet? "))
    area_room_ft = float(length_room_ft) * float(width_room_ft)
    area_room_m = 0.0
    length_room_m = 0.0
    width_room_m = 0.0

    print("you entered dimensions of " + str(length_room_ft) + " feet" +
           " by " + str(width_room_ft) + " feet")
    print("The area is")
    print(str(area_room_ft) + " square feet")

    # convert ft_to_m
    length_room_m = ft_to_m(length_room_ft)
    width_room_m = ft_to_m(width_room_ft)

    area_room_m = length_room_m * width_room_m
    print('{:.3f}'.format(area_room_m) + " square meters")
