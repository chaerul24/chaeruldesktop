from setuptools import setup, find_packages

setup(
    name="chaeruldesktop",
    version="0.1.0",
    author="Chaerul",
    description="Komponen GUI sederhana berbasis CustomTkinter untuk aplikasi desktop Python",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/chaerul24/chaeruldesktop",  # Ganti dengan URL GitHub kamu
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "customtkinter",
        "pillow"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3.7',
)

