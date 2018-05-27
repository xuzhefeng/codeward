def find_missing_letter(chars):
    miss_chars = []
    alpha_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    i = 0
    index_start = alpha_list.find(chars[0])
    # while i < lenght:
    for i in range(len(chars)):
        if chars[i] == alpha_list[index_start]:
            i += 1
            index_start += 1
        else:
            miss_chars.append(alpha_list[index_start])
            index_start += 1
    return " ".join(miss_chars)
chars = "abcdfhj"
print(find_missing_letter(chars))
