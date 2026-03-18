# 한 글자(알파벳) → 다음 알파벳
c = "a"
next_c = chr(ord(c) + 1)  # "b"


# z/Z는 a/A로 돌리기(랩어라운드)
def next_alpha(c: str) -> str:
    if 'a' <= c <= 'z':
        return chr((ord(c) - ord('a') + 1) % 26 + ord('a'))
    if 'A' <= c <= 'Z':
        return chr((ord(c) - ord('A') + 1) % 26 + ord('A'))
    return c  # 알파벳 아니면 그대로

print(next_alpha("a"))  # b
print(next_alpha("z"))  # a
print(next_alpha("Z"))  # A


# 문자열 전체에 적용
s = "aZz-1"
t = "".join(next_alpha(ch) for ch in s)
print(t)  # bAa-1


