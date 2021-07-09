def paragraph_count(paragraph):
    line_count = 1
    word_count = 0
    delim_count = 0
    delim = set([' ', '.', ',', '!', '?'])
    linec = set(['\n'])
    for line in paragraph:
        linecom = set(line)
        compare = set(line)
        line_count += len(linecom.intersection(linec))
        delim_count += len(compare.intersection(delim))
        line = line.split()
        word_count += len(line)
    print("line_count: %d, delim_count: %d, word_count: %d"%(line_count, delim_count, word_count))