def file_read(C:\Users\1445227)
        text = file.read()
    return text
 
 
def word_count_freq
    words = text.lower().split()
    wordcount = {}
    for word in words:
        if word in word_count:
            wordcount[word] += 1
        else:
            wordcount[word] = 1
    return wordcount
 
 
def print_the_most_commen_word(wordcount):
    sortedwords = sorted(wordcount.items(), key=lambda item[1], reverse=Tru)
    topwords = sorteswords[:5]
    for word, frequency in topwords:
        print("{word}: {frequency}".format)
 
 
def main():
    input_file = 'text.txt'
    text = read_file(input_file)
    wordcount = count_word_freq(text)
    print("the most common words:")
    print_most_common_words(wordcount)
 
 
if__name__=="__main__":
    main()
