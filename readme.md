# Aos Fatos Spider

Este projeto contém um spider Scrapy chamado `AosfatosspiderSpider`, desenvolvido para rastrear e extrair informações do site "Aos Fatos". O objetivo principal é analisar o impacto da desinformação nos direitos difusos como parte de um estudo preliminar financiado pelo Fundo de Direitos Difusos (FDD).

## O que é o Fundo de Direitos Difusos (FDD)?

O Fundo de Direitos Difusos (FDD) é um fundo administrado pelo Ministério da Justiça e Segurança Pública do Brasil. Ele visa financiar projetos que promovam a reparação de danos causados ao meio ambiente, ao consumidor, a bens e direitos de valor artístico, estético, histórico, turístico e paisagístico, entre outros direitos difusos.

## Objetivo do Projeto

Este projeto faz parte de um processo de análise dos impactos da desinformação nos direitos difusos. A coleta e análise de dados de checagem de fatos são etapas preliminares para entender como a desinformação pode afetar esses direitos.

## Estrutura do Projeto

O projeto consiste nos seguintes arquivos principais:

- `aosfatosspider.py`: Contém a definição do spider Scrapy que rastreia e extrai dados do site "Aos Fatos".
- `aosfatoscraper_pipeline.py`: Contém a definição do pipeline que processa os itens extraídos pelo spider.

Além disso, o projeto inclui todos os arquivos típicos de um projeto Scrapy, como `items.py`, `middlewares.py`, `settings.py`, entre outros.


## Dependências

- Python 3.x
- Scrapy
- scrapy-xlsx

## Como Funciona

### Importações

O código começa importando o módulo Scrapy e a classe `AosfatoscraperItem` do módulo `aosfatoscraper.items`. O Scrapy é usado para fazer o web scraping e `AosfatoscraperItem` define a estrutura dos dados a serem extraídos.

### Definição da Classe

Define-se a classe `AosfatosspiderSpider`, que herda de `scrapy.Spider`. Esta classe é o coração do spider e contém toda a lógica para rastrear e extrair dados do site "Aos Fatos".

### Configurações Iniciais

- O nome do spider é definido como `aosfatosspider`.
- Os domínios permitidos para rastreamento são especificados.
- A URL inicial de onde o spider começará a rastrear é definida.

### Método `parse`

1. **Extração de Links de Notícias**: O método `parse` extrai links de notícias individuais de checagem de fatos da página inicial usando seletores CSS.
2. **Seguir Links de Notícias**: Para cada link de notícia extraído, o spider segue o link e chama o método `parse_newscheck_page` para processar a página da notícia.
3. **Paginação**: O método também identifica o link para a próxima página de resultados. Se existir, o spider segue o link e chama `parse` novamente para continuar o processo de extração na próxima página.

### Método `parse_newscheck_page`

1. **Criação do Item**: Cria uma instância de `AosfatoscraperItem`, que será preenchida com os dados extraídos.
2. **Extração de Parágrafos**: Extrai todos os parágrafos do artigo de checagem de fatos.
3. **Identificação do Último Parágrafo**: Identifica o último parágrafo e extrai todos os links e o texto dele.
4. **Verificação de Conteúdo**: Se o último parágrafo não contiver um determinado padrão, o spider verifica os parágrafos anteriores até encontrar o padrão desejado.
5. **Montagem de Texto e Referências**: Extrai os links e o texto de todos os parágrafos, excluindo o último, e os combina em strings separadas.
6. **Preenchimento do Item**: Preenche os campos do item `AosfatoscraperItem` com os dados extraídos, como URL, texto, data de publicação, título, fonte, status de checagem e referências.
7. **Retorno do Item**: Retorna o item preenchido para ser processado pelo pipeline.

### Funcionamento Geral

- O spider inicia na página principal de checagem de fatos, extrai links de notícias, navega por essas notícias, extrai dados detalhados de cada notícia e segue para a próxima página de resultados.
- Durante a extração detalhada, o spider identifica e formata o conteúdo dos parágrafos, verificando a presença de padrões específicos antes de extrair os dados finais.
- Todos os dados extraídos são organizados e retornados na forma de itens estruturados, prontos para serem processados e armazenados.
- **Depois de instaladas as dependências, é só executar "scrapy crawl aosfatosspider -O nome_do_arquivo.xlsx"**, certificando-se de que está na pasta do scraper.
  
## Licença

### MIT License

© 2024 Douglas da Silva Ferreira

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
