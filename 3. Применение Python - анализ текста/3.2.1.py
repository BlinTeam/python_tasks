# Вам дана последовательность строк.
# Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.

import sys
for line in sys.stdin:
    line = line.rstrip()
    if line.count("cat") >= 2:
        print(line)