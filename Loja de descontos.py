# Loja da Camila Brazão
print('Bem vindo a loja da Camila Brazão')
valor=int(input('Valor do produto: '))
qtd=int(input('Qual a quantidade? '))
preco= valor*qtd
print('O valor sem desconto é R$ {:.2f}'.format(preco))
if (qtd<=9):
  print('Esta quantidade não recebe desconto')
  print('O preço do produto será R$ {:.2f}'.format(preco))
elif qtd<=99:
  desconto = preco*(5/100)
  preco_com_desconto= preco - desconto
  print('O valor com desconto é R$ {:.2f}'.format(preco_com_desconto)) #desconto de 5%"
elif qtd<=999:
  desconto = preco*(10/100)
  preco_com_desconto = preco - desconto
  print('O valor com desconto é R$ {:.2f}'.format(preco_com_desconto)) #desconto de 10%
else:
   desconto = preco*(15/100)
   preco_com_desconto = preco - desconto
   print('O valor com desconto é R$ {:.2f}'.format(preco_com_desconto)) #desconto de 15%