class Paragraph:
    def __init__(self, text):
        '''make a text(just the input) and words list(text split by space, use the .split() function)'''
        pass
    def __getitem__(self, idx):
        '''return the word at idx'''
        pass
    
    def num_of_word(self, word):
        '''return the number of occurences of the given word'''
        pass
    
    def __add__(self, o):
        '''overload the __add__ function to return a new paragraph with the two texts appended(call the constructor)'''
        pass
    
    def word_count_dict(self):
        '''return a dictionary containing the number of occurences of each word, to be completed after day 5'''
        pass

if __name__ == '__main__':
    par = Paragraph('''Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together.''')
    print(par.words)
    print(par[5])
    print(par.num_of_word('as'))
    print((Paragraph('I think') + par).text)
    #print(par.word_count_dict())