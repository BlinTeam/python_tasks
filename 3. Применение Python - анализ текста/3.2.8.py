# Вам дана последовательность строк.
# В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.

import re
import sys

pattern = r"\b(\w)(\w)(.*?)\b"

for line in sys.stdin:
    line = line.rstrip()
    x = re.findall(pattern, line)
    print(re.sub(pattern, r"\2\1\3", line, len(x)))

