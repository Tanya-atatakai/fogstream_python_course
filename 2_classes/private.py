# coding=utf-8

import re

my_regexp = r'.+(df 1)?.+'
aaa = re.match(my_regexp, 'asdf 123')
print (aaa)

