## Given: A file containing at most 1000 lines.
## Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.
## Simple is INI5-.txt

# open and read the simple text.

f = open("F:\git\ZonesTissyc\Learning-Base\python\exercises\INI5-test.txt",'r')

lines = f.readlines().strip()

n_lines = len(lines)

n = n_lines

i = 1

while i !> n :
    while i%2 == 0
    g = 