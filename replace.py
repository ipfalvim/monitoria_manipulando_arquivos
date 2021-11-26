def replace_pattern(pattern, replace, source, dest):
    raise NotImplementedError

def main():
    pattern = 'Ilha'
    replace = 'Floresta'
    source = 'poema.txt'
    dest = source + '.replaced'
    replace_pattern(pattern, replace, source, dest)


if __name__ == '__main__':
    main()