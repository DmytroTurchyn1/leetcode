num = int(input("Enter a number : "))

def maximumSwap(num):
    res = [int(x) for x in str(num)]
    i = 0

    for x in res:
        while i<len(res):
            if x > res[i]:
                b = res[i]
                x, res[i] = res[i], x
            else:
                pass

            i+=1

    print(res)








    # maxIndex = res.index(max(res))
    # res[maxIndex],res[0]=res[0],res[maxIndex]
    # integer = int("".join([str(x) for x in res]))
    # return integer
# res[res.index(x)], res[res.index(y)] = res[res.index(y)], res[res.index(x)]
maximumSwap(num)