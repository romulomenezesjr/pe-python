1. Leitura e Escrita em Arquivo de Texto

Exercício:
Crie um programa em Python que:

Leia um arquivo de texto chamado entrada.txt e imprima seu conteúdo na tela.
Em seguida, escreva um novo arquivo chamado saida.txt que contenha o conteúdo do arquivo entrada.txt, mas com todas as letras em maiúsculas.

Dica: Utilize os métodos read() e write() para realizar a leitura e escrita dos arquivos.

2. Listagem de Arquivos em um Diretório

Exercício:
Escreva um programa que:

Solicite ao usuário o caminho de um diretório.
Liste todos os arquivos e diretórios contidos no caminho fornecido e exiba-os na tela.

Dica: Utilize os.listdir() para listar o conteúdo do diretório.


3. Cópia de Arquivo

Exercício:
Implemente um programa que:

Solicite ao usuário o nome de um arquivo de origem e o nome do arquivo de destino.
Realize a cópia do arquivo de origem para o arquivo de destino.

Dica: Utilize shutil.copy() para realizar a cópia do arquivo.

4. Busca de Arquivos com glob

Exercício:
Crie um programa que:

Solicite ao usuário um padrão de arquivo (por exemplo, *.txt).
Liste todos os arquivos no diretório atual que correspondem ao padrão informado.

Dica: Utilize a biblioteca glob para buscar arquivos com base no padrão fornecido.


5. Manipulação de Arquivos JSON

Exercício:
Escreva um programa que:

Crie um arquivo JSON chamado dados.json que contenha informações sobre 3 pessoas (nome, idade e profissão).
Depois, leia esse arquivo JSON e exiba as informações de cada pessoa na tela.

Dica: Utilize as funções json.dump() e json.load() para a escrita e leitura do arquivo JSON.


6. Manipulação de Arquivos CSV

Exercício:
Implemente um programa que:

Leia um arquivo CSV chamado produtos.csv, que contém uma lista de produtos com os campos: Nome, Preço e Quantidade.
Após a leitura, exiba o nome de todos os produtos que têm preço superior a R$ 50,00.

Dica: Utilize o módulo csv para ler o arquivo e filtrar os produtos com base no preço.


7. Serialização com pickle

Exercício:
Crie um programa que:

Defina uma lista de dicionários representando dados de alunos (nome, idade e nota).
Serialize esses dados em um arquivo chamado alunos.pkl usando o módulo pickle.
Depois, leia o arquivo alunos.pkl e exiba os dados de cada aluno na tela.

Dica: Utilize pickle.dump() para serializar e pickle.load() para desserializar os dados.


8. Verificação e Manipulação de Arquivos

Exercício:
Escreva um programa que:

Verifique se um arquivo chamado log.txt existe no diretório atual.
Se existir, renomeie o arquivo para log_antigo.txt. Se não existir, crie o arquivo log.txt com o conteúdo "Arquivo de log criado."

Dica: Utilize os.path.exists() para verificar a existência do arquivo e os.rename() para renomeá-lo.


9. Criação e Remoção de Diretórios

Exercício:
Implemente um programa que:

Crie uma estrutura de diretórios recursivamente com o caminho projetos/python/codigo.
Depois, remova o diretório codigo e seus subdiretórios.

Dica: Utilize os.makedirs() para criar os diretórios e os.removedirs() para removê-los.

10. Atualização de Arquivo CSV

Exercício:
Crie um programa que:

Leia um arquivo CSV chamado estoque.csv, contendo informações de produtos em estoque (Nome, Quantidade, Preço).
Atualize o arquivo CSV, multiplicando o preço de todos os produtos por 1.1 (aumento de 10%).

Dica: Utilize o módulo csv para ler e escrever de volta os dados atualizados no arquivo.
