from collections import defaultdict

def is_unique_char_with_data_structure(string):
    freq = defaultdict(int)
    for char in string:
        freq[char] += 1
    return all(freq[char] == 1 for char in string)

def is_unique_char_without_data_structure(string):
    for i in range(len(string)):
        for j in range(i):
            if string[i] == string[j]:
                return False
    return True

def reverse_string_in_place(string):
    bytes = bytearray(string)
    length = len(string)
    for i in range(length/2):
        bytes[i], bytes[length-i-1] = bytes[length-i-1], bytes[i]
    return str(bytes)

def remove_duplicate_char_in_place(string):
    if len(string) < 1:
        return string
    bytes = bytearray(string)
    tail = 1
    for i in range(1, len(bytes)):
        if all(bytes[j] != bytes[i] for j in range(tail)):
            bytes[tail] = bytes[i]
            tail += 1
    return str(bytes[:tail])

def remove_duplicate_char_with_memory(string):
    freq = {char:True for char in string}
    result = ""
    for char in string:
        if char in freq and freq[char]:
            result += char
            freq[char] = False
    return result

def is_anagram(a, b):
    freq = defaultdict(int)
    for char in a:
        freq[char] += 1
    for char in b:
        if not char in freq or freq[char] == 0:
            return False
        freq[char] -= 1
    return all(val == 0 for key, val in freq.iteritems())

def replace_space_char(string):
    result = ""
    for char in string:
        if char == " ":
            result += "%20"
        else:
            result += char
    return result

def rotate_matrix(M):
    size = len(M)
    for level in range(size/2):
        first, last = level, size-level-1
        for i in range(first, last):
            offset = i - first
            temp = M[first][i]
            M[first][i] = M[last-offset][first]
            M[last-offset][first] = M[last][last-offset]
            M[last][last-offset] = M[i][last]
            M[i][last] = temp
    return M

def set_row_and_col_zero(M):
    row, col = {}, {}
    for i in range(len(M)):
        for j in range(len(M)):
            if M[i][j] == 0:
                row[i], col[j] = True, True
    for i in row:
        for j in range(len(M)):
            M[i][j] = 0
    for j in col:
        for i in range(len(M)):
            M[i][j] = 0
    return M

def is_rotation(a, b):
    def is_substr(substr, string):
        return substr in string
    if len(a) != len(b):
        return False
    return is_substr(b, a+a)







print is_unique_char_with_data_structure("abcde")
print is_unique_char_with_data_structure("abcce")
print is_unique_char_without_data_structure("abcde")
print is_unique_char_without_data_structure("abcce")
print reverse_string_in_place("abcde")
print remove_duplicate_char_in_place("abcde")
print remove_duplicate_char_in_place("abcce")
print remove_duplicate_char_with_memory("abcde")
print remove_duplicate_char_with_memory("abcce")
print is_anagram("abcde", "edcba")
print is_anagram("abcde", "edcbaa")
print is_anagram("abcde", "fdcba")
print replace_space_char("abc def")
print rotate_matrix([[1,2],[3,4]])
print rotate_matrix([[1,2,3],[4,5,6],[7,8,9]])
print rotate_matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print set_row_and_col_zero([[1,2,0,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print set_row_and_col_zero([[1,2,0,4],[5,6,7,8],[9,0,11,12],[13,14,15,16]])
print is_rotation("apple", "pleap")







