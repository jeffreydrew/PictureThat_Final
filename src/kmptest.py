def kmp(pattern, text):
    a = len(text)
    b = len(pattern)

    prefix_arr = lps(pattern, b)

    initial_point = []

    m = 0
    n = 0

    while m != a:

        if text[m] == pattern[n]:
            m += 1
            n += 1

        else:
            n = prefix_arr[n - 1]

        if n == b:
            initial_point.append(m - n)
            n = prefix_arr[n - 1]
        elif n == 0:
            m += 1

    return initial_point


def lps(pattern, b):
    lps = [0] * b
    n = 0
    m = 1

    while m != b:
        if pattern[m] == pattern[n]:
            n += 1
            lps[m] = n
            m += 1
        elif n != 0:
            n = lps[n - 1]
        else:
            lps[m] = 0
            m += 1

    return lps


#testing grounds
# string = "abcabcabc"
# pat = "abc"

# initial_index = kmp(pat, string)

# for i in initial_index:
#     print("Pattern is found in the string at index number", i)
