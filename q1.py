def longest_palindrome(s):
    n = len(s)
    best_start = 0
    best_len = 0

    def expand(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1  

    for i in range(n):
        
        l1, r1 = expand(i, i)
        len1 = r1 - l1 + 1

        if len1 > best_len or (len1 == best_len and l1 < best_start):
            best_start = l1
            best_len = len1

        
        l2, r2 = expand(i, i + 1)
        len2 = r2 - l2 + 1

        if len2 > best_len or (len2 == best_len and l2 < best_start):
            best_start = l2
            best_len = len2

    if best_len < 2:
        return ""

    return s[best_start:best_start + best_len]