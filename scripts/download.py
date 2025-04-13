import ftplib
import os
from datetime import datetime

def download_latest_file():
    try:
        ftp = ftplib.FTP('ftp.bmf.com.br')
        ftp.login()
        
        # Ajuste o caminho conforme necessário
        ftp.cwd('MarketData/Bovespa-Vista/')
        
        files = ftp.nlst()
        # Filtra arquivos de opções (ajuste o filtro)
        option_files = [f for f in files if 'OPCOES' in f and '.TXT' in f]
        
        if not option_files:
            raise Exception("Nenhum arquivo de opções encontrado")
        
        # Pega o arquivo mais recente (simplificado)
        latest_file = sorted(option_files)[-1]
        
        # Cria diretório se não existir
        os.makedirs('../data', exist_ok=True)
        
        # Baixa o arquivo
        with open(f'../data/{latest_file}', 'wb') as f:
            ftp.retrbinary(f'RETR {latest_file}', f.write)
        
        return latest_file
    
    finally:
        ftp.quit()

if __name__ == "__main__":
    downloaded_file = download_latest_file()
    print(f"Arquivo baixado: {downloaded_file}")
