class Encoder:
    def longToShort(self, url, d1, d2):
        if url in self.longURL:
            return self.longURL[url]
        shorted = self.generateShortedURL(url)
        # 防止 hash collision 重新生成一个直到没有为止
        while shorted in self.shortURL:
            shorted = self.generateShortedURL(url)
        self.longURL[url] = shorted
        self.shortURL[shorted] = url
        return shorted

    def generateShortedURL(self, url):
        import random
        shorted = ''
        for _ in range(6):
            shorted += random.choice(self.chars)
class Decoder:
      def shortToLong(self, url):
        if url in self.shortURL:
            return self.shortURL[url]
        return None
class TinyUrl:
    """
    @param: url: a long url
    @return: a short url starts with http://tiny.url/
    """
    def __init__(self, encoder, decoder):
        self.chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.longURL = {}
        # key: longURL, value: shortURL
        self.shortURL = {}
        # key: shortURL, value: longURL
        self.encoder = encoder
        self.decoder = decoder

    def get_long_to_short(self):
        pass
    def get_short_to_long(self):
        pass
    """
    @param: url: a short url starts with http://tiny.url/
    @return: a long url
    """
    def shortToLong(self, url):
        if url in self.shortURL:
            return self.shortURL[url]
        return None
    def generateShortedURL(self, url):
        import random
        shorted = ''
        for _ in range(6):
            shorted += random.choice(self.chars)
        return 'http://tiny.url/' + shorted
test = TinyUrl()

res1 = test.longToShort("http://www.lintcode.com/faq/?id=10")
print(test.shortToLong(res1))