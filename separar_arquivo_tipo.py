import os

audios = ['.ogg','.mp3']
video = ['.mp4', '.mov', '.avi']
imagens =  ['.jpg', 'jpeg', '.png']
documentos = ['.pdf', '.log']

def pegar_extensao(nomes):
    index = nomes.rfind('.')
    return nomes[index:]
    
def organizar(diretorio):
    
    AUDIO_dir = os.path.join(diretorio, "audios")
    VIDEO_dir = os.path.join(diretorio, "videos")
    DOC_dir = os.path.join(diretorio, "documentos")
    IMAGENS_dir = os.path.join(diretorio, "imagens")
    OUTROS_dir = os.path.join(diretorio, "outros")
    
    if not os.path.isdir(AUDIO_dir):
        os.mkdir(AUDIO_dir)
    if not os.path.isdir(VIDEO_dir):
        os.mkdir(VIDEO_dir)
    if not os.path.isdir(DOC_dir):
        os.mkdir(DOC_dir)
    if not os.path.isdir(IMAGENS_dir):    
        os.mkdir(IMAGENS_dir)
    if not os.path.isdir(OUTROS_dir):
        os.mkdir(OUTROS_dir)

    
    file_names = os.listdir(diretorio)
    
    pasta = ''
    
    for file in file_names:
        if os.path.isfile(os.path.join(diretorio, file)):
            ext = str.lower(pegar_extensao(file))
            if ext in audios:
                pasta = AUDIO_dir
            elif ext in video:
                pasta = VIDEO_dir
            elif ext in imagens:
                pasta = IMAGENS_dir
            elif ext in documentos:
                pasta = DOC_dir
            else:
                pasta = OUTROS_dir
        
            old = os.path.join(diretorio, file)
            new = os.path.join(pasta, file)
            os.rename(old, new)
            print("Moveu", old, "->", new)

if __name__ == '__main__':
    
    dir_path = '/home/edudev/Downloads'
    organizar(dir_path)