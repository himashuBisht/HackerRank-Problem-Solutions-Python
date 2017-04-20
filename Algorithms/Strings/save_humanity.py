#Author: Khaleeque Ansari

def string_match(str1, str2):

    mismatches = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            mismatches += 1
            if mismatches == 2:
                return False
    return True


if __name__ == '__main__':

    assert string_match('aba', 'aba') == True
    assert string_match('aba', 'abc') == True
    assert string_match('lba', 'lbd') == True
    assert string_match('aba', 'akf') == False

    n = int(input())
    for t in range(n):
        p, v = input().split(' ')
        len_p = len(p)
        len_v = len(v)

        outputs = []
        for j in range (len_p - len_v + 1):
            if (string_match(p[j:j+len_v], v)):
                outputs += [j]
        if outputs:
            to_print = ' '.join([str(x) for x in outputs])
            print(to_print)
        else:
            print('No Match!')

