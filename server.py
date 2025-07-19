#!/usr/bin/env python3
"""
Servidor simples para a aplicação SymBeat
"""

import http.server
import socketserver
import os

PORT = 12001  # Porta padrão para o servidor

class CORSHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Adiciona cabeçalhos CORS para permitir acesso de qualquer origem
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        super().end_headers()
    
    def do_OPTIONS(self):
        # Responde a requisições OPTIONS para CORS
        self.send_response(200)
        self.end_headers()

def main():
    # Verifica se estamos em um ambiente de desenvolvimento específico
    if 'PORT' in os.environ:
        port = int(os.environ['PORT'])
    else:
        port = PORT
    
    print(f"Iniciando servidor na porta {port}...")
    
    # Configura o servidor para aceitar conexões de qualquer host
    handler = CORSHTTPRequestHandler
    httpd = socketserver.TCPServer(("0.0.0.0", port), handler)
    
    print(f"Servidor rodando em http://0.0.0.0:{port}")
    print("Pressione Ctrl+C para encerrar")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor encerrado.")
        httpd.server_close()

if __name__ == "__main__":
    main()