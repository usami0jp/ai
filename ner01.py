def sub(sente):
    ij=0
    if 'you' in sente:
        ij=2
    if 'watch' in sente:
        ij=2
    if 'watching' in sente:
        ij=2
    if 'see' in sente:
        ij=2
    if 'seeing' in sente:
        ij=2
    if 'what' in sente:
        ij=2
    if 'How' in sente:
        ij=2
    if '何が' in sente:
        if '見える' in sente:
            ij=2
        elif '見えます' in sente:
            ij=2
        elif '見え' in sente:
            ij=2
    if 'ニュース' in sente:
        ij=1
    return ij

'''
def sub(sente):
    ij=0
    if 'you' in sente:
        ij=ij+1
    if 'watch' in sente:
        ij=ij+1
    if 'watching' in sente:
        ij=ij+1
    if 'see' in sente:
        ij=ij+1
    if 'seeing' in sente:
        ij=ij+1
    if 'what' in sente:
        ij=ij+1
    if 'How' in sente:
        ij=ij+1
    if 'ニュース' in sente:
        ij=ij+1
    return ij
'''










#sente=' what can you see '









#sente=' what can you see '
#ijk=sub(sente)
#print(ijk)
