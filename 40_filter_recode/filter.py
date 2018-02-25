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

사용자가 입력한 글자와 First Name 필드와 Last Name 필드의 데이터를 모두 비교하여
사용자가 입력한 글자를 포함하는 모든 레코드를 출력하는 프로그램을 작성하라.


출력 예
enter a search string: Jac

Results:

Name                | Position          | Separation Date
--------------------|-------------------|-----------------
Jacquelyn Jackon    | DBA               |
Jake Jacobson       | Programmer        |


제약 조건
* 맵 배열이나 연관 배열을 사용하여 데이터를 구현할 것

도전 과제
* 글자 조회 시 대소문자를 구분하도록 프로그램을 수정해보자.
* Position을 조회하는 옵션을 추가하자.
* Separation date가 6개월 이상 된 직원을 조회하는 옵션을 추가하자.
* 데이터를 파일에서 읽도록 프로그램을 수정해보자.

'''


class InputError(BaseException):
    pass


class Table(object):
    def __init__(self, *argv):
        self.row_list = []
        self.cur_list = []
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
        for d in self.cur_list:
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

        self.cur_list = sorted(self.row_list, key=_priority)

    def filter_match(self, match, case=False):
        result = []
        for row in self.cur_list:
            for data in row:
                if case is False:
                    match = match.lower()
                    cmp_data = data.lower()
                else:
                    cmp_data = data

                if cmp_data.find(match) > -1:
                    result.append(row)
                    break
        self.cur_list = result

    def filter_col(self, column, match):
        idx = self._find_col_index(column)

        result = []
        for row in self.cur_list:
            data = row[idx]
            if data.find(match) > -1:
                result.append(row)
        self.cur_list = result

    def _find_col_index(self, column):
        for i, d in enumerate(self.column_set):
            col_name = d['c_name']
            if col_name == column:
                return i
        raise InputError("There is no Column name {}".format(column))

    def reset(self):
        self.cur_list = self.row_list


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
    d.reset()
    print("")
    d.filter_match('Jac')
    d.print_list()

    d.reset()
    print("")
    d.filter_col('Position', 'DBA')
    d.print_list()


