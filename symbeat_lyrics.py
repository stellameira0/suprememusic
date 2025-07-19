#!/usr/bin/env python3
"""
SymBeat Lyrics - Gerador de letras simbólico determinístico
Versão Python standalone do gerador usado no app web SymBeat

Autores: Gustavo Buhrer Sukevicz, Lira Kosmos, Stella Meira dos Santos (2025)
"""

import random
import argparse
import os

def generate_lyrics(seed="amor e rua", style="Trap", length=8):
    """
    Gera letras de música baseadas nos parâmetros fornecidos
    
    Args:
        seed (str): Tema ou semente para geração
        style (str): Estilo musical (Trap, Lofi, Funk BR, etc.)
        length (int): Número de versos a serem gerados
        
    Returns:
        str: Letra gerada
    """
    # Usa uma seed determinística baseada na combinação de tema e estilo
    random.seed(hash(seed + style) % (10**8))
    
    # Dicionário de palavras por estilo
    bases = {
        "Trap": ["yeah", "mano", "fogo", "cash", "no beat", "flow", "droga", "chama", "rua", "noite", "vida", "luta"],
        "Lofi": ["chuva", "vento", "calma", "tempo", "janela", "voz", "silêncio", "vibe", "sonho", "memória", "café", "livro"],
        "Funk BR": ["bumbum", "favela", "batida", "sequência", "tudo nosso", "no bailão", "pancadão", "baile", "noite", "gata", "mano"],
        "Coral": ["luz", "eterno", "céu", "chama", "voz", "glória", "eco", "vida", "alma", "espírito", "caminho", "verdade"],
        "Bossa": ["mar", "amor", "sol", "praia", "saudade", "beleza", "coração", "olhar", "canção", "poesia", "cidade", "tarde"],
        "Trance": ["mente", "viagem", "universo", "energia", "pulso", "ritmo", "infinito", "luz", "tempo", "espaço", "dimensão"],
        "Experimental": ["caos", "ruído", "silêncio", "fragmento", "abstrato", "concreto", "digital", "analógico", "distorção", "glitch"]
    }
    
    # Palavras conectoras e verbos para enriquecer a geração
    conectores = ["e", "com", "sem", "no", "na", "do", "da", "que", "pra", "pro", "como", "quando"]
    verbos = ["sinto", "vejo", "ouço", "penso", "sonho", "vivo", "morro", "canto", "danço", "corro", "paro", "sigo"]
    
    # Usa o vocabulário do estilo selecionado ou default para Trap
    palavras = bases.get(style, bases["Trap"])
    versos = []
    
    # Gera os versos com variações de estrutura
    for i in range(length):
        if i % 4 == 0 and i > 0:  # Adiciona um refrão a cada 4 versos
            verso = f"{random.choice(palavras).upper()} {random.choice(palavras).upper()}!"
        elif random.random() < 0.3:  # 30% de chance de verso com estrutura verbo + conector + substantivo
            verso = f"{random.choice(verbos)} {random.choice(conectores)} {random.choice(palavras)}"
        else:  # Verso padrão com 3 palavras
            verso = f"{random.choice(palavras)} {random.choice(conectores)} {random.choice(palavras)}"
        
        # Adiciona variações ocasionais
        if random.random() < 0.2:
            verso += f", {random.choice(palavras)}"
        if random.random() < 0.1:
            verso = verso.upper()  # Ocasionalmente coloca tudo em maiúsculas para ênfase
            
        versos.append(verso.capitalize())
    
    # Adiciona um verso final com repetição para fechamento
    final_word = random.choice(palavras)
    versos.append(f"{final_word}, {final_word}... {final_word}.")
    
    return "\n".join(versos)

def get_seed_from_string(s):
    """Gera uma seed determinística a partir de uma string"""
    h = 5381
    for c in s:
        h = ((h << 5) + h) + ord(c)
    return abs(h % 4294967295)

def main():
    parser = argparse.ArgumentParser(description='SymBeat Lyrics - Gerador de letras simbólico')
    parser.add_argument('--theme', type=str, default='amor e rua', help='Tema para a letra')
    parser.add_argument('--style', type=str, default='Trap', 
                        choices=['Trap', 'Lofi', 'Funk BR', 'Coral', 'Bossa', 'Trance', 'Experimental'],
                        help='Estilo musical')
    parser.add_argument('--length', type=int, default=8, help='Número de versos')
    parser.add_argument('--output', type=str, default=None, help='Arquivo de saída (opcional)')
    
    args = parser.parse_args()
    
    print(f"Gerando letra com os seguintes parâmetros:")
    print(f"  Tema: {args.theme}")
    print(f"  Estilo: {args.style}")
    print(f"  Versos: {args.length}")
    
    # Gera a letra
    lyrics = generate_lyrics(args.theme, args.style, args.length)
    
    # Exibe a letra gerada
    print("\n--- LETRA GERADA ---\n")
    print(lyrics)
    print("\n-------------------\n")
    
    # Salva em arquivo se solicitado
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(lyrics)
        print(f"Letra salva em: {os.path.abspath(args.output)}")

if __name__ == "__main__":
    main()