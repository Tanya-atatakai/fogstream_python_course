# coding=utf-8
import re

print(re.search('[abc]', 'Mark'))
print('Mark became ', re.sub('[abc]', 'o', 'Mark'))
print('rock became ', re.sub('[abc]', 'o', 'rock'))
print('caps became ', re.sub('[abc]', 'o', 'caps'))

print(re.sub('y$', 'ies', 'vacancy'))  # 'vacancies'
print(re.sub('y$', 'ies', 'agency'))  # 'agencies'
print(re.sub('([^aeiou])y$', r'\1ies', 'vacancy'))
