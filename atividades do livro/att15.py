
data=int(input("Digite data no formato DDMMAA: "))
dia=int
mes=int
ano=int
dia=data / 10000
mes=data % 10000 / 100
ano=data %100
print("DIA: ",dia)
print("MES: ",mes) 
print ("ANO: ",ano)