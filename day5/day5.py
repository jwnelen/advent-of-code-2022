import numpy as np


def get_first_non_empty(row):
    return next((i for i, x in enumerate(row) if x != '0'), len(row))


def get_crates(data_in, bucket_in, amount_in):
    index_first_crate = get_first_non_empty(data_in[bucket_in])
    print('row', data_in[bucket_in])
    print('index', index_first_crate)

    return_vals = data_in[bucket_in][index_first_crate:index_first_crate + amount_in]
    data_in[bucket_in][index_first_crate:index_first_crate + amount_in] = '0' * amount_in

    return_vals.reverse()
    return return_vals


def move_crates(data_in, crates_in, to_bucket):
    index_first_crate = get_first_non_empty(data_in[to_bucket])
    print('counter', index_first_crate)
    data_in[to_bucket][index_first_crate - len(crates_in):index_first_crate] = crates_in


def process_result(data_in):
    res = [row[get_first_non_empty(row)] for row in data_in]
    return res


if __name__ == '__main__':
    f = open('day5/day5.txt', 'r')
    data = [d for d in f.readlines()]

    buckets = []
    counter = 0
    while "1" not in data[counter]:
        d = data[counter]
        d = d.replace("    ", "0").replace(' ', '') \
            .replace("[", "").replace("]", "").replace("\n", "")

        buckets.append(list(d))
        counter += 1

    rows = [d for d in data[counter].split(" ") if d != '' and d != '\n']
    counter += 1
    moves = [d.strip() for d in data[counter:] if d.strip() != '']

    buckets = np.array(buckets).T.tolist()
    a = 1
    buckets = [["0"] * a + d for d in buckets]

    # print(buckets, rows, moves, sep="\n")
    print(buckets)

    for move in moves:
        print(move)
        l = move.split(" ")
        amount, bucket_from, bucket_to = int(l[1]), int(l[3]) - 1, int(l[5]) - 1

        print(amount, bucket_from, bucket_to)
        crates = get_crates(buckets, bucket_from, amount)
        print('crates', crates)

        move_crates(buckets, crates, bucket_to)

        print('after move', buckets)

    r = process_result(buckets)
    print(r)
    r = ''.join(r)
    print('result', r)

    f.close()
