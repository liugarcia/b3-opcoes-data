import pandas as pd
import json
import glob
import os

def process_to_json():
    # Encontra o arquivo mais recente baixado
    files = glob.glob('../data/*.TXT') or glob.glob('../data/*.txt')
    if not files:
        raise FileNotFoundError("Nenhum arquivo de dados encontrado")
    
    latest_file = max(files, key=os.path.getctime)
    
    # Lê o arquivo (ajuste o delimitador e encoding conforme necessário)
    df = pd.read_csv(latest_file, delimiter='@', encoding='iso-8859-1')
    
    # Processamento básico (ajuste conforme seus needs)
    processed_data = []
    
    # Exemplo de transformação - ajuste para o formato real dos dados
    for _, row in df.iterrows():
        processed_data.append({
            'ativo': row.get('CODBDI', ''),
            'tipo': row.get('TPREC', ''),
            'preco': row.get('PREEXE', ''),
            'strike': row.get('PREEXE', ''),  # Ajuste para coluna correta
            'vencimento': row.get('DATVEN', ''),
            'volume': row.get('QUATOT', '')
        })
    
    # Salva como JSON
    output_path = '../data/opcoes.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump({
            'ultima_atualizacao': pd.Timestamp.now().isoformat(),
            'dados': processed_data
        }, f, ensure_ascii=False, indent=2)
    
    return output_path

if __name__ == "__main__":
    output_file = process_to_json()
    print(f"Dados processados salvos em: {output_file}")
