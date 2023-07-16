# 2. Kopējie Elementi


def get_common_ellements(seq1, seq2, seq3):
    return tuple(set(seq1) & set(seq3) & set(seq2))


def main():
    print(get_common_ellements(['a', 'b'], "abc", ('b', 'c')))


if __name__ == "__main__":
    main()
