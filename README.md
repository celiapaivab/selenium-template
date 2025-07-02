# 🚀 Selenium Template

Este repositório é um template base para automação de testes com Selenium e Pytest, com suporte para:

- Estrutura modular (Page Object Model)
- Pipeline CI/CD com GitHub Actions
- Relatórios HTML (opcional)
- Testes BDD com Gherkin (opcional)


---

## Como usar

Para iniciar um novo projeto baseado neste template, siga os passos:

1. Clique no botão **"Use this template"**.

2. Escolha um nome para o novo repositório e clique em **"Create repository from template"**.

3. Clone o repositório recém-criado para sua máquina local:
```bash
git clone https://github.com/SEU_USUARIO/NOME_DO_NOVO_REPOSITORIO.git
cd NOME_DO_NOVO_REPOSITORIO
```

4. Crie e ative um ambiente virtual Python:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

5. Instale as dependências do projeto:
```bash
pip install -r requirements.txt
```

6. Execute os testes localmente:
```bash
pytest
pytest --html=reports/report.html # Com relatório HTML
```


## Estrutura do projeto

- `.github/workflows/` — pipeline do GitHub Actions 
- `features/` — arquivos Gherkin (.feature) (opcional)  
- `pages/` — Page Objects  
- `tests/` — scripts de teste  
- `utils/` — fixtures e configurações  
- `reports/` — relatórios gerados (não versionados)  
- `requirements.txt` — dependências  
- `.gitignore` — arquivos ignorados  
- `README.md` — documentação 


### `.github/workflows/`

Contém o arquivo de configuração do **GitHub Actions**, que executa os testes automaticamente em cada `push` ou `pull request` na branch `main`.

Neste template, o workflow:
- Faz checkout do código
- Cria o ambiente virtual
- Instala as dependências listadas no `requirements.txt`
- Executa os testes com o `pytest`
- (Opcional) Gera um relatório HTML dos testes e salva como artefato

### `features/`

Contém os arquivos **Gherkin (.feature)**, que descrevem cenários de teste no formato **BDD**.

- Esta pasta é **opcional**
- Instale o `pytest-bdd` no `requirements.txt`.
- Cada arquivo `.feature` descreve cenários em linguagem natural (Given, When, Then).
- Os testes em Python devem implementar os steps definidos nos `.feature`.



---