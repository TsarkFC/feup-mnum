'''
OTIMIZAÇÃO

-Apenas funciona para problemas convexos (que têm apenas um mínimo no intervalo a considerar)

Guess (Valor perto do míninimo) -> 
Pesquisa (Arranja intervalo que enquadra o mínimo)-> 
Intervalo -> 
Redução intervalar (trisseção)-> 
Intervalo (mais pequeno que o anterior)-> 
Ajuste (Ajuste de quádrica)-> 
1 ponto (Valor melhor para o mínimo)


Porque não de passa logo de uma pesquisa para um ajuste??
Re. Ajuste apenas é válido na proximidade do mínimo


 Passo de PESQUISA:

-Estratégia de dobrar o passo a cada pesquisa -> Excelente se estiver garantido 
que a região em causa é convexa
-Direção de pesquisa (direção em que valores vão sendo sucessivamente menores)
-Detetar direção de pesquisa, uma vez que o problema é convexo também é a direção do mínimo
-Ao encontrar um valor que se opõe à direção de pesquisa (é maior que o anterior), está encontrado o 
intervalo

 Passo de REDUÇÃO INTERVALAR: (GOLDEN SECTION / THIRDS RULE)

-Estando garantido que entre os pontos a, b existe um mínimo
-Divisão do intervalo inicial em três subintervalos
-Um dos intervalos pode "deitado fora" dependendo dos pontos escolhidos para formar o intervalo
-Caso os pontos estejam alinhados pode se rejeitar qualquer intervalo

THIRDS RULE:
-Em cada iteração são calculados dois novos pontos, sendo rejeitado um dos pontos já 
calculado anteriormente, uma vez que ao rejeitar 1/3 do intervalo inicial, o novo 
intervalo (2/3), vai ser novamente dividido em três partes 

GOLDEN SECTION: (intervalo [a,b])
-Golden ratio: (sqrt(5) - 1) / 2 aprox. 0.618
-Divisão do intervalo segundo o golden ratio:
    
    Cálculo de D(novo ponto do intervalo): 
        -sendo que a primeira parte corresponde a  0.618 do intervalo e a segunda (1-0.618):
        d = a + 0.618 * (b-a) V d = b - 0.38 * (b-a)

    Cálculo de C(outro ponto do novo intervalo):
        c = a + 0.38 * (b-a) V c = b - 0.618 * (b-a)

GOLDEN SECTION É MUITO MELHOR MELHOR QUE THIRDS RULE:
-reduction rate de 38% muito melhor que 33%;

Passo de AJUSTE: (não é um processo iterativo) - "One shot method"

'''

from math import sin, pi

#Econtrar o mínimo por este método para sin(x)
def optimized(f, step, guess_a, guess_b):

    #Get search direction
    if (f(guess_a + step) > f(guess_a)):
        step = -step

    a = guess_a

    while (f(guess_a + step) < f(guess_a)):
        a = guess_a
        guess_a += step

    b = guess_a

    #Intervalo [a,b]

    #GOLDEN SECTION
    d = a + 0.618 * (b-a)
    c = a + 0.38 * (b-a)

    while (b-a > 0.0001):
        d = a + 0.618 * (b-a)
        c = a + 0.38 * (b-a)

        if (f(c) < f(d)):
            b = d
        elif (f(c) > f(d)):
            a = c

    return (a + b) / 2

print(optimized(sin, 0.005, -8, 0))