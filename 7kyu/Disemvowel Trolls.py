def disemvowel(string_):
    vowels = 'aeiouAEIOU'
    return ''.join([i for i in string_ if i not in vowels])