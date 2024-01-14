# Enumeração de Subdomínios e Brute Force de Diretórios

Este projeto é uma ferramenta simples para realizar a enumeração de subdomínios e brute force de diretórios em uma URL.

## Funcionalidades

### Enumeração de Subdomínios

A função `brutesub` usa a biblioteca `dns.resolver` para enumerar subdomínios de uma URL fornecida.

```bash
python seu_script.py http://sua-url.com lista_de_subdominios.txt

### Brute Force de Diretórios
A função brutedir tenta acessar diretórios em uma URL fornecida e imprime os resultados.

```bash
python seu_script.py http://sua-url.com lista_de_diretorios.txt
