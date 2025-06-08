# macacoBalao

## Bloons Tower Defense em Python com OpenGL

Esse é um projeto pessoal de um jogo estilo **Bloons Tower Defense** feito com Python, usando **PyOpenGL** e **GLFW**. A ideia é simples: posicionar torres, estourar balões e tentar sobreviver o maior tempo possível.

---

## O que o jogo já tem

* Interface com gráficos em OpenGL
* Sistema de *waves* com balões que ficam mais difíceis com o tempo
* Várias torres diferentes, cada uma com seu alcance, dano e tempo de recarga
* Balões com diferentes aparências, velocidades e quantidade de vida
* Sistema de dinheiro: ganha ao estourar balões e gasta ao colocar torres
* Perda de vidas se balões chegarem até o fim do trajeto
* HUD interativo para escolher e posicionar torres com o mouse
* Menu inicial com seleção de mapa (em construção)

---

## 🛠Como rodar

### Requisitos:

* Python 3.10 ou superior
* GLFW
* PyOpenGL
* Pillow

### Para instalar as dependências:

```bash
pip install PyOpenGL PyOpenGL_accelerate glfw Pillow
```

### Depois é só rodar:

```bash
python main.py
```

---

## Próximos passos

* Finalizar o menu de escolha de mapas
* Adicionar sistema de upgrade para as torres
* Efeitos sonoros (explosão dos balões, clique, etc)
* Melhorar balanceamento das waves
* Salvar pontuação ou progresso

---

## Sobre o projeto

Esse jogo foi feito com o objetivo de aprender mais sobre gráficos 3D, renderização em tempo real e estruturas de jogo em Python. Foi inspirado no clássico **Bloons Tower Defense**, mas com uma pegada mais simples e 100% feita do zero com PyOpenGL.
