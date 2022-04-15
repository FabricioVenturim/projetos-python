def Substituir (texto, texto_antigo, texto_novo):
    documento_novo=texto.replace(texto_antigo, texto_novo)
    print(documento_novo)

texto ="""
"oi!! oi meu nome soi pablo, tchau!

"""
Substituir (texto, 'oi', 'tchau')