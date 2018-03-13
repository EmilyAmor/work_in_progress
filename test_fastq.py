#!/usr/bin/env python

import click

@click.command()
@click.argument('data')

def test_fastq(data):
  f = open(data)
  inputfile = f.readlines()

  # count characters for each line
  L = []
  for line in inputfile:
    line = line.replace('\n','') # remove \n characters for accurate count
    L.append(len(line))
  print (L)

# test if line 2 and line 4 are the same value (length) for every set of 4
  count_1 = 1
  count_2 = 3
  while count_2 <= len(L):
    if L[count_1] == L[count_2]:
        continue
    else:
        print ('error')
        print ("sequence:", (count_1+1), "quality:", (count_2+1)) # tell me which lines have the error
    count_1 += 4
    count_2 += 4


if __name__ == '__main__':
    test_fastq()
