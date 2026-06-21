# Jogo da Cobrinha (Snake Game) em Python 🐍

Um jogo clássico da cobrinha desenvolvido inteiramente em Python utilizando a biblioteca **Pygame**. Este projeto foi criado com foco em praticar lógicas de colisão, manipulação de eventos, criação de telas e controle de estado do jogo.

## ✨ Funcionalidades

* **Gameplay Clássica:** Movimentação em grade com crescimento da cobra ao comer a maçã.
* **Sistema de Pontuação:** Placar atualizado em tempo real na tela.
* **Telas de Interface:**
  * Tela Inicial para aguardar o jogador começar.
  * Tela de *Game Over* informando a pontuação final.
* **Sistema de Reinício:** Opção de jogar novamente apertando `R` sem precisar reabrir o programa.
* **Prevenção de Bugs:** Bloqueio de "marcha ré" (impedir que a cobra vire 180 graus de uma vez e colida com o próprio pescoço).

## 🚀 Como executar o projeto

### Pré-requisitos
Certifique-se de ter o [Python](https://www.python.org/downloads/) instalado na sua máquina.

### Instalação

1. Clone este repositório ou baixe os arquivos.
2. Abra o terminal na pasta do projeto.
3. Instale a biblioteca necessária executando o comando de acordo com o seu sistema operacional:
  * **Windows e Linux:**
     ```
     pip install pygame
     ```
   * **macOS:**
     ```
     pip install pygame-ce
     ```
5. Inicie o jogo executando o arquivo principal:
   ```
   python main.py
   ```

### 🎮 Controles
Setas do Teclado (⬆️ ⬇️ ⬅️ ➡️): Controlam a direção da cobrinha.

Qualquer Tecla: Inicia a partida na tela inicial.

**R**: Reinicia o jogo na tela de Game Over.

**Q**: Sai do jogo na tela de Game Over.

### 🛠️ Tecnologias Utilizadas
**Python 3**

**Pygame (Biblioteca principal para renderização gráfica e eventos)**

Desenvolvido com dedicação e muito código! 💻
