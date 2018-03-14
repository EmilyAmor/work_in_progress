import click

@click.command()
@click.argument('data')

def change_readnames(data):
  # read in original fastq file
  f = open(data)
  fastq = f.readlines()

  # remove new line characters
  L =[]
  for line in fastq:
    line = line.replace('\n','') # remove \n characters for accurate count
    L.append(line)

  # add "\1" to the end of the read name lines
  count = 0
  fastq_new = []
  for L[count] in L:
    if L[count].startswith("@"):
        changed_string = L[count] + "\\"  + str(ord("\x01"))
        fastq_new.append(changed_string)
    else:
        fastq_new.append(L[count])
    count += 1

    # re-add new line characters
    final = []
    for line in fastq_new:
        line += "\n"
        final.append(line)

    # write to file
    f = open('sequence_new.fq', 'w')
    f.writelines(final)
    f.close()

if __name__ == '__main__':
      change_readnames()
