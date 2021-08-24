class Document:
    def __init__(self, word, count):
        self.word = word
        self.count = count
class GoogleSuggestion:
    # @param {Document} value is a document and value have two attributes(word and count)
    def mapper(self, value):
        # Write your code here
        # Please use 'yield key, value' here
        # key is prefix and value is document
        words = value.word
        key = ""
        for word in words:
            key += word
            my_value = Document(words,value.count)
            yield key, my_value


    # @param key is from mapper
    # @param values is a list of document
    def reducer(self, key, values):
        # Write your code here
        # Please use 'yield key, value' here
        # key is prefix, value is ordered list of document
        values = sorted(values,key=lambda x:(-x.count,x.word))
        index = 0
        list_len = len(values)
        if len(values) > 10 :
            list_len = 10
        results = values[:list_len]
        yield key,results

s = GoogleSuggestion()
d1 = Document('apple', 100)
d2 = Document('app', 1200)
d3 = Document('app store', 1200)
values = [("apple",100), ("app",1200), ("app store",1200)]
values = sorted(values,key=lambda x:(-x[1],x[0]))
print(values)
# for k, v in s.mapper(d1):
#     for keys, res in s.reducer(k, value):
#         print(keys, res)
