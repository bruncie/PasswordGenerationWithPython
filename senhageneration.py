import random
import string

tamanho = 16

#estrutura geradora de senha
chars = string.ascii_letters + string.digits + ' /?!@#$%¨&*()_+{} '

#para gerar numeros aleatorios a partir dos numeros do sistema operacional
rnd = random.SystemRandom()

#join irá juntar rnd+chars variando n vezes até atingir o tamanho no for
print( ' '.join(rnd.choice(chars) for i in range(tamanho)))