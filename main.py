from chaeruldesktop.app_desktop import *

input_ = {}

def input_username(parent):
    entry = inputView(
        parent,
        icon="icon/circle-user.png",
        placeholder="Masukkan username",
        width=250,
        height=35,
        border=2,
        textColor="black",
        fontSize=12,
        borderColor='black'
    )
    entry.pack(pady=10)
    input_["username"] = entry
    return entry


def input_password(parent):
    entry = inputView(
        parent,
        icon="icon/lock.png",
        eyeIcon=True,
        placeholder="Masukkan password",
        width=250,
        height=35,
        border=2,
        textColor="black",
        fontSize=12,
        show="*",
        borderColor='black'
    )
    # entry.configure(show="*")
    entry.pack(pady=10)
    input_["username"] = entry
    return entry


def on_ready(inputs):
    print("Form ready!")
    print("Input username widget:", inputs.get("username"))

appDesktop(
    title="Kasir Desktop",
    width=400,
    height=600,
    on_ready=on_ready,
    align='center',
    body=[
        lambda parent: ImageViewPilLow(parent, "kasir.png", width=100, height=100),
        lambda parent: textView(parent, "Masuk akun anda", fontSize=16),
        lambda parent: textView(parent, "Username", fontSize=12).pack(anchor='w'),
        input_username,
        lambda parent: textView(parent, "Password", fontSize=12).pack(anchor='w'),
        input_password,
        lambda parent: buttonView(
            parent,
            "Login",
            radius=10,
            width=300,
            backgroundColor=Colors()['success'],
            textColor="white",
            command=safe_callback(lambda: print("Username:", input_["username"].get()))
        ),
        lambda parent: textView(parent, "Belum punya akun? Daftar disini", fontSize=10, textColor='red').pack(pady=10)
    ]
)
