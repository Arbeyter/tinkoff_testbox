def checker(n):
    word = str(n)
    len_word = len(word)
    for i in range(len_word):
        if word[i] != '9':
            return pow(10,(len_word - 1 - i))*(9-int(word[i]))
    return 0

def search_k_max(tspisock, k):
    max_ind = []
    spisock = tspisock[:]
    for t in range(k):
        tmp = max(spisock)
        tmp_ind = spisock.index(tmp)
        max_ind.append(tmp_ind)
        spisock[tmp_ind]=-1
    return max_ind

def summer(spisock, sp_ind):
    summa = 0
    for i in sp_ind:
        summa+=spisock[i]
    return summa

n , k = [int(i) for i in input().split()]
spisock = [int(i) for i in input().split()]
znach_sp = [checker(i) for i in spisock]
max_ind = search_k_max(znach_sp,k)



print(n, k)
print(spisock)
print(znach_sp)
print(max_ind)

print(summer(znach_sp,max_ind))


