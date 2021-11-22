import os 

audios_ext = ['.ogg','.mp3']
video_ext = ['.mp4', '.mov', '.avi']
imagens_ext =  ['.jpg', 'jpeg', '.png']
documentos_ext = ['.pdf', '.log']

def encontra_extensao(files):
    index = files.rfind('.')
    return files[index:]

def organiza(diretorio):
    AUDIO_DIR = os.path.join(diretorio, "audio")
    VIDEO_DIR = os.path.join(diretorio, "videos")
    IMG_DIR = os.path.join(diretorio, "imagens")
    DOCUMENTO_DIR = os.path.join(diretorio, "documentos")
    OUTROS_DIR = os.path.join(diretorio, "outros")    
        
    if not os.path.isdir(AUDIO_DIR): os.mkdir(AUDIO_DIR)
    if not os.path.isdir(VIDEO_DIR): os.mkdir(VIDEO_DIR)
    if not os.path.isdir(IMG_DIR): os.mkdir(IMG_DIR)
    if not os.path.isdir(DOCUMENTO_DIR): os.mkdir(DOCUMENTO_DIR)
    if not os.path.isdir(OUTROS_DIR): os.mkdir(OUTROS_DIR)
        
    list_files = os.listdir(diretorio)
    
    pasta = ''
    
    for file in list_files:
        if os.path.isfile(os.path.join(diretorio, file)):
            ext = str.lower(encontra_extensao(file))
            if ext in audios_ext : pasta = AUDIO_DIR
            elif ext in video_ext : pasta = VIDEO_DIR
            elif ext in imagens_ext : pasta = IMG_DIR
            elif ext in documentos_ext : pasta = DOCUMENTO_DIR
            else :  pasta = OUTROS_DIR
            
            old = os.path.join(diretorio, file)
            new = os.path.join(pasta, file)
            
            os.rename(old, new)
            
            print(f"MOVE{old} >>> {new}")
    
     
if __name__ == '__main__':
    organiza('oraganizar_pasta copy')
    
        