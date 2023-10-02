data=int(input("Digite data no formato DDMMAA: "))
dia=int
mes=int
ano=int
ndata=int
dia=data / 10000
mes=data % 10000 / 100
ano=data %100
ndata=mes *10000 +dia* 100 +ano
print("DIA: ",dia)
print("MES: ",mes) 
print ("ANO: ",ano)
print("DATA NO FORMATO MMDDAA: ",ndata) 