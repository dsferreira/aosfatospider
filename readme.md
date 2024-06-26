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

**Copyleft License**

This software is licensed under the terms of the GNU General Public License v3.0. By using, modifying, or distributing this software, you agree to the terms and conditions of this license.
Terms and Conditions for Copying, Distribution, and Modification

  Source Code: The "source code" for a work means the preferred form of the work for making modifications to it. "Object code" means any non-source form of a work.

  Basic Permissions: You may copy and distribute verbatim copies of the Program's source code as you receive it, in any medium, provided that you conspicuously and appropriately publish on each copy an appropriate copyright notice; keep intact all notices stating that this License applies to the code; keep intact all notices of the absence of any warranty; and give all recipients a copy of this License along with the Program.

  Conveying Modified Source Versions: You may convey a work based on the Program, or the modifications to produce it from the Program, in the form of source code under the terms of section 2, provided that you also meet all of these conditions:
        The work must carry prominent notices stating that you modified it, and giving a relevant date.
        The work must carry prominent notices stating that it is released under this License.
        You must license the entire work, as a whole, under this License to anyone who comes into possession of a copy.

  Conveying Non-Source Forms: You may convey the object code of a work under the terms of sections 1 and 2, provided that you also convey the machine-readable Corresponding Source under the terms of this License.

   No Surrender of Others' Freedom: You are not responsible for enforcing compliance by third parties with this License.

   Revised Versions of this License: The Free Software Foundation may publish revised and/or new versions of the GNU General Public License from time to time. Each version is given a distinguishing version number. If the Program specifies that a certain numbered version of the GNU General Public License "or any later version" applies to it, you have the option of following the terms and conditions either of that numbered version or of any later version published by the Free Software Foundation.

