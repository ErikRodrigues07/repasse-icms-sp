# Repasse ICMS - São Paulo

Projeto desenvolvido para realizar a coleta automatizada de dados de **Repasse ICMS dos municípios do Estado de São Paulo**, utilizando técnicas de Web Scraping e armazenamento estruturado em banco de dados SQL Server.

## Sobre o projeto

O projeto tem como objetivo automatizar a coleta dos dados disponibilizados pela **Secretaria da Fazenda e Planejamento do Estado de São Paulo (SEFAZ-SP)**, permitindo o armazenamento e a organização das informações para consultas e análises posteriores.

A coleta é realizada por meio de um script desenvolvido em **Python**, utilizando a biblioteca **Playwright** para automatizar o acesso e a navegação no portal da SEFAZ-SP.

Os dados coletados são armazenados em um banco de dados **Microsoft SQL Server**, executado em um container Docker.

## Fonte dos dados

Os dados utilizados no projeto são disponibilizados publicamente pela Secretaria da Fazenda e Planejamento do Estado de São Paulo.

Portal utilizado:

https://www.fazenda.sp.gov.br/RepasseConsulta/Consulta/repasse.aspx

## Tecnologias utilizadas

* Python
* Playwright
* Microsoft SQL Server
* Docker
* Docker Compose

## Estrutura dos dados

O banco de dados foi estruturado para armazenar informações relacionadas aos repasses de ICMS aos municípios paulistas.

Entre as principais tabelas utilizadas estão:

* `Municipios` — informações dos municípios do Estado de São Paulo;
* `RepasseMensal` — dados referentes aos repasses mensais;
* `RepasseSemanal` — dados referentes aos repasses semanais.

## Banco de dados

O SQL Server é executado por meio de um container Docker.

Por questões de segurança, o arquivo utilizado localmente para configuração do container não é disponibilizado no repositório.

O projeto disponibiliza apenas um arquivo de exemplo:

```text
docker-compose.example.yml
```

Para utilizar o projeto localmente, copie esse arquivo para:

```text
docker-compose.yml
```

e configure as informações necessárias de acordo com o ambiente local.


## Objetivo acadêmico

Este projeto faz parte de um Trabalho de Conclusão de Curso (TCC) desenvolvido na **USP/ESALQ**, tendo como foco a aplicação de técnicas de Web Scraping para coleta e organização de dados públicos relacionados ao Repasse ICMS dos municípios do Estado de São Paulo.

A disponibilização do código tem como objetivo contribuir para a transparência, reprodutibilidade e utilização dos dados coletados para fins de consulta e análise.

## Licença

Este projeto é disponibilizado para fins acadêmicos e de pesquisa.
