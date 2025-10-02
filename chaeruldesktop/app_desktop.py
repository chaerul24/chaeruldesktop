import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from customtkinter import CTkImage
import time
import tkinter.messagebox as messagebox
from PIL import Image, ImageTk
import traceback

def config(title, width=0, height=0):
    root = tk.Tk()
    root.title(title)
    if width > 0 and height > 0:
        root.geometry(f"{width}x{height}")
    else:
        root.state('zoomed')
    return root

def textView(parent, text, textColor='black', fontSize=10, fontFamily="Arial"):
    return tk.Label(parent, text=text, font=(fontFamily, fontSize), fg=textColor)
def safe_callback(callback):
    def wrapper(*args, **kwargs):
        try:
            return callback(*args, **kwargs)
        except Exception as e:
            now = time.strftime('%H:%M:%S')
            print(f"[{now}] Error di callback:\n{traceback.format_exc()}")

            # Tampilkan popup juga jika mau
            messagebox.showerror("Terjadi Error", f"{type(e).__name__}: {str(e)}")
    return wrapper
def Colors():
    return {
        'primary': '#0d6efd',
        'secondary': '#6c757d',
        'success': '#198754',
        'danger': '#dc3545',
        'warning': '#ffc107',
        'info': '#0dcaf0',
        'light': '#f8f9fa',
        'dark': '#212529'
    }

def buttonView(parent, text="Click", backgroundColor=None, textColor="white", radius=10, width=120, height=40, command=None):
    colors = Colors()
    bg = backgroundColor if backgroundColor else colors['primary']
    # Buat hover color lebih gelap sedikit (atau tetap manual)
    hover = "#0b5ed7" if not backgroundColor else backgroundColor  # kamu bisa bikin logic lebih kompleks untuk hover

    return ctk.CTkButton(
        parent,
        text=text,
        width=width,
        height=height,
        corner_radius=radius,
        fg_color=bg,
        hover_color=hover,
        text_color=textColor,
        command=command
    )



def progressView(parent, length=100, max=100, value=20, mode='determinate', orient='horizontal'):
    return ttk.Progressbar(
        parent,
        length=length,
        mode=mode,
        orient=orient,
        maximum=max,
        value=value
    )

def styleInput(width, backgroundColor=None, border=2, textColor='white', fontFamily="Arial", fontSize=10, relief='groove'):
    style = {
        'width': width,
        'fg': textColor,
        'font': (fontFamily, fontSize),
        'bd': border,
        'relief': relief
    }
    if backgroundColor is not None:
        style['bg'] = backgroundColor
    return style
def inputView(
    parent,
    icon=None,
    eyeIcon=False,
    placeholder="",
    width=200,
    height=30,
    textColor="black",
    backgroundIconColor=None,
    borderColor=None,
    border=1,
    fontSize=12,
    radius=6,
    show=None
):
    frame = ctk.CTkFrame(parent, fg_color="transparent")

    # Kurangi width jika ada eyeIcon supaya totalnya tidak terlalu besar
    if eyeIcon:
        width -= 30  # sesuaikan dengan lebar tombol mata

    # Ikon kiri
    if icon is not None:
        try:
            pil_img = Image.open(icon)
            img = CTkImage(pil_img, size=(20, 20))
            label_icon = ctk.CTkLabel(frame, image=img, text="")
            label_icon.image = img
            label_icon.pack(side="left", padx=(0, 10))
        except Exception as e:
            print("Gagal load icon:", e)

    # Entry field
    entry_var = tk.StringVar()
    entry = ctk.CTkEntry(
        frame,
        textvariable=entry_var,
        placeholder_text=placeholder,
        width=width,
        height=height,
        corner_radius=radius,
        border_width=border,
        border_color=borderColor,
        fg_color=backgroundIconColor,
        text_color=textColor,
        font=("Arial", fontSize),
        show=show
    )
    entry.pack(side="left", fill="x", expand=True)

    # Tombol toggle mata (eye icon)
    if eyeIcon:
        show_state = {"visible": False}

        try:
            eye_open = CTkImage(Image.open("icon/eye.png"), size=(20, 20))
            eye_closed = CTkImage(Image.open("icon/crossed-eye.png"), size=(20, 20))
        except Exception as e:
            print("Gagal load icon mata:", e)
            eye_open = eye_closed = None

        def toggle_show():
            if show_state["visible"]:
                entry.configure(show="*")
                if eye_button and eye_closed:
                    eye_button.configure(image=eye_closed)
            else:
                entry.configure(show="")
                if eye_button and eye_open:
                    eye_button.configure(image=eye_open)
            show_state["visible"] = not show_state["visible"]

        eye_button = ctk.CTkButton(
            frame,
            text="",
            width=30,
            height=30,
            fg_color="transparent",
            hover=False,
            image=eye_closed,
            command=toggle_show
        )
        eye_button.pack(side="left", padx=(5, 0))

    frame.entry = entry
    return frame




