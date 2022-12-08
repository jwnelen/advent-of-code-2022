if __name__ == '__main__':
    f = open('day1/day1.txt', 'r')
    data = [d.rstrip() for d in f.readlines()]

    temp_sum = 0
    sums = []

    for i in range(len(data)):
        if data[i] == '':
            sums.append(temp_sum)
            temp_sum = 0
        else:
            temp_sum += int(data[i])

    print(sums)
    sums.sort(reverse=True)
    x = sums[:3]
    print(sums)
    print(sum(x))

    f.close()
