def len_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return len(f.readlines())


def sorted_files():
    res = {}
    for i in range(1, 4):
        filename = f'{i}.txt'
        res[filename] = len_file(filename)
    return sorted(res.items(), key=lambda x: x[1])

for filename, lines_count in sorted_files():
    print(filename)
    print(lines_count)
    with open(filename, 'r', encoding='utf-8') as f:
        print("".join(f.readlines()))
