#!/usr/bin/python3
for n1 in range(0, 10):
    for n2 in range(n1 + 1, 10):
        print("{:d}{:d}".format(n1, n2),
              end='\n' if n1 == 8 and n1 + 1 == 9 else ', ')
