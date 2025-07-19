# 🎧 SymBeat – Música e Letras IA 100% Local

SymBeat é uma aplicação web que permite gerar música e letras usando IA de forma 100% local, sem necessidade de conexão com servidores externos. A aplicação roda diretamente no navegador utilizando Pyodide para executar código Python.

## 🎵 Funcionalidades

### 🎼 Geração de Música
- **Geração de música** baseada em descrições textuais
- **Seleção de estilos musicais** (Trap, Drill, Coral, Funk BR, Lofi, Bossa, Trance, Experimental)
- **Controle de duração** da música (10-30 segundos)
- **Exportação em formato WAV e MIDI**

### 🎤 Geração de Letras
- **Geração de letras** baseada em temas e inspirações
- **Múltiplos estilos** (Trap, Drill, Funk BR, Lofi, Bossa, Coral)
- **Controle de quantidade** de versos (4-20 linhas)
- **Exportação em formato TXT**
- **Cópia para área de transferência**

### 🎯 Funcionalidades Avançadas
- **Modo Completo**: Gera música + letras simultaneamente
- **Interface com abas** para diferentes modos de uso
- **Visualização do código Python** utilizado
- **Compartilhamento via Base91** para distribuição compacta
- **Geração de QR Code** com a aplicação embutida
- **Controle do número de versos** a serem gerados
- **Exportação em formato TXT**
- **Visualização do código Python** utilizado para gerar as letras

## 🚀 Como Usar

### Gerador de Música
1. Acesse `index.html` para o gerador de música
2. Descreva a vibe ou gênero musical desejado
3. Selecione um estilo musical predefinido
4. Ajuste a duração desejada
5. Clique em "Gerar" para criar sua música
6. Use os botões para ouvir, exportar ou compartilhar sua criação

### Gerador de Letras
1. Acesse `lyrics.html` para o gerador de letras
2. Descreva o tema da letra
3. Selecione um estilo musical predefinido
4. Ajuste o número de versos desejado
5. Clique em "Gerar Letra" para criar sua letra
6. Use os botões para copiar, exportar ou visualizar o código

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