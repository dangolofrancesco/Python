##
# Questo programma censura le parolacce
#

def main() :
    words_file = open('bad words.txt', 'r')
    bad_words = []
    for line in words_file :
        line = line.upper().rstrip()
        bad_words.append(line)


    infile = open('input.txt', 'r')
    outfile = open('output.txt', 'w')

    line = infile.readline().rstrip().upper()
    while line != '' :
        words = line.split()
        pos = len(words) - 1
        for word in words :
            if word in bad_words :
                for ch in word :
                    outfile.write('*')
                outfile.write(' ')
            else:
                outfile.write(word + ' ')

            if word == words[-1] :
                outfile.write('\n')
        line = infile.readline().rstrip().upper()


main()
