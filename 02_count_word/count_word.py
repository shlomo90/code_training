# problem 2. counting words
'''
Description
The method count() returns the number of occurrences of substring sub in
the range [start, end]. Optional arguments start and end are interpreted
as in slice notation.

Syntax
str.count(sub, start= 0,end=len(string))
Parameters
sub -- This is the substring to be searched.

start -- Search starts from this index. First character starts from 0 index.
By default search starts from 0 index.

end -- Search ends from this index. First character starts from 0 index.
By default search ends at the last index.

Return Value
Centered in a string of length width.
'''

name = raw_input('what is the input string? ')

name_len = len(name)

if(name_len == 0):
    print('input something plz')
else:
    print(name+' has '+str(name_len)+' characters.')