def ImageViewPilLow(parent, image_path, width=100, height=100, top=5, bottom=5, left=5, right=5):
    pil_image = Image.open(image_path)
    pil_image = pil_image.resize((width, height))
    img = ImageTk.PhotoImage(pil_image)
    label = tk.Label(parent, image=img)
    label.image = img
    label._padding = {'padx': (left, right), 'pady': (top, bottom)}
    return label

def appDesktop(title="App", width=400, height=600, body=[], on_ready=None, align='start'):
    input_ = {}

    try:
        root = tk.Tk()
        root.title(title)
        root.geometry(f"{width}x{height}")

        frame = tk.Frame(root)
        frame.pack(fill='both', expand=True)

        if align == 'center':
            container = tk.Frame(frame)
            container.place(relx=0.5, rely=0.5, anchor='center')
            for builder in body:
                widget = builder(container)
                if isinstance(widget, tk.Widget):
                    widget.pack(pady=5)

        elif align in ('center|start', 'start|center', 'top|center', 'center|top'):
            container = tk.Frame(frame)
            container.pack(fill='x', side='top')
            for builder in body:
                widget = builder(container)
                if isinstance(widget, tk.Widget):
                    widget.pack(anchor='center', pady=5)

        elif align in ('center|end', 'end|center', 'bottom|center', 'center|bottom'):
            container = tk.Frame(frame)
            container.pack(fill='x', side='bottom')
            for builder in body:
                widget = builder(container)
                if isinstance(widget, tk.Widget):
                    widget.pack(anchor='center', pady=5)

        elif align in ('left|center', 'center|left'):
            container = tk.Frame(frame)
            container.place(relx=0, rely=0.5, anchor='w')
            for builder in body:
                widget = builder(container)
                if isinstance(widget, tk.Widget):
                    widget.pack(anchor='w', pady=5)

        elif align in ('right|center', 'center|right'):
            container = tk.Frame(frame)
            container.place(relx=1, rely=0.5, anchor='e')
            for builder in body:
                widget = builder(container)
                if isinstance(widget, tk.Widget):
                    widget.pack(anchor='e', pady=5)

        elif align == 'end':
            container = tk.Frame(frame)
            container.pack(fill='both', expand=True)
            bottom_right = tk.Frame(container)
            bottom_right.pack(side='bottom', anchor='e', padx=10, pady=10)
            for builder in body:
                widget = builder(bottom_right)
                if isinstance(widget, tk.Widget):
                    widget.pack(anchor='e', pady=5)

        else:  # default 'start' dan fallback lainnya
            for builder in body:
                widget = builder(frame)
                if isinstance(widget, tk.Widget):
                    widget.pack(side='top', anchor='w', padx=10, pady=5)

        # Callback jika ada fungsi on_ready
        if callable(on_ready):
            on_ready(input_)

        root.mainloop()

    except Exception as e:
        now = time.strftime('%H:%M:%S')
        print(f"[{now}] Pesan Error :", e)