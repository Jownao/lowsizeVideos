# Ocorre bugs , teste e verifique se serve para sua necessidade

import os
from PIL import Image
from moviepy.editor import VideoFileClip

# Ajuste o Pillow para compatibilidade com versões recentes
if not hasattr(Image, "ANTIALIAS"):
    Image.ANTIALIAS = Image.Resampling.LANCZOS

# Caminhos das pastas
pasta_entrada = "videos"
pasta_saida = "videos_comprimidos"
os.makedirs(pasta_saida, exist_ok=True)

for nome_arquivo in os.listdir(pasta_entrada):
    if nome_arquivo.endswith(".mp4"):
        caminho_entrada = os.path.join(pasta_entrada, nome_arquivo)
        caminho_saida = os.path.join(pasta_saida, f"ruim_comprimido_{nome_arquivo}")
        
        print(f"🔄 Processando: {nome_arquivo}")
        try:
            clip = VideoFileClip(caminho_entrada)
            clip_resized = clip.resize(0.9)  # reduz a resolução pela metade

            # Define o fps para o mesmo valor do clip original
            fps_original = clip.fps if hasattr(clip, "fps") and clip.fps else 30  # fallback para 30 se não definido

            # Exporta o vídeo com o fps explicitamente definido
            clip_resized.write_videofile(
                caminho_saida,
                fps=fps_original,
                audio_fps=44100,
                bitrate="800k",      
                codec="libx264",
                audio_codec="aac",   
                audio_bitrate="128k",
                preset="fast",       
            )
            
            print(f"✅ Arquivo salvo em: {caminho_saida}\n")
        except Exception as e:
            print(f"❌ Erro ao processar {nome_arquivo}: {e}\n")
