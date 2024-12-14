while True:
    quantidade_vagoes = int(input())
    if quantidade_vagoes == 0:
        break
    
    while True:
        sequencia = list(map(int, input().split()))
        if sequencia == [0]:
            break
        
        pilha = []
        vagon_atual = 1
        possivel = True
        
        for vagon in sequencia:
            while vagon_atual <= quantidade_vagoes and (not pilha or pilha[-1] != vagon):
                pilha.append(vagon_atual)
                vagon_atual += 1
            
            if pilha and pilha[-1] == vagon:
                pilha.pop()
            else:
                possivel = False
                break
        
        if possivel:
            print("Yes")
        else:
            print("No")
    
    print()
