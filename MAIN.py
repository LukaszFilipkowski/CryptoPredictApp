# ===============================
# IMPORTY
# ===============================

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
import numpy as np

# matplotlib do wykresu w GUI
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# ===============================
# GŁÓWNE OKNO
# ===============================

root = tk.Tk()
root.title("Crypto Oracle Analytics")
root.geometry("1200x650")

# ===============================
# GŁÓWNA RAMKA
# ===============================

main_frame = ttk.Frame(root, padding=10)
main_frame.pack(fill="both", expand=True)

# ===============================
# TYTUŁ
# ===============================

title = ttk.Label(
    main_frame,
    text="🔮 Crypto Oracle Analytics",
    font=("Arial", 22, "bold")
)
title.pack(pady=10)

# ===============================
# RAMKA NA TABELĘ + WYKRES
# ===============================

content_frame = ttk.Frame(main_frame)
content_frame.pack(fill="both", expand=True)

# dwie kolumny: tabela | wykres
content_frame.columnconfigure(0, weight=1)
content_frame.columnconfigure(1, weight=2)
content_frame.rowconfigure(0, weight=1)

# ===============================
# LEWA STRONA – TABELA
# ===============================

table_frame = ttk.Frame(content_frame)
table_frame.grid(row=0, column=0, sticky="nsew", padx=5)

# scrollbary
scroll_y = ttk.Scrollbar(table_frame, orient="vertical")
scroll_x = ttk.Scrollbar(table_frame, orient="horizontal")

# tabela
table = ttk.Treeview(
    table_frame,
    columns=("Time", "Value"),
    show="headings",
    yscrollcommand=scroll_y.set,
    xscrollcommand=scroll_x.set
)

table.heading("Time", text="Time")
table.heading("Value", text="Value")

table.column("Time", width=150)
table.column("Value", width=100)

scroll_y.config(command=table.yview)
scroll_x.config(command=table.xview)

# layout tabeli
table.grid(row=0, column=0, sticky="nsew")
scroll_y.grid(row=0, column=1, sticky="ns")
scroll_x.grid(row=1, column=0, sticky="ew")

table_frame.rowconfigure(0, weight=1)
table_frame.columnconfigure(0, weight=1)

# ===============================
# PRAWA STRONA – WYKRES
# ===============================

plot_frame = ttk.Frame(content_frame)
plot_frame.grid(row=0, column=1, sticky="nsew", padx=5)

# matplotlib Figure
fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)

ax.set_title("Wykres danych")
ax.set_xlabel("Time")
ax.set_ylabel("Value")

# canvas matplotlib w Tkinter
canvas = FigureCanvasTkAgg(fig, master=plot_frame)
canvas.draw()
canvas.get_tk_widget().pack(fill="both", expand=True)

# ===============================
# ZAŁADOWANIE DANYCH
# ===============================

def load_data():
    # 1️ wybór pliku
    file_path = filedialog.askopenfilename(
        title="Wybierz plik CSV",
        filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*"))
    )
    if not file_path:
        return  # kliknięto Anuluj
    
    # 2️ wczytanie CSV
    df = pd.read_csv(file_path, sep=';')
    # jeśli CSV ma więcej kolumn, bierzemy pierwsze dwie automatycznie
    time_col = df.columns[0]
    value_col = df.columns[1]

    # 3️ tabeli
    table.delete(*table.get_children())
    for _, row in df.iterrows():
        table.insert("", "end", values=(row[time_col], row[value_col]))

    # 4️ aktualizacja wykresu
    ax.clear()
    ax.plot(df[time_col], df[value_col])
    ax.set_title("Wykres danych")
    ax.set_xlabel(time_col)
    ax.set_ylabel(value_col)
    canvas.draw()
    canvas.get_tk_widget().update()

# ===============================
# PRZYCISKI
# ===============================

button_frame = ttk.Frame(main_frame)
button_frame.pack(pady=10)

load_btn = ttk.Button(button_frame, text="Wczytaj dane", command=load_data)
load_btn.pack(side="left", padx=10)

predict_btn = ttk.Button(button_frame, text="Predykcja (t+1)")
predict_btn.pack(side="left", padx=10)

# ===============================
# START APLIKACJI
# ===============================

root.mainloop()
