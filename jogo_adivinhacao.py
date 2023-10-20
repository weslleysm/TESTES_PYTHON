print("                                 Seja bem vindo ao jogo de adivinhação!")

numero_secreto = 10
chute = int(input("Digite o numero:"))

acertou = numero_secreto == chute
maior   = chute > numero_secreto
menor   = chute < numero_secreto

print("Voce digitou:", chute)

  # funsão if/else -> significa se/então

if (acertou):
   print("Parabem, Voce acertou!")
else:
   if(maior):
      print("Voce digitou uma numero maior!");
   elif(menor):
      print("Voce digitou um numero menor!")