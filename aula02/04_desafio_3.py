from datetime import datetime, date, time, timedelta


# Peça para o usuário digitar a data de seu próximo aniversário no formato brasileiro
aniversario_str = input('Digite seu aniversário em 2022 (dd/mm/aaaa): ')
aniversario_datetime = datetime.strptime(aniversario_str, '%d/%m/%Y')

# Imprima uma mensagem dizendo quantos dias faltam para o aniversário dele
agora = datetime.now()
contagem_de_dias = aniversario_datetime - agora

print("Faltam " + str(contagem_de_dias) + " para o seu aniversário")

# Pergunte ao usuário se ele(a) gosta de aniversário e salve a resposta
gosta_de_aniversario = input('Você gosta de aniversário? (sim ou não) ')

# Pergunte ao usuário se ele(a) vai fazer festa e salve a resposta
fazer_festa = input('Você vai fazer festa? (sim ou não) ')

if gosta_de_aniversario =='sim' and fazer_festa == 'sim':
  print("Você vai ganhar um presente!")

elif gosta_de_aniversario.lower == 'não' or fazer_festa.lower == 'não':
  print('Você não vai ganhar um presente')

else:
  print('você não vai ganhar um presente')

# Imprima uma mensagem dizendo se o usuário vai ganhar presente ou não
# A regra é: o usuário só pode ganhar presente se gostar de aniversário e for fazer festa.