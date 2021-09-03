"""
Encode and Decode TinyURL

Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it
returns a short URL such as http://tinyurl.com/4e9iAk. Design a class to encode a URL and decode a tiny URL.

There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be
encoded to a tiny URL and the tiny URL can be decoded to the original URL.

Implement the Solution class:

Solution() Initializes the object of the system.
String encode(String longUrl) Returns a tiny URL for the given longUrl.
String decode(String shortUrl) Returns the original long URL for the given shortUrl. It is guaranteed that the given
shortUrl was encoded by the same object.


Example 1:

Input: url = "https://leetcode.com/problems/design-tinyurl"
Output: "https://leetcode.com/problems/design-tinyurl"

Explanation:
Solution obj = new Solution();
string tiny = obj.encode(url); // returns the encoded tiny url.
string ans = obj.decode(tiny); // returns the original url after deconding it.

"""
from random import randint


class Codec:
    def __init__(self):
        self.alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        self.base_url = "http://tinyurl.com/"
        self.code_meta = {}  # maintain the list of code which have been used to encode already
        self.url_data = {}  # long_url => code mapping

    def generate_code(self) -> str:
        code = []
        # possibility of 1 / 62 choose 6 * 6! = 2.26e-11 is enough to avoid easily duplication
        for i in range(6):
            code.append(self.alpha[randint(0, 61)])
        return self.base_url + "".join(code)

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        # same url shouldn't be encoded once again
        if longUrl in self.url_data:
            return self.url_data[longUrl]
        code = self.generate_code()
        # same code shouldn't be reused
        while code in self.code_meta:
            code = self.generate_code()
        self.code_meta[code] = longUrl
        self.url_data[longUrl] = code
        return code

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        if shortUrl not in self.code_meta:
            raise Exception("URL not found")
        return self.code_meta[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
