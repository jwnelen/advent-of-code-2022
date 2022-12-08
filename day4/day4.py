def fully_contains(elf1_low, elf1_high, elf2_low, elf2_high):
    if elf1_low <= elf2_low and elf1_high >= elf2_high:
        return True
    elif elf2_low <= elf1_low and elf2_high >= elf1_high:
        return True
    else:
        return False


def overlap(elf1_low, elf1_high, elf2_low, elf2_high):
    if elf1_high < elf2_low :
        return False

    if elf1_low > elf2_high:
        return False

    if elf2_low > elf1_high:
        return False

    if elf2_high < elf1_low:
        return False

    return True


if __name__ == '__main__':
    f = open('day4/day4.txt', 'r')
    data = [d.strip() for d in f.readlines()]

    count = 0

    for d in data:
        elf1 = d.split(',')[0]
        elf2 = d.split(',')[1]

        low_elf_1 = int(elf1.split('-')[0])
        high_elf_1 = int(elf1.split('-')[1])

        low_elf_2 = int(elf2.split('-')[0])
        high_elf_2 = int(elf2.split('-')[1])

        print(low_elf_1, high_elf_1, low_elf_2, high_elf_2)
        do_overlap = overlap(low_elf_1, high_elf_1, low_elf_2, high_elf_2)
        print(do_overlap)
        if do_overlap:
            count += 1

    print(count)
    f.close()
