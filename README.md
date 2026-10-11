# 📊 Estudos: Estatística Básica - Pedro A. Morettin & Wilton de O. Bussab

Repositório dedicado ao acompanhamento prático, anotações conceituais, resolução formal de exercícios e implementações computacionais desenvolvidas ao longo do estudo do livro **Estatística Básica** (10ª Edição), de autoria de Pedro A. Morettin e Wilton de Oliveira Bussab (Editora Saraiva).

## 🎯 Objetivos de Aprendizado

- Compreender e aplicar técnicas de Análise Exploratória de Dados (AED) unidimensionais e bidimensionais.
- Dominar os fundamentos da Teoria de Probabilidades, distribuições discretas, contínuas e modelos multivariados.
- Compreender métodos de simulação estocástica e teoremas limites (Leis dos Grandes Números e Teorema Central do Limite).
- Desenvolver proficiência em Inferência Estatística: estimação pontual/intervalar e formulação rigorosa de testes de hipóteses paramétricos e não paramétricos.
- Formular, ajustar e validar modelos estatísticos clássicos (ANOVA, Tabelas de Associação/Aderência e Regressão Linear Simples/Múltipla).
- Traduzir formulações analíticas em rotinas computacionais reprodutíveis em **Python** e/ou **R**.

## 📁 Estrutura do Repositório

```plaintext
├── notebooks/              # Cadernos interativos com teoria aplicada e simulações
│   ├── 01_descritiva/      # Resumos numéricos, tabelas e visualização exploratória
│   ├── 02_probabilidade/   # Variáveis aleatórias, distribuições e Teorema de Bayes
│   ├── 03_simulacao/       # Simulação Monte Carlo e Teorema Central do Limite
│   ├── 04_inferencia/      # Estimação, intervalos de confiança e testes de hipóteses
│   └── 05_modelagem/       # ANOVA, tabelas de contingência e regressão linear
├── data/                   # Conjuntos de dados oficiais do livro (CD-Brasil, etc.)
│   ├── raw/                # Arquivos brutos originais disponibilizados pelos autores
│   └── processed/          # Bases limpas e tratadas para análises e exercícios
├── exercicios/             # Resoluções detalhadas dos problemas por capítulo
│   ├── cap02_resumo_dados/
│   ├── cap05_probabilidades/
│   └── ...
├── notes/                  # Fichamentos, fórmulas em LaTeX ($) e sínteses teóricas
├── src/                    # Scripts auxiliares e rotinas utilitárias reutilizáveis
├── .gitignore              # Arquivos e diretórios ignorados pelo Git
├── environment.yml         # Ambiente Conda (ou requirements.txt para Python/renv.lock para R)
├── LICENSE                 # Licença de uso
└── README.md               # Documentação principal do repositório
```

## 🛠️ Tecnologias e Dependências

- **Linguagens:** Python 3.14+ e/ou R 4.3+
- **Bibliotecas Centrais (Ecossistema Python):**
  - `numpy` / `scipy.stats`: Modelagem probabilística, distribuições e testes estatísticos.
  - `pandas`: Manipulação, agregação tabular e preparo de dados.
  - `matplotlib` / `seaborn`: Construção de diagramas de dispersão, histogramas e boxplots.
  - `statsmodels`: Modelos de regressão linear, ANOVA e diagnósticos de resíduos.
- *(Opcional)* **Ecossistema R:** `tidyverse`, `ggplot2`, `stats`.
- **Ambiente de Trabalho:** Jupyter Lab / VS Code / RStudio.

## 🚀 Como Executar o Projeto Localmente

### 1. Clonar o repositório

```bash
git https://github.com/rafa-fsantos/Estat_Basica.git
cd Estat_Basica
```

### 2. Criar e ativar o ambiente virtual

No Linux ou macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

No Windows (PowerShell):
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Instalar as dependências

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Abrir o ambiente de desenvolvimento

```bash
jupyter lab
```

## 📋 Checklist de Progresso do Livro

### Parte I — Análise Exploratória de Dados
- [ ] [Capítulo 01 - Preliminares](notebooks/01_descritiva/cap01_preliminares.ipynb)
- [ ] [Capítulo 02 - Resumo de Dados](notebooks/01_descritiva/cap02_resumo_dados.ipynb)
- [ ] [Capítulo 03 - Medidas-Resumo](notebooks/01_descritiva/cap03_medidas_resumo.ipynb)
- [ ] [Capítulo 04 - Análise de Dados de Várias Variáveis](notebooks/01_descritiva/cap04_analise_varias_variaveis.ipynb)

### Parte II — Probabilidades
- [ ] [Capítulo 05 - Probabilidades](notebooks/02_probabilidade/cap05_probabilidades.ipynb)
- [ ] [Capítulo 06 - Variáveis Aleatórias Discretas](notebooks/02_probabilidade/cap06_va_discretas.ipynb)
- [ ] [Capítulo 07 - Variáveis Aleatórias Contínuas](notebooks/02_probabilidade/cap07_va_continuas.ipynb)
- [ ] [Capítulo 08 - Variáveis Aleatórias Multidimensionais](notebooks/02_probabilidade/cap08_va_multidimensionais.ipynb)
- [ ] [Capítulo 09 - Noções de Simulação](notebooks/03_simulacao/cap09_nocoes_simulacao.ipynb)

### Parte III — Inferência Estatística
- [ ] [Capítulo 10 - Introdução à Inferência Estatística](notebooks/04_inferencia/cap10_intro_inferencia.ipynb)
- [ ] [Capítulo 11 - Estimação](notebooks/04_inferencia/cap11_estimacao.ipynb)
- [ ] [Capítulo 12 - Testes de Hipóteses](notebooks/04_inferencia/cap12_testes_hipoteses.ipynb)
- [ ] [Capítulo 13 - Inferência para Duas Populações](notebooks/04_inferencia/cap13_duas_populacoes.ipynb)
- [ ] [Capítulo 14 - Análise de Aderência e Associação](notebooks/05_modelagem/cap14_aderencia_associacao.ipynb)
- [ ] [Capítulo 15 - Inferência para Várias Populações](notebooks/05_modelagem/cap15_anova.ipynb)
- [ ] [Capítulo 16 - Modelos de Regressão](notebooks/05_modelagem/cap16_regressao_linear.ipynb)

- [ ] [Capítulo 17 - Séries Temporais](notebooks/05_modelagem/series_temporais.ipynb)

## 📚 Referência Bibliográfica

- **Livro:** Estatística Básica.
- **Autores:** Pedro Alberto Morettin e Wilton de Oliveira Bussab.
- **Edição:** 10ª Edição.
- **Editora:** Saraiva Uni (2024).
- **Recursos Adicionais:** Plataforma Saraiva Conecta (conjuntos de dados `CD-Brasil`, `CD-Poluição`, `CD-Municípios`).

## 📄 Licença

Este projeto é desenvolvido para fins estritamente acadêmicos e de estudo pessoal. O código autoral deste repositório está sob licença [MIT](LICENSE).
