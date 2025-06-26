import os as o
import sys
from datetime import datetime as D, timedelta as T
from fpdf import FPDF as P
import customtkinter as ctk
from tkinter import messagebox
from tkcalendar import Calendar

# Configuração do Tema
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# Funções de pré-definições de etiquetas
def calcular_data_predefinida(categoria):
    hoje = D.now()
    if categoria == "Perecíveis":
        return hoje, hoje + T(days=3)
    elif categoria == "Semi-perecíveis":
        return hoje, hoje + T(days=15)
    elif categoria == "Não-perecíveis":
        return hoje, hoje + T(days=180)
    elif categoria == "DM-dia":
        return hoje, hoje + T(days=1)
    elif categoria == "DM-noite":
        return hoje + T(days=1), hoje + T(days=2)
    elif categoria == "Branda-dia":
        return hoje, hoje + T(days=1)
    elif categoria == "Branda-noite":
        return hoje + T(days=1), hoje + T(days=2)
    else:
        return hoje, hoje + T(days=1)

# Função de configuração das etiquetas no PDF
def configurar_campos_pagina(data_manipulacao, data_validade, texto_personalizado="", categoria=""):
    pdf = P(orientation='P', unit='mm', format='A4')
    pdf.set_auto_page_break(auto=False)
    pdf.add_page()

    pdf.set_font("Arial", size=10)
    largura_pagina = 210
    margem = 10
    largura_etq = (largura_pagina - 2 * margem) / 4
    altura_etq = 15
    espac_v = 5

    x, y = margem, 15
    for _ in range(14):
        for _ in range(4):
            pdf.set_xy(x, y)
            # Sempre exibe M, V, e depois texto personalizado em linhas separadas
            pdf.cell(w=largura_etq, h=5, txt=f"M: {data_manipulacao}", border=0, ln=2, align='C')
            pdf.set_font("Arial", size=10)
            pdf.cell(w=largura_etq, h=5, txt=f"V: {data_validade}", border=0, ln=2, align='C')
            if texto_personalizado:
                pdf.cell(w=largura_etq, h=5, txt=texto_personalizado, border=0, ln=2, align='C')
            x += largura_etq
        x = margem
        y += altura_etq + espac_v
    pdf.output("etiquetas.pdf")

# Geração de etiquetas com suporte a manual ou predefinido
def gerar_etiquetas(data_manipulacao_str, data_validade_str, texto_personalizado, categoria):
    try:
        if categoria == "Manual":
            # Usa datas informadas manualmente
            hoje = D.strptime(data_manipulacao_str, "%d/%m/%Y")
            validade = D.strptime(data_validade_str, "%d/%m/%Y")
        elif categoria != "Padrão":
            hoje, validade = calcular_data_predefinida(categoria)
        else:
            # Padrão: manip=hoje, validade = +1 dia
            hoje = D.now()
            validade = hoje + T(days=1)

        m_str = hoje.strftime("%d/%m/%Y")
        v_str = validade.strftime("%d/%m/%Y")
        configurar_campos_pagina(m_str, v_str, texto_personalizado, categoria)
        messagebox.showinfo("Sucesso", "Etiquetas geradas com sucesso!")
        o.startfile("etiquetas.pdf", "print") # envia para immpressão automaticamente
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao gerar etiquetas: {e}")

# Seleção de data por calendário
def selecionar_data(entry):
    def confirmar():
        sel = cal.selection_get().strftime("%d/%m/%Y")
        entry.delete(0, 'end')
        entry.insert(0, sel)
        popup.destroy()
    popup = ctk.CTkToplevel(app)
    popup.title("Selecione a Data")
    popup.geometry(f"+{app.winfo_x()+50}+{app.winfo_y()+50}")
    popup.transient(app)
    popup.grab_set(); popup.focus_force()
    cal = Calendar(popup, selectmode='day', year=D.now().year, month=D.now().month, day=D.now().day)
    cal.pack(pady=10)
    btn = ctk.CTkButton(popup, text="Confirmar", command=confirmar)
    btn.pack(pady=5)

# Fechar app
def on_closing():
    if messagebox.askokcancel("Sair", "Deseja sair?"):
        app.destroy(); sys.exit(0)

# Interface gráfica atualizada
def criar_interface():
    global app, dt_manip_entry, dt_valid_entry, texto_entry, categoria_var
    app = ctk.CTk()
    app.title("Labelrinty - Gerador de Etiquetas")
    app.geometry("500x550")

    # Cabeçalho
    ctk.CTkLabel(app, text="Labelrinty - Gerador de Etiquetas", font=("Arial", 24)).pack(pady=(10,5))
    ctk.CTkLabel(app, text="Selecione um padrão ou insira datas manualmente:", font=("Arial", 14)).pack()

    # Categoria ou manual
    categoria_var = ctk.StringVar(value="Padrão")
    valores = ["Padrão", "Perecíveis", "Semi-perecíveis", "Não-perecíveis",
               "DM-dia", "DM-noite", "Branda-dia", "Branda-noite", "Manual"]
    ctk.CTkOptionMenu(app, variable=categoria_var, values=valores).pack(pady=10)

    # Data de manipulação
    ctk.CTkLabel(app, text="Data de Manipulação (dia/mês/ano):").pack(pady=(15,2))
    dt_manip_entry = ctk.CTkEntry(app, placeholder_text="dd/mm/AAAA", width=200)
    dt_manip_entry.pack()
    ctk.CTkButton(app, text="Selecionar", command=lambda: selecionar_data(dt_manip_entry)).pack(pady=2)

    # Data de validade (manual)
    ctk.CTkLabel(app, text="Data de Validade (dia/mês/ano):").pack(pady=(15,2))
    dt_valid_entry = ctk.CTkEntry(app, placeholder_text="dd/mm/AAAA", width=200)
    dt_valid_entry.pack()
    ctk.CTkButton(app, text="Selecionar", command=lambda: selecionar_data(dt_valid_entry)).pack(pady=2)

    # Texto personalizado
    ctk.CTkLabel(app, text="Texto Personalizado (opcional):").pack(pady=(15,2))
    texto_entry = ctk.CTkEntry(app, placeholder_text="Insira uma mensagem, um aviso...", width=300)
    texto_entry.pack(pady=5)

    # Botão gerar
    ctk.CTkButton(app, text="Gerar Etiquetas",
                  command=lambda: gerar_etiquetas(
                      dt_manip_entry.get(), dt_valid_entry.get(), texto_entry.get(), categoria_var.get()
                  )).pack(pady=20)

    # Rodapé
    ctk.CTkLabel(app, text="Criado por Jhonny (jnslnutridev) - 2024", font=("Arial", 14)).pack(side='bottom', pady=10)
    app.protocol("WM_DELETE_WINDOW", on_closing)
    app.mainloop()

if __name__ == "__main__":
    criar_interface()
