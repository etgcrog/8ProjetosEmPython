import os

audios_ext = ['.ogg','.mp3']
video_ext = ['.mp4', '.mov', '.avi']
imagens_ext =  ['.jpg', 'jpeg', '.png']
documentos_ext = ['.pdf', '.log']

def encontra_ext(name_file):
    index = name_file.rfind('.')
    return name_file[index:]

def organizar(diretorio):
    AUDIO_DIR = os.path.join(diretorio, "audio")
    VIDEO_DIR = os.path.join(diretorio, "video")
    IMG_DIR = os.path.join(diretorio, "imagens")
    DOC_DIR = os.path.join(diretorio, "documentos")
    OUTROS_DIR = os.path.join(diretorio, "outros")
    
    if not os.path.isdir(AUDIO_DIR) : os.mkdir(AUDIO_DIR)
    if not os.path.isdir(VIDEO_DIR) : os.mkdir(VIDEO_DIR)
    if not os.path.isdir(IMG_DIR) : os.mkdir(IMG_DIR)
    if not os.path.isdir(DOC_DIR) : os.mkdir(DOC_DIR)
    if not os.path.isdir(OUTROS_DIR) : os.mkdir(OUTROS_DIR)
    
    name_files = os.listdir(diretorio)
    dir = ''
    
    for file in name_files:
        if os.path.isfile(os.path.join(diretorio, file)):
            ext = str.lower(encontra_ext(file))
            if ext in audios_ext : dir = AUDIO_DIR
            elif ext in video_ext : dir = VIDEO_DIR
            elif ext in imagens_ext : dir = IMG_DIR
            elif ext in documentos_ext : dir = DOC_DIR
            else : dir = OUTROS_DIR
            
            old = os.path.join(diretorio, file)
            new = os.path.join(dir, file)
            
            os.rename(old, new)
            
            print(f"MOVE {old} TO {new}")
            
if __name__ == '__main__':
    organizar("teste")
    
            