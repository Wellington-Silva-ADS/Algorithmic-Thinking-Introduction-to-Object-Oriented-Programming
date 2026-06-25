# Sistema de Orçamento Imobiliário - R.M Imóveis

## Sobre o Projeto

Este projeto foi desenvolvido como atividade prática da disciplina **Algorithmic Thinking & Introduction to Object-Oriented Programming** do curso de **Análise e Desenvolvimento de Sistemas** da UniFECAF.

O sistema tem como objetivo automatizar a geração de orçamentos de locação para uma imobiliária fictícia chamada **R.M Imóveis**, permitindo calcular valores de aluguel com base em diferentes regras de negócio.

## Funcionalidades

* Seleção do tipo de imóvel:

  * Apartamento
  * Casa
  * Estúdio

* Cálculo automático do valor do aluguel.

* Acréscimo de valores conforme:

  * Quantidade de quartos.
  * Vaga de garagem.
  * Vagas adicionais para estúdios.

* Aplicação de desconto para apartamentos sem crianças.

* Parcelamento do contrato imobiliário em até 5 vezes.

* Geração automática de arquivo CSV contendo as 12 parcelas do orçamento.

## Tecnologias Utilizadas

* Python 3
* Biblioteca CSV (nativa do Python)

## Conceitos Aplicados

Durante o desenvolvimento foram utilizados conceitos fundamentais de programação:

* Variáveis
* Estruturas condicionais
* Laços de repetição
* Tratamento de exceções
* Entrada e saída de dados
* Manipulação de arquivos
* Lógica de negócios

## Exemplo de Uso

```text
Digite o tipo de imóvel: apartamento
Quantos quartos? 2
Possui crianças? n
Deseja vaga de garagem? s
```

Resultado:

```text
Valor do aluguel mensal: R$ 1.140,00
Valor total do contrato: R$ 2.000,00
Parcelado em 5x de R$ 400,00
```

## Estrutura do Projeto

```text
Portfolio.py
orcamento_imobiliario.csv
README.md
```

## Melhorias Futuras

* Interface gráfica.
* Persistência em banco de dados.
* Aplicação web utilizando Flask ou Django.
* Implementação completa dos princípios de Programação Orientada a Objetos.
* Cadastro de clientes e imóveis.

## Autor

Wellington de Paula Silva

Estudante de Análise e Desenvolvimento de Sistemas (UniFECAF)

Interesses:

* Desenvolvimento Back-end
* Qualidade de Software
* Automação de Processos
* Engenharia de Software
