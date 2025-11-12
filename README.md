# 🌐 Portfólio de Projetos — Guilherme Fernandes Secco

Portfólio interativo desenvolvido com **Flask**, **Bootstrap** e integração com **GitHub API**, apresentando meus principais projetos nas áreas de **Data Science**, **Machine Learning** e **Automação**.

<img width="1850" height="1002" alt="image" src="https://github.com/user-attachments/assets/c2524524-a395-41b7-966f-de992f545ccf" />

---

## 🚀 Sobre o Projeto

Este site foi desenvolvido para reunir, organizar e **apresentar de forma dinâmica** meus projetos de tecnologia.  
Cada projeto possui uma página dedicada, com:
- 🧠 Descrição técnica detalhada  
- 🖼️ Imagem ilustrativa  
- 🧾 Tecnologias utilizadas  
- 💬 Explicação do raciocínio de modelagem ou implementação  
- 🔗 Links diretos para o GitHub e, quando disponível, **demonstrações interativas**

O portfólio é totalmente **responsivo e dinâmico**, alimentado automaticamente via **API do GitHub** — sem necessidade de atualizar manualmente cada projeto.

---

## ⚙️ Principais Funcionalidades

- 🔄 **Integração automática com o GitHub**  
  Exibe todos os repositórios que contenham o tópico `portfolio-project`.

- 🧩 **Exibição de tecnologias e linguagens usadas**  
  Cada projeto exibe badges coloridos com base em suas *tags* (por exemplo: `python`, `machine-learning`, `flask`, etc).

- 💻 **Páginas individuais para projetos selecionados**  
  Projetos especiais possuem uma rota dedicada dentro do site, com visual customizado.

- 🌈 **Temas dinâmicos e animações suaves**  
  Interface moderna construída com **Bootstrap 5** e **Animate.css**.

- 📱 **Design responsivo e leve**  
  Totalmente adaptado para dispositivos móveis e desktop.

---

## 🧠 Estrutura do Projeto

    project_root/
    ├── app.py # Arquivo principal Flask
    ├── views.py # Blueprints e rotas do site
    ├── static/
    │ ├── bootstrap/ # Framework CSS local
    │ ├── css/ # Estilos de cada projeto
    │ ├── img/ # Ícones e imagens
    │ └── script.js # Scripts globais
    ├── templates/
    │ ├── base.html # Template principal
    │ ├── index.html # Página inicial
    │ ├── projetos.html # Página com listagem de repositórios
    │ └── projetos/
    │ └── simulador-credito.html # Exemplo de projeto com página dedicada
    └── ml_models/ # Modelos e scripts de Machine Learning


---

## 💻 Tecnologias Utilizadas

| Categoria | Tecnologias |
|------------|-------------|
| **Backend** | Flask (Python) |
| **Frontend** | HTML5, CSS3, Bootstrap 5, JavaScript |
| **Integração** | GitHub REST API |
| **Animações e Estilo** | Animate.css, Bootstrap Icons |
| **Machine Learning (em projetos específicos)** | XGBoost, scikit-learn, pandas, NumPy |

---

## 🧩 Projetos em Destaque

### 💳 [Simulador de Crédito Inteligente](https://github.com/GuilhermeSecco/Simulador-Credito)
> Um simulador de aprovação de crédito que usa **XGBoost** para prever risco de inadimplência e definir taxa de juros personalizada.

📊 **Tópicos:** `python`, `machine-learning`, `flask`, `bootstrap`, `xgboost`

---

### 🧠 Outros Projetos
Além do simulador, o portfólio integra automaticamente todos os projetos do meu GitHub que possuem o tópico:

    portfolio-project

Para projetos com demonstrações ativas (por exemplo, Streamlit, Flask ou sites publicados), basta adicionar também:

    portfolio-demo

Isso adiciona automaticamente um botão “Acessar Demonstração” ao card do projeto. 🚀

## 🔧 Configuração Local

Para executar o portfólio localmente:

    1️⃣ Clonar o repositório
    git clone https://github.com/GuilhermeSecco/portfolio.git
    cd portfolio
    
    2️⃣ Criar ambiente virtual
    python -m venv venv
    source venv/bin/activate  # (ou venv\Scripts\activate no Windows)
    
    3️⃣ Instalar dependências
    pip install -r requirements.txt
    
    4️⃣ Executar o servidor Flask
    python app.py
    
    Acesse:
    👉 http://localhost:5000

## 🌈 Estrutura Visual

    🔹 Sidebar fixa com navegação por seções (Início, Sobre, Habilidades, Projetos, Contato)

    🔹 Cards de projetos automáticos, alimentados por tópicos do GitHub

    🔹 Seção de contato com links para LinkedIn e GitHub

    🔹 Tema escuro predominante, com realces em cores de destaque

## 💡 Próximas Melhorias

    🔍 Modo de busca para projetos

    🧾 Página de blog/tutoriais técnicos

    💬 Seção interativa para feedback dos visitantes

    🌙 Tema claro/escuro alternável

## Links

### [💼LinkedIn](https://www.linkedin.com/in/guilherme-f-secco/)
### [💻GitHub](https://github.com/GuilhermeSecco)
