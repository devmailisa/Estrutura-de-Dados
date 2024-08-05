import lista_sequencial as l
#import lista_encadeada as l
import random, math
#TAM = 100

L1 = l.Lista()
L2 = l.Lista()

for i in range(10):
    L1.insereFim(math.ceil(random.random()*100))
    
for i in range(15):
    L2.insereFim(math.ceil(random.random()*100))

L3 = L1.concatenar(L2)
L4 = l.Lista()
for i in range(len(L3)):
    L4.insereInicio(L3.elemento(i+1))

print(f"Lista 1 -> {L1}")
print(f"Lista 2 -> {L2}")
print(f"Lista 3 -> {L3}")
print(f"Lista 4 -> {L4}")