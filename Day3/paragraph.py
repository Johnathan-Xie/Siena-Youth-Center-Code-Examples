class Paragraph:
    def __init__(self, text):
        self.text = text
        self.words = text.translate({'.': ''}).split(' ')
    
    def __getitem__(self, idx):
        return self.words[idx]
    
    def num_of_word(self, word):
        return sum([i == word for i in self.words])
    
    def __add__(self, o):
        return Paragraph(self.text + ' ' + o.text)
    
    def word_count_dict(self):
        out = {i:0 for i in set(self.words)}
        for i in self.words:
            out[i] += 1
        return out
        #return {word: self.num_of_word(word) for word in set(self.words)}

if __name__ == '__main__':
    par = Paragraph('''Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together.''')
    print(par.words)
    print(par[5])
    print(par.num_of_word('as'))
    print((Paragraph('I think') + par).text)
    #print(par.word_count_dict())