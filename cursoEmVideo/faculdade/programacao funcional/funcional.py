usuario = {
    'nome': 'Jaoa',
    'redes': [{
        'nome': 'facebook',
        'imagem_profile': "",
        'imagem_capa': 'imagem do naruto'
    }, {
        'nome': 'X',
        'imagem_profile': "imagem1",
        'imagem_capa': ''
    }]
}

# retorna a imagem do profile
def getImgProfile(usuario):
    for rede in usuario['redes']:
        if rede[imagem_profile]:
            return rede['imagem_profile']
    return 'default'

# retorna a imagem de capa
def getImgCapa(usuario):
    for rede in usuario['redes']:
        if rede[imagem_capa]:
            return rede['imagem_capa']
    return 'default'

# utilizando partial
from functools import partial
def getImg(qualImg, usuario):
    for rede in usuario['redes']:
        if rede[qualImg]:
            return rede[qualImg]
    return 'defautl'


get_imagem_profile = partial(getImg, 'imagem_profile')
get_imagem_capa = partial(getImg, 'imagem_capa')

print('Saida')
print(get_imagem_profile(usuario))
print(get_imagem_capa(usuario))

