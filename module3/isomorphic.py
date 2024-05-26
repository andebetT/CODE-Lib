def isIsomorphic(s, t):
    if len(s) != len(t):
        return False

    s_to_t = {}
    t_to_s = {}

    for i in range(len(s)):
        if s[i] not in s_to_t:
            s_to_t[s[i]] = t[i]
        elif s_to_t[s[i]] != t[i]:
            return False

        if t[i] not in t_to_s:
            t_to_s[t[i]] = s[i]
        elif t_to_s[t[i]] != s[i]:
            return False

    return True