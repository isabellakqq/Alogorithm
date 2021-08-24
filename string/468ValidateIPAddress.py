class Solution:
    def validIPAddress(self, IP: str) -> str:
        if IP.count('.') == 3:
            if self.is_valid4(IP):
                return "IPv4"
        if IP.count(':') == 7:
            if self.is_valid6(IP):
                return "IPv6"
        return "Neither"
    
    def is_valid4(self, IP):
        v4 = IP.split('.')
        for s in v4:
            if len(s) == 0 or len(s) > 3:
                return False
            if s[0] == '0' and len(s) != 1 or not s.isdigit() or int(s) > 255:
                return False
        return True
    
    def is_valid6(self, IP):
        hexdigits = '0123456789abcdefABCDEF'
        v6 = IP.split(':')
        for s in v6:
            if len(s) < 1 or len(s) > 4 or not all(i in hexdigits for i in s) :
                    print(all(ch in hexdigits for ch in s))
                    return False
        return True
s = Solution()
IP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
print(s.validIPAddress(IP))       