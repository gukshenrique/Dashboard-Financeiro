# Dashboard Financeiro 📈

De modo a estudo, este dashboard foi criado com informações de cartão de crédito pessoal, para fins de aprendizagens e portfolio de meus projetos.

[Visualizar Dashboard](https://app.powerbi.com/view?r=eyJrIjoiNzRjYTEwNGEtM2U2MC00NDNjLThmMmItOTMwZjcyY2IxYTc0IiwidCI6Ijk3MDJhNGE5LTk3ZGEtNDAwMS1hZDQ0LTMyZjNlNzY2MmY3YyJ9)


Antes de iniciar o projeto, fiz um fluxograma para nao me perder nas etapas



![_Fluxograma](https://github.com/gukshenrique/Dashboard-Financeiro/assets/97614116/7656c430-d193-443f-9727-002c421f3a58)




Temos 1 pasta e 2 arquivos para a execução final:

- UnifCSV: Esse codigo serve para unificar e consolidar todos os arquivos csv, ofx que estao dentro da pasta "Cartao".
  Ele lê, padroniza as colunas e nomes para depois transformar em um unico arquivo "Dados.csv".


![USANDO-O-UNIF-CSV](https://github.com/gukshenrique/Dashboard-Financeiro/assets/97614116/19f045e8-fa24-4461-a0de-0e76dc3e259f)





- DadosToSQL: Lê as informações em "Dados.csv" e insere no SQL em Banco de Dados. No meu caso eu escolhi o POSTGRESQL como a ferramenta para manusear o SQL.

![PEGANDO-ARQUIVO-DADOS-E-INSERINDO-NO-DATA-BASE](https://github.com/gukshenrique/Dashboard-Financeiro/assets/97614116/0b090b6e-ca9c-429a-ae1a-2f90e6353b3e)






- Após rodar o codigo no python, já posso consultar as informações dentro do SQL.

![SEELECT-FROM-DADOS-POSTGREE4](https://github.com/gukshenrique/Dashboard-Financeiro/assets/97614116/314ec64b-8265-42c5-8f66-3abf23826590)





  



