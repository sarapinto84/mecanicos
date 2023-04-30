# serve para calcular a aldrabice dos mecânicos
a=input("qual é o preço do fornecedor?")
b=input("qual é o valor de aldrabice que eu quero juntar ao preço do fornecedor?")
forn_tot=int(a)+int(b)
vatti2=(forn_tot)*1.23
print("parabéns sacaste bué da guita:",vatti2,"€","és mesmo bué da bom!")
htr=input("que número de horas reais trabalhaste?")
htr1=int(htr)
htaldr=(htr1+2)
print("Ok, vamos acreditar que trabalhaste",htaldr)
hora=30
mao_de_obra=htaldr*hora
calculo_final=vatti2+mao_de_obra
print("Parabéns, mais um dia a encher bem a carteira ;) mais umas jeiras sem trabalhar!",calculo_final,"€")