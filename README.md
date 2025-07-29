# Tech Challenge - Fase 4: Previsão de Ações com LSTM 📈

Neste projeto, desenvolvemos um modelo preditivo de redes neurais **Long Short-Term Memory (LSTM)** que realiza previsões do valor de fechamento da ação **SAPR4 (Sanepar)** na bolsa de valores, com base em dados históricos obtidos através do Yahoo Finance.

Esse modelo foi implementado em uma **API RESTful** desenvolvida com **FastAPI**, que recebe uma data como parâmetro e retorna uma previsão para o preço da ação. A aplicação foi totalmente containerizada com Docker para garantir a portabilidade e a consistência do ambiente.

**Desenvolvido por:** Bianca Gobe, Emerson Quirino e Mayara Reghin.  
*Projeto para a pós-graduação em Machine Learning Engineering da FIAP.*

---

### 📊 Redes Neurais LSTM

O projeto utiliza redes neurais do tipo Long Short-Term Memory (LSTM), uma variação das Redes Neurais Recorrentes (RNN) especialmente eficaz para lidar com dados sequenciais e séries temporais. As LSTMs são capazes de aprender padrões de longo prazo, superando limitações das RNNs tradicionais, o que as torna ideais para modelar os comportamentos complexos do mercado financeiro.

Neste projeto, os LSTMs foram aplicados para prever o valor do fechamento das ações da Companhia de Saneamento Paraná SANEPAR na bolsa de valores, com base no histórico de preços. O modelo foi treinado utilizando dados diários.

O código do treinamento do modelo está disponível também no Google Colab: [Link para o Colab](https://colab.research.google.com/drive/11CINwt-G1YskeQQOo03HMhs9sbwC_o71?usp=sharing)

### 🛠️ Tecnologias Utilizadas

-   📦 **Python 3.11**
-   🧠 **TensorFlow / Keras:** Treinamento do modelo LSTM.
-   📊 **Pandas, Numpy, Scikit-learn:** Manipulação e pré-processamento de dados.
-   📈 **yfinance:** Coleta de dados financeiros.
-   🚀 **FastAPI:** Criação da API REST.
-   💾 **SQLAlchemy & Alembic:** ORM e gerenciamento de migrations para o banco de dados SQLite.
-   🐳 **Docker:** Containerização da aplicação.
-   ☁️ **AWS EC2:** Deploy da aplicação em nuvem.
-   📡 **AWS CloudWatch:** Monitoramento de performance e recursos.

---

### 🚀 Funcionalidades da API

-   **Previsão do Valor das Ações:** Retorna a previsão do valor de fechamento das ações SAPR4 a partir de uma data informada.
-   **Autenticação Segura:** As rotas da API são protegidas por autenticação **JWT (JSON Web Token)**. Os usuários podem criar, consultar, alterar e deletar suas próprias contas. O token de acesso é válido por 30 minutos.
-   **Documentação Interativa:** A API conta com documentação automática e interativa gerada pelo Swagger UI.

### 🔬 Monitoramento e Escalabilidade

Para garantir a robustez e a confiabilidade da aplicação em produção, foi implementada uma estratégia completa de monitoramento e escalabilidade utilizando os serviços da AWS.

-   **Monitoramento com AWS CloudWatch:**
    -   **Recursos da Instância:** O **Agente do CloudWatch** foi configurado na instância EC2 para coletar métricas essenciais de performance, como **Utilização da CPU (%), Uso de Memória RAM (%) e Uso do Disco (%)**.
    -   **Performance da Aplicação:** A API foi instrumentada com um *middleware* customizado que envia uma métrica de **Tempo de Resposta (Latência)** para o CloudWatch a cada previsão realizada.
    -   **Dashboard Centralizado:** Todas as métricas foram consolidadas em um dashboard unificado, permitindo uma visualização clara e em tempo real da saúde da aplicação.

-   **Estratégia de Escalabilidade:**
    -   A aplicação foi totalmente containerizada com **Docker**, garantindo que o ambiente seja consistente e facilmente replicável. Para um ambiente de produção com alta demanda, a arquitetura pode ser estendida com um **Application Load Balancer (ALB)** para distribuir o tráfego e um **Auto Scaling Group (ASG)** para ajustar o número de instâncias automaticamente com base na carga.

---

### 🧪 Como Executar o Projeto Localmente

**Pré-requisitos:**
-   Python 3.11
-   Docker

**1. Clone o Repositório**
```bash
git clone [https://github.com/emersonquirino/Previsao-acao-SAPR4-Tech-Challenge-4.git](https://github.com/emersonquirino/Previsao-acao-SAPR4-Tech-Challenge-4.git)
cd Previsao-acao-SAPR4-Tech-Challenge-4/
```

**2. Construa a Imagem Docker**
Este comando pode levar vários minutos, pois instalará todas as dependências.
```bash
docker build -t previsao-api .
```

**3. Execute o Contêiner**
```bash
docker run -d -p 8000:8000 --name api-container previsao-api
```

**4. Inicialize o Banco de Dados (Passo Crucial)**
Execute o comando abaixo para criar as tabelas do banco de dados dentro do contêiner.
```bash
docker exec api-container alembic upgrade head
```

**5. Acesse a API**
A API estará disponível no seu navegador no endereço:
[http://localhost:8000/docs](http://localhost:8000/docs)

---

### ☁️ Deploy na Nuvem

O deploy foi realizado em uma instância **EC2 da AWS**. A API está disponível publicamente no seguinte endereço:  
**Link da API:** [http://3.14.153.23:8000/docs](http://3.14.153.23:8000/docs)


### 🤝 Contribuindo
Fork este repositório.
Crie sua branch (git checkout -b feature/nova-funcionalidade).
Faça commit das suas alterações (git commit -m 'Adiciona nova funcionalidade').
Faça push para sua branch (git push origin feature/nova-funcionalidade).
Abra um Pull Request. instalar, configurar e usar o projeto. Ele também cobre contribuições, contato, licença e agradecimentos, tornando-o completo e fácil de entender para novos desenvolvedores.
