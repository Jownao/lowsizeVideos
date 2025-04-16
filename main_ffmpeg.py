# Funciona perfeitamente porém requer download do ffmpeg

import os
import subprocess

ffmpeg_path = r"C:\\tools\\ffmpeg\\bin\\ffmpeg.exe"  # ajuste conforme onde você extraiu

# Caminhos das pastas
pasta_entrada = "videos"
pasta_saida = "videos_comprimidos"
os.makedirs(pasta_saida, exist_ok=True)

# Resolução alvo (metade, por exemplo: 1280x720 → 640x360)
resolucao_alvo = "scale=iw/2:ih/2"

for nome_arquivo in os.listdir(pasta_entrada):
    if nome_arquivo.endswith(".mp4"):
        caminho_entrada = os.path.join(pasta_entrada, nome_arquivo)
        caminho_saida = os.path.join(pasta_saida, f"comprimido_{nome_arquivo}")
        
        print(f"🔄 Processando: {nome_arquivo}")
        try:
            comando = [
                ffmpeg_path,
                "-i", caminho_entrada,
                "-vf", resolucao_alvo,           # Reduz resolução
                "-b:v", "800k",                  # Bitrate do vídeo
                "-c:v", "libx264",               # Codec de vídeo
                "-preset", "fast",               # Velocidade de compressão
                "-c:a", "aac",                   # Codec de áudio
                "-b:a", "128k",                  # Bitrate do áudio
                "-movflags", "+faststart",       # Otimiza para web
                caminho_saida
            ]

            subprocess.run(comando, check=True)
            print(f"✅ Arquivo salvo em: {caminho_saida}\n")

        except subprocess.CalledProcessError as e:
            print(f"❌ Erro ao processar {nome_arquivo}: {e}\n")
