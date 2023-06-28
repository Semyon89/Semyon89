# def strcounter(s):
#     syms_counter = {}
#     for sym in s:
#         syms_counter[sum] =  syms_counter.get(sym, 0) +1
#
#         print(syms_counter)
#
# strcounter('aaaabca')


def palindrome(s):
    return s[::-1] == s

while True:

    s = input("введите слово: ")
    print(f"{s} это слово является палиндромом" if
palindrome (s) else "это слово не является палиндромом")