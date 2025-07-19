#!/usr/bin/env python3
"""
SymBeat - Gerador de música simbólica determinística
Versão Python standalone do gerador usado no app web SymBeat

Autores: Gustavo Buhrer Sukevicz, Lira Kosmos, Stella Meira dos Santos (2025)
"""

import numpy as np
import io
import wave
import argparse
import os

try:
    from midiutil import MIDIFile
    MIDI_AVAILABLE = True
except ImportError:
    MIDI_AVAILABLE = False

def gen_beat(desc, style, dur, seed):
    """
    Gera uma música baseada nos parâmetros fornecidos
    
    Args:
        desc (str): Descrição da música
        style (str): Estilo musical (Trap, Drill, Coral, etc.)
        dur (int): Duração em segundos
        seed (int): Semente para geração determinística
        
    Returns:
        dict: Dicionário com dados WAV, MIDI e metadados
    """
    np.random.seed(seed)
    
    # Define BPM baseado no estilo
    bpm_map = {
        "Trap": 72,
        "Drill": 140,
        "Funk BR": 120,
        "Lofi": 78,
        "Bossa": 92,
        "Trance": 138,
        "Coral": 70,
        "Experimental": np.random.randint(60, 150)
    }
    bpm = bpm_map.get(style, 90)
    
    # Configuração básica
    sr = 22050  # Sample rate
    t = np.linspace(0, dur, int(sr*dur), endpoint=False)
    
    # Funções de síntese para bateria
    def kick(env=1.5, f0=60):
        envs = np.exp(-np.linspace(0, env, int(sr*0.15)))
        return 0.8 * envs * np.sin(2*np.pi*np.cumsum(f0*np.exp(-5*np.linspace(0, 1, int(sr*0.15)))/sr))
    
    def snare():
        n = np.random.randn(int(sr*0.09))
        env = np.exp(-np.linspace(0, 2.2, len(n)))
        return env * n * 0.5
    
    def hat():
        n = np.random.randn(int(sr*0.06))
        env = np.exp(-np.linspace(0, 10, len(n)))
        return env * n * 0.15
    
    # Geração de padrões rítmicos
    nbeats = int(bpm*dur/60)
    beat_t = sr*60/bpm
    audio = np.zeros_like(t)
    
    # Adiciona bateria
    for b in range(nbeats):
        pos = int(b*beat_t)
        if b % 4 == 0:
            audio[pos:pos+3300] += kick()[:3300]
        if b % 4 == 2:
            audio[pos:pos+1900] += snare()[:1900]
        if b % 2 == 0:
            audio[pos:pos+1300] += hat()[:1300]
    
    # Escolhe escala baseada no estilo
    if style in ["Trap", "Drill", "Funk BR"]:
        scale = [0, 3, 5, 7, 10]  # Escala menor pentatônica
    else:
        scale = [0, 2, 4, 5, 7, 9, 11]  # Escala maior
    
    # Nota raiz baseada na seed
    root = 30 + (seed % 12)
    
    # Adiciona linha de baixo
    for b in range(nbeats):
        note = root + scale[np.random.randint(len(scale))]
        start = int(b*beat_t)
        ln = int(beat_t*0.8)
        env = np.exp(-np.linspace(0, 3, ln))
        f = 2**((note-69)/12)*440
        audio[start:start+ln] += 0.16*env*np.sin(2*np.pi*f*np.arange(ln)/sr)
    
    # Adiciona melodia simples
    for b in range(nbeats//4):
        note = root+12 + scale[np.random.randint(len(scale))]
        pos = int(b*beat_t*4 + beat_t*2)
        ln = int(beat_t*2)
        env = np.exp(-np.linspace(0, 2.1, ln))
        f = 2**((note-69)/12)*440
        audio[pos:pos+ln] += 0.09*env*np.sin(2*np.pi*f*np.arange(ln)/sr)
    
    # Adiciona coral/pads se o estilo for "Coral"
    if style == "Coral":
        for i in range(3):
            f = [261, 329, 392][i]  # Frequências de um acorde maior
            env = np.exp(-np.linspace(0, 3, len(t)))
            audio += 0.08*env*np.sin(2*np.pi*f*t + np.random.rand()*6)
    
    # Normaliza o áudio
    audio = audio/np.max(np.abs(audio))*0.8
    
    # Gera arquivo WAV
    wav_buffer = io.BytesIO()
    wavef = wave.open(wav_buffer, 'wb')
    wavef.setnchannels(1)
    wavef.setsampwidth(2)
    wavef.setframerate(sr)
    wavef.writeframes((audio*32767).astype('<i2').tobytes())
    wavef.close()
    
    # Gera arquivo MIDI se disponível
    midi_buffer = None
    if MIDI_AVAILABLE:
        midi_buffer = io.BytesIO()
        mf = MIDIFile(1)
        mf.addTempo(0, 0, bpm)
        
        # Adiciona notas ao MIDI
        for b in range(nbeats):
            note = root + scale[np.random.randint(len(scale))]
            mf.addNote(0, 0, note, b*60/bpm, 60/bpm, 90)
        
        mf.writeFile(midi_buffer)
    
    return {
        "wav_buffer": wav_buffer,
        "midi_buffer": midi_buffer,
        "meta": {
            "bpm": bpm,
            "sr": sr,
            "desc": desc,
            "style": style,
            "seed": seed
        }
    }

def get_seed_from_string(s):
    """Gera uma seed determinística a partir de uma string"""
    h = 5381
    for c in s:
        h = ((h << 5) + h) + ord(c)
    return abs(h % 4294967295)

def main():
    parser = argparse.ArgumentParser(description='SymBeat - Gerador de música simbólica')
    parser.add_argument('--desc', type=str, default='Trap com baixo forte', help='Descrição da música')
    parser.add_argument('--style', type=str, default='Trap', 
                        choices=['Trap', 'Drill', 'Coral', 'Funk BR', 'Lofi', 'Bossa', 'Trance', 'Experimental'],
                        help='Estilo musical')
    parser.add_argument('--dur', type=int, default=15, help='Duração em segundos')
    parser.add_argument('--seed', type=int, default=None, help='Seed para geração determinística')
    parser.add_argument('--output', type=str, default='symbeat_output', help='Prefixo para arquivos de saída')
    
    args = parser.parse_args()
    
    # Se não for fornecida uma seed, gera uma a partir da descrição e estilo
    if args.seed is None:
        args.seed = get_seed_from_string(f"{args.desc}|{args.style}|{args.dur}")
    
    print(f"Gerando música com os seguintes parâmetros:")
    print(f"  Descrição: {args.desc}")
    print(f"  Estilo: {args.style}")
    print(f"  Duração: {args.dur}s")
    print(f"  Seed: {args.seed}")
    
    # Gera a música
    result = gen_beat(args.desc, args.style, args.dur, args.seed)
    
    # Salva o arquivo WAV
    wav_path = f"{args.output}.wav"
    with open(wav_path, 'wb') as f:
        f.write(result['wav_buffer'].getvalue())
    print(f"Arquivo WAV salvo em: {os.path.abspath(wav_path)}")
    
    # Salva o arquivo MIDI se disponível
    if result['midi_buffer']:
        midi_path = f"{args.output}.mid"
        with open(midi_path, 'wb') as f:
            f.write(result['midi_buffer'].getvalue())
        print(f"Arquivo MIDI salvo em: {os.path.abspath(midi_path)}")
    else:
        print("Biblioteca MIDIUtil não encontrada. Arquivo MIDI não gerado.")
    
    print("\nMetadados da música gerada:")
    print(f"  BPM: {result['meta']['bpm']}")
    print(f"  Sample Rate: {result['meta']['sr']}")

if __name__ == "__main__":
    main()