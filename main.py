import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from in_code.player import PlayerPanel
from in_code.timeline import TimelinePanel
from in_code.media_panel import MediaPanel
from effects.edit_video import VideoEffectsPanel
from effects.edit_text import TextEffectsPanel
from effects.edit_image import ImageEffectsPanel

# === تحميل الأيقونة ===
def load_icon(name, size=None):
    path = f"assets/icons/{name}.png"
    if os.path.exists(path):
        icon = tk.PhotoImage(file=path)
        if size:
            icon = icon.subsample(size, size)
        return icon
    return None

# === قراءة ملف About ===
def show_about():
    if os.path.exists("about.txt"):
        with open("about.txt", "r", encoding="utf-8") as f:
            content = f.read()
    else:
        content = "QTZ Video Editor\nالإصدار: 0.1\nالكاتب: أنت!"
    messagebox.showinfo("About", content)

# === النافذة الرئيسية ===
root = tk.Tk()
root.title("QTZ VIDEO EDITOR")
root.geometry("1200x750")
root.configure(bg="#1e1e1e")

# ====== تحميل الأيقونة ======
icon_ico = "assets/icons/app_icon.ico"
icon_png = "assets/icons/app_icon.png"
if os.path.exists(icon_ico):
    root.iconbitmap(icon_ico)
elif os.path.exists(icon_png):
    icon_image = tk.PhotoImage(file=icon_png)
    root.iconphoto(False, icon_image)

# === Menu Bar ===
menubar = tk.Menu(root)
root.config(menu=menubar)

# === File Menu ===
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="New Project", accelerator="Ctrl+N", command=lambda: print("New Project"), image=load_icon("new", 2), compound="left")
file_menu.add_command(label="Open Project", accelerator="Ctrl+O", command=lambda: print("Open Project"), image=load_icon("open", 2), compound="left")
file_menu.add_separator()
file_menu.add_command(label="Exit", accelerator="Ctrl+Q", command=root.quit, image=load_icon("exit", 2), compound="left")
menubar.add_cascade(label="File", menu=file_menu)

# === Edit Menu ===
edit_menu = tk.Menu(menubar, tearoff=0)
edit_menu.add_command(label="Undo", accelerator="Ctrl+Z", image=load_icon("undo", 2), compound="left")
edit_menu.add_command(label="Redo", accelerator="Ctrl+Y", image=load_icon("redo", 2), compound="left")
menubar.add_cascade(label="Edit", menu=edit_menu)

# === Help Menu ===
help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="About", command=show_about, image=load_icon("about", 2), compound="left")
menubar.add_cascade(label="Help", menu=help_menu)

# === تقسيم الواجهة ===
main_frame = tk.Frame(root, bg="#1e1e1e")
main_frame.pack(fill="both", expand=True)

# === الجزء العلوي (Media / Player / Effects) ===
top_frame = tk.Frame(main_frame, bg="#1e1e1e")
top_frame.pack(fill="both", expand=True, padx=5, pady=(5,0))
top_frame.columnconfigure(0, weight=25)
top_frame.columnconfigure(1, weight=50)
top_frame.columnconfigure(2, weight=25)
top_frame.rowconfigure(0, weight=1)

media_panel = MediaPanel(top_frame)
media_panel.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

player_panel = PlayerPanel(top_frame)
player_panel.grid(row=0, column=2, sticky="nsew", padx=0, pady=2)


# --- نافذة التأثيرات مع تبويبات ---
effects_frame = tk.Frame(top_frame, bg="#2d2d2d")
effects_frame.grid(row=0, column=2, sticky="nsew", padx=2, pady=2)
notebook = ttk.Notebook(effects_frame)
notebook.pack(fill="both", expand=True)
notebook.add(VideoEffectsPanel(notebook), text="Video Effects")
notebook.add(TextEffectsPanel(notebook), text="Text")
notebook.add(ImageEffectsPanel(notebook), text="Image")

# === شريط أدوات Timeline ===
toolbar_frame = tk.Frame(main_frame, bg="#2d2d2d", height=40)
toolbar_frame.pack(fill="x", padx=5, pady=3)
for text in ["Cut","Copy","Paste","Delete","Zoom In","Zoom Out"]:
    btn = tk.Button(toolbar_frame, text=text, bg="#3c3c3c", fg="white", relief="flat")
    btn.pack(side="left", padx=3, pady=3)

# === الجزء السفلي (Timeline) ===
timeline_panel = TimelinePanel(main_frame)
timeline_panel.pack(fill="x", padx=5, pady=5)

root.bind("<Control-q>", lambda e: root.quit())
root.mainloop()
