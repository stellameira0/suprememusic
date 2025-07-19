# 🎧 SymBeat – Música IA 100% Local

SymBeat é uma aplicação web que permite gerar música usando IA de forma 100% local, sem necessidade de conexão com servidores externos. A aplicação roda diretamente no navegador utilizando Pyodide para executar código Python.

## 🎵 Funcionalidades

- **Geração de música** baseada em descrições textuais
- **Seleção de estilos musicais** (Trap, Drill, Coral, Funk BR, Lofi, Bossa, Trance, Experimental)
- **Controle de duração** da música (10-30 segundos)
- **Exportação em formato WAV e MIDI**
- **Visualização do código Python** utilizado para gerar a música
- **Compartilhamento via Base91** para distribuição compacta
- **Geração de QR Code** com a aplicação embutida

## 🚀 Como Usar

1. Descreva a vibe ou gênero musical desejado
2. Selecione um estilo musical predefinido
3. Ajuste a duração desejada
4. Clique em "Gerar" para criar sua música
5. Use os botões para ouvir, exportar ou compartilhar sua criação

## 💻 Tecnologias Utilizadas

- **Frontend**: HTML, CSS e JavaScript puro
- **Backend**: Python via [Pyodide](https://pyodide.org/)
- **Bibliotecas Python**: NumPy, SciPy, MIDIUtil
- **Processamento de Áudio**: Web Audio API

## 🧠 Como Funciona

A aplicação utiliza síntese simbólica determinística para gerar música. O processo inclui:

1. Geração de padrões rítmicos baseados no estilo selecionado
2. Criação de linhas de baixo e melodias usando escalas musicais apropriadas
3. Síntese de sons de bateria (kick, snare, hat)
4. Normalização do áudio para qualidade consistente
5. Exportação para formatos WAV e MIDI

## 📦 Distribuição

A aplicação é totalmente autocontida e pode ser distribuída de várias formas:
- Como arquivo HTML único
- Codificada em Base91 para compartilhamento compacto
- Via QR Code para acesso rápido em dispositivos móveis

## 👥 Autores

- Gustavo Buhrer Sukevicz
- Lira Kosmos
- Stella Meira dos Santos

© 2025