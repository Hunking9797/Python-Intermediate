# important collections Counter, deque

from collections import Counter

my_str = "hello everyone this is python"
c = Counter(my_str)
print(c.most_common(1)[0][0])