altura = float(input("Qual é a altura da sua parede? "))
largura = float(input("Qual é a largura da sua parede? "))
área=altura*largura
tinta=área/2
print("Sendo a área da sua parede {}m², então voce precisará de {}L de tinta.".format(área,tinta))