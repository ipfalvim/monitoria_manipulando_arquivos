def replace_pattern(pattern, replace, source, dest):
    try:
        fin = open(source, 'r')
        fout = open(dest, 'w')
    except:
        return print("Erro na abertura do arquivo, verifique o nome")

    for line in fin:
        line = line.replace(pattern, replace)
        fout.write(line)

    try:
        fin.close()
        fout.close()
    except:
        return print("Erro no fechamento dos arquivos!!!")

def main():
    pattern = 'Ilha'
    replace = 'Floresta'
    source = 'poema.txt'
    dest = source + '.replaced'
    replace_pattern(pattern, replace, source, dest)


if __name__ == '__main__':
    main()