def preLetterCase(s, si):
    str_l = s.lower()
    ind_si = -1
    for i in range(len(str_l)):
        if str_l[i] == si.lower():
            ind_si = i
            break
    if ind_si > -1:
        result = str_l[:ind_si] + str_l[ind_si:].upper()
    else:
        result = str_l
    return result


print(preLetterCase("CAtCHa", "a"))
print(preLetterCase("Preteen", "e"))
print(preLetterCase("You've got this", "m"))
print(preLetterCase("Keep trying", "k"))
