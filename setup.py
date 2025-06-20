from setuptools import setup, find_packages

setup(
    name="ASCII_Terminal_art",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=2.2.6",
        "opencv-python>=4.11.0.86"
    ],
    author="Gabriel Rocha de Souza",
    author_email="souza.gabriel.0210@gmail.com",
    description="Codes used for display ascii art in terminal",
    url="https://github.com/Gabriel-br2/ASCII_Terminal_art.git"
)
