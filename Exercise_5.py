# Exercise_5
class SuperStr(str):
    def is_repeatance(self, s):
        if not s or len(self) % len(s) != 0:
            return False
        if self == s * (len(self) // len(s)):
            return True
        return False

    def is_palindrom(self):
        return self.lower() == self[::-1].lower()
    