import sys
import subprocess
from pathlib import Path
from PIL import Image

def criar_venv():
    # Verificar se já existe uma venv
    venv_path = Path("venv")
    if not venv_path.exists():
        print("Criando ambiente virtual...")
        subprocess.run([sys.executable, "-m", "venv", str(venv_path)])
    else:
        print("Ambiente virtual já existe.")

def instalar_dependencias():
    print("Instalando dependências...")
    subprocess.run([str(Path("venv", "bin" if sys.platform != "win32" else "Scripts", "pip")), "install", "Pillow"])

def redimensionar_para_3x4(imagem_entrada, imagem_saida):
    # Dimensões desejadas para uma foto 3x4
    largura_desejada = 300
    altura_desejada = 400

    # Abre a imagem de entrada
    imagem = Image.open(imagem_entrada)

    # Redimensiona a imagem mantendo a proporção
    imagem_redimensionada = imagem.resize((largura_desejada, altura_desejada))

    # Salva a imagem redimensionada
    imagem_redimensionada.save(imagem_saida)

if __name__ == "__main__":
    # Criar ambiente virtual e instalar dependências
    criar_venv()
    instalar_dependencias()

    # Redimensionar imagem
    redimensionar_para_3x4('fotoOriginal.jpeg', 'saida.jpg')
