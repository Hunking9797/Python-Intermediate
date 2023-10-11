# important collections Counter, deque

from collections import Counter
from collections import deque

my_str = "hello everyone this is python"
c = Counter(my_str)
print(c.most_common(1)[0][0])
print(c.total())

d = deque() # double ended queue
d.append(1)
d.append(2)
d.appendleft(3)
# can popleft and simple pop
d.extendleft([9,8,7,6])
print(d)
print(d.count(1))

# default rotate is one step towards right
d.rotate(-1)
print(d)