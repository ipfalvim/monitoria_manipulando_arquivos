# Exemplo de manipulação de arquivos e string em Python

Escreva uma função chamada ***replace_pattern*** que recebe como argumentos uma *string-padrão*, uma *string-de-substituição* e dois *nomes de arquivos*.

Ela deve **ler** o **primeiro arquivo** (criando, se necessário). Caso a *string-padrão* apareça em algum lugar do **primeiro arquivo**, ela deve ser substituída pela *string-de-substituição*. Por padrão o nome do **primeiro arquivo** é *poema.txt*

O resultado final deve ser escrito no **segundo arquivo**.

Caso ocorra um erro na abertura, leitura ou fechamento de algum dos arquivos, deve-se exibir uma mensagem de erro e encerrar!