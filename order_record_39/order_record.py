# -*- encoding:utf-8 -*-

'''
다음의 데이터 집합이 주어졌다고 가정하자.

Firstname   |   LastName    |   Position            |   SeparationDate
-----------------------------------------------------------------------
john        |   johnson     |   Manager             |   2016-12-31
-----------------------------------------------------------------------
Tou         |   Xiong       |   Software Engineer   |   2016-10-15
-----------------------------------------------------------------------
Michaela    |   Michaelson  |   District Manager    |   2015-12-19
-----------------------------------------------------------------------
Jake        |   Jacobson    |   Programmer          |
-----------------------------------------------------------------------
Jacquelyn   |   Jackson     |   DBA                 |
-----------------------------------------------------------------------
Sally       |   Weber       |   Web Developer       |   2015-12-18

앞의 직원 명단을 Last Name으로 정렬시킨다음, 그 결과를 표 형태로 출력하는
프로그램을 작성하라.

출력 예
Name                | Position          | Separation Date
--------------------+-------------------+-----------------
Jacquelyn Jackon    | DBA               |
Jake Jacobson       | Programmer        |
John Johnson        | Manager           | 2016-12-31
Michaela Michaelson | District Manager  | 2015-12-19
Sally Weber         | Web Developer     | 2015-12-18
Tou Xiong           | Software Engineer | 2016-10-05

제약 조건
* 맵 리스트를 사용하여 데이터를 구현할 것

도전 과제
* 어떻게 정렬시킬 것인지를 입력받도록 하라. 정렬 가능한 기준은 Separation Data,
  Position, Last Name이 있다.
* MySQL 같은 데이터베이스나 Redis 같은 키-값 저장소를 사용하여 지원 레코드를
  저장하라. 물론 데이터 저장소로부터 레코드를 조회해야 한다.

'''


class InputError(BaseException):
    pass


class Table(object):
    def __init__(self, *argv):
        self.row_list = []
        self.column_set = []
        self.ncolumn = len(argv)
        self.column_index = {}
        self.t_len = 0

        for i, k in enumerate(argv):
            column = {}
            w = len(k)
            column['c_name'] = k
            column['c_max'] = w
            column['hide'] = False
            self.t_len += w
            self.column_index[k] = i
            self.column_set.append(column)

        self.t_len += self.ncolumn  # width should consider that '|' included

    def set_elem(self, *argv):
        employ = []
        if len(argv) != self.ncolumn:
            raise InputError("Over Column")

        for i, d in enumerate(argv):
            employ.append(d)
            if len(d) > self.column_set[i]['c_max']:
                self.column_set[i]['c_max'] = len(d)

        self.row_list.append(employ)

    def print_list(self):
        ''' first line '''
        t_line = sum([int(n['c_max']) for n in self.column_set]) + self.ncolumn
        cols = [d['c_name'].ljust(d['c_max'], ' ') for d in self.column_set]
        line = '|'.join(cols)
        print(line)

        ''' border_list line '''
        cols = ['-' * d['c_max'] for d in self.column_set]
        bsort_list = '+'.join(cols)
        print(bsort_list)

        ''' data lines '''
        lines = []
        for d in self.row_list:
            cols = []
            for i, v in enumerate(d):
                max_len = self.column_set[i]['c_max']
                cols.append(v.ljust(max_len, ' '))
            line = '|'.join(cols)
            lines.append(line)
        print('\n'.join(lines))

    def sort_list(self, column):
        def _priority(e):
            i = self.column_index[column]
            return str.lower(e[i])

        new_row_list = sorted(self.row_list, key=_priority)
        self.row_list = new_row_list


if __name__ == "__main__":
    d = Table('Firstname', 'LastName', 'Position', 'SeparationDate')
    d.set_elem('John', 'johnson', 'Manager', '2016-12-31')
    d.set_elem('Tow', 'Xiong', 'Software Engineer', '2016-10-15')
    d.set_elem('Michaela', 'Michaelson', 'District Manager', '')
    d.set_elem('Jake', 'Jacobson', 'Programmer', '')
    d.set_elem('Jacquelyn', 'Jackson', 'DBA', '')
    d.set_elem('Sally', 'Weber', 'Web Developer', '2015-12-18')
    d.print_list()
    print("")
    d.sort_list('Firstname')
    d.print_list()
    print("")
    d.sort_list('LastName')
    d.print_list()
    print("")
    d.sort_list('SeparationDate')
    d.print_list()

