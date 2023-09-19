# validaCpf
Algoritmo para verificar a consistência de um número de CPF.
**NÃO** indica que o CPF existe e/ou pertence a alguém; para esse tipo de validação, consultar o site da Receita Federal.

## Como funciona
- O programa recebe um número de cpf dado pelo usuário; 
- Armazena-o numa variável secundária, mantendo o input original;
- Na var. secundária, remove os dois últimos dígitos que vieram do input;
- Segundo a forma de validação explicada no site [calculadorafacil](https://www.calculadorafacil.com.br/computacao/validar-cpf#Como%20Validar%20CPF):
- calcula os dois últimos dígitos verificadores do cpf;
- adiciona esses dígitos à variável secundária;
- e o compara com o cpf do input do usuário. 

*se resultarem no mesmo número, o cpf é consistente ("válido")*

Gere alguns CPF's para testar: [4devs](https://www.4devs.com.br/gerador_de_cpf)