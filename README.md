### Olá, seja bem vindo ao meu diretório. Esta página é somente um relatório do projeto, para acessar as análises na íntegra clique na pasta "notebooks" e em seguida no arquivo "notebook.ipynb" :smiley:
# BuyMore Company
## Sales Forecast
![](img/capa.jpg)
## 1.0 Contexto
A rede de supermercados BuyMore está com uma necessidade de atualizar seus sistemas preditivos, e a forma com que compartilha informações relevantes com seus stackholders. O time de negócios entendeu que há demanda na empresa por melhorar sua capacidade de PREDITIBILIDADE, ou seja, melhorar a forma com que faz predições, e melhorar a forma com que COMPARTILHA suas INFORMAÇÕES, com o uso de dashboards compartilháveis e com segurança de dados e um sistema de ENVIOS DE NOTIFICAÇÕES para o smartphone de todos os envolvidos no processo. Inicialmente no setor financeiro, mais especificamente um preditor de demanda. Uma empresa tercerizada foi contratada para fazer a entrega de um produto de dados desenvolvido sob demanda para solucionar o problema de negócios descrito.
## 2.0 Tools and Requirements
### Linguagem de desenvolvimento - Python
### Banco de Dados - Postgres
### Servidor - Linux Server 22.04 local
### Container - Docker
### Workflow - Airflow
### Demais bibliotecas disponívels em "requirements.txt" no diretório raíz do projeto
## 3.0 Business Assumptions
A granularidade original dos dados segue a seguinte orientação: DEPERTAMENTOS -> LOJAS -> DATAS. Foi assumido um posicionamento de trabalhar sem a separação de DEPARTAMENTOS, por motivo de redução de complexidade, os departamentos foram mantidos no dataset e utilizados para visualizações em dashboards somente portanto a granularidade segue no projeto como sendo: LOJAS -> DATAS.
## 4.0 Estratégia da Solução
### 4.1 Objetivos:
Criar um sistema preditivo para todas as lojas da rede, de forma que a informação seja facilmente acessada por todos os envolvidos no processo, com envios de notificações por smartphones, dashboards compartilháveis, com informações disponívels em tempo real, atualizada e automatizada acessível por smartphones e notebooks.
### 4.2 Entregáveis:
1. Preditor de demanda para a rede
2. Dashboard
3. Sistema de envios de mensagens de texto para o smartphone dos envolvidos
4. Pipeline de Dados com Workflow automatizado
## 5.0 Top3 Data Insights
## 6.0 Machine Learning Applied
## 7.0 Machine Learning Performance
## 8.0 Buisness Results
## 9.0 Leasson Learned
## 10.0 Summary
### Dataframe Train
#### Store - Número único de identificação da Loja
#### Dept - Número único de identificação do Departamento
#### Date - Data (granularidade semanal)
#### Weekly_Sales - Valor total semanal de venda do departamento
#### IsHoliday - É ou não feriado
### Dataframe Features
#### Store - Número único de identificação da Loja
#### Date - Data (granularidade semanal)
#### Temperature - Temperatura em fahrenheit
#### Fuel_Price - Preço do combustível em Dolar
#### MarkDown - Não há informações sobre
#### Cpi - Índice de Preço ao Consumidor regional
#### Unemployment - Taxa de desemprego regional
#### IsHoliday - É ou não feriado
### Dataframe Stores
#### Store - Número único de identificação da Loja
#### Type - Tipo de Loja
#### Size - Tamanho da Loja
## 11.0 Next Steps
* Coletar novos dados
* Retreinar o modelo a cada ano
* Melhorar o entendimento com novas features, 
* Buscar com os envolvidos no processo informações sobre Markdown
## 12.0 Estágio Atual do Projeto
