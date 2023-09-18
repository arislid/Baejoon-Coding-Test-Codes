def reverse_string():
    a = input()
    zeros = []
    ones = []
    zero = ''
    one = ''
    if len(a) == 1:
        print(1)
    for i, x in enumerate(a):
        if i < len(a)-1:
            if x == '0':
                zero += x
                if a[i+1] == '1':
                    zeros.append(zero)
                    zero = ''
            else:
                one += x
                if a[i+1] == '0':
                    ones.append(one)
                    one = ''
        else:
            if x == '0':
                zero += x
                zeros.append(zero)
            else:
                one += x
                ones.append(one)

    # print(zeros)
    # print(ones)
    print(min(len(zeros), len(ones)))

if __name__=='__main__':
    reverse_string()