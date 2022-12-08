def map_letter_to_num(letter):
    if letter.isupper():
        return ord(letter) - 38
    else:
        return ord(letter) - 96


if __name__ == '__main__':
    f = open('day3/day3.txt', 'r')
    data = [d.strip() for d in f.readlines()]

    sum = 0
    # Get list
    for i in range(0, len(data) - 1, 3):
        l1 = set(data[i])
        l2 = set(data[i + 1])
        l3 = set(data[i + 2])

        # Get intersection
        item = l1.intersection(l2)
        item = item.intersection(l3)

        print(item)
        item = list(item)[0]
        print(len(l1), len(l2), item)
        # Map to amount
        amount = map_letter_to_num(item)
        sum += amount

    print(sum)
    f.close()
