# labeling_automation
Automation of food labeling processes.

```markdown
# Labelrinty

**Labelrinty** é uma aplicação desktop feita em Python com interface gráfica para gerar etiquetas de manipulação e validade de alimentos, muito útil em Unidades de Alimentação e Nutrição (UAN). O sistema permite gerar etiquetas com datas automáticas (baseadas em categorias) ou inseridas manualmente, além de incluir texto personalizado.

## 🖼️ Exemplo de etiqueta
```

M: 26/06/2025
V: 29/06/2025
Atenção com a validade

````

## 🚀 Funcionalidades

- 📅 Geração automática de datas de validade com base na categoria:
  - Perecíveis (+3 dias)
  - Semi-perecíveis (+15 dias)
  - Não-perecíveis (+180 dias)
  - Dietas (DM, Branda) com lógica dia/noite
- ✍️ Inserção manual de datas (manipulação e validade)
- 🖨️ Geração de arquivo PDF com etiquetas prontas para impressão automática
- 💬 Campo de texto personalizado (exibido abaixo da validade)
- 🎨 Interface moderna com CustomTkinter
- 📅 Seletor de calendário para facilitar a entrada de datas

## 🛠️ Tecnologias utilizadas

- Python 3.9+
- [FPDF](https://pyfpdf.github.io/fpdf2/) – geração de PDF
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) – GUI moderna
- [tkcalendar](https://github.com/j4321/tkcalendar) – calendário para seleção de datas

## 📦 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/jnslnutridev/labeling_automation.git
   cd labelrinty
````

2. Crie um ambiente virtual (opcional mas recomendado):

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # ou .venv\\Scripts\\activate no Windows
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

    Ou manualmente:

    ```bash
    pip install fpdf customtkinter tkcalendar
    ```

## ▶️ Como usar

Execute o script principal:

```bash
python labelrinty.py
```

Na interface:

1. Escolha uma **categoria** de validade (ou selecione “Manual” para inserir as datas).
2. Preencha a **data de manipulação** (ou use o seletor).
3. Preencha a **data de validade** (se estiver no modo Manual).
4. Escreva um **texto personalizado** (opcional).
5. Clique em **Gerar Etiquetas**.

Um arquivo `etiquetas.pdf` será gerado com 56 etiquetas prontas para impressão.

## 📁 Estrutura das etiquetas no PDF

-   4 colunas por linha, 14 linhas por página.
-   Tamanho ideal para etiquetas pequenas (como 50mm x 25mm).
-   Cada etiqueta contém:

    -   Linha 1: Data de manipulação (M)
    -   Linha 2: Data de validade (V)
    -   Linha 3: Texto personalizado (opcional)

## 👨‍💻 Autor

Desenvolvido por **Jhonny (jnslnutridev)**
💼 Nutrição + Programação

## 📃 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

Feito com carinho para tornar o trabalho mais rápido e eficiente.
