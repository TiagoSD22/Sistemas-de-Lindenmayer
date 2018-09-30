import turtle
import random

def SetColor(cor = ("#000000"),espessura = 0):
    turtle.resetscreen()
    turtle.colormode(255)
    turtle.color(cor)
    turtle.pensize(espessura)

def ReescreverKochSnowFlake(NI):
    axi = '-F+F+F---'
    regra = 'F-F+F-F'
    res = axi
    for i in range(NI):
        res = ''
        for i in axi:
            if(i == 'F'):
                res = res + regra
            elif i == '-':
                res = res + '-'
            else:
                res = res + '+'
        axi = res
    return res

def InterpretarKochSnowFlake(Lado,NG):
    turtle.speed(0)
    tela = turtle.getscreen()
    tela.tracer(8,25)
    turtle.up()
    turtle.bk(200)
    turtle.down()
    expressao = ReescreverKochSnowFlake(NG)
    Lado = Lado/(3 ** NG)
    turtle.hideturtle()
    for i in expressao:
        if(i == 'F'):
            turtle.fd(Lado)
        elif i == '-':
            turtle.left(60)
        else:
            turtle.right(120)
    turtle.update()

def ReescreverKochIsland(NI):
    axi = 'F-F-F-F-'
    regra = 'F-F+F+FF-F-F+F'
    saida = axi
    for i in range(NI):
        saida = ''
        for i in axi:
            if(i == 'F'):
                saida = saida + regra
            elif i == '-':
                saida = saida + '-'
            else:
                saida = saida + '+'
        axi = saida
    return saida

def InterpretarKochIsland(Lado,NG):
    turtle.speed(0)
    tela = turtle.getscreen()
    tela.tracer(8,25)
    turtle.up()
    turtle.bk(200)
    turtle.right(90)
    turtle.fd(150)
    turtle.left(90)
    turtle.down()
    expressao = ReescreverKochIsland(NG)
    Lado = Lado / (4 ** NG)
    turtle.hideturtle()
    for i in expressao:
        if(i == 'F'):
            turtle.fd(Lado)
        elif i == '-':
            turtle.left(90)
        else:
            turtle.right(90)
    turtle.update()

def ReescreverKochIslandLake(NI):
    axi = 'F+F+F+F'
    regra = 'F+f-FF+F+FF+Ff+FF-f+FF-F-FF-Ff-FFF'
    saida = axi
    for i in range(NI):
        saida = ''
        for i in axi:
            if(i == 'F'):
                saida = saida + regra
            if(i == 'f'):
                saida = saida + 'ffffff'
            if(i == '-'):
                saida = saida + '-'
            if(i == '+'):
                saida = saida + '+'
        axi = saida
    return saida

def InterpretarKochIslandLake(Lado,NG):
    turtle.speed(0)
    turtle.up()
    tela = turtle.getscreen()
    tela.tracer(5,10)
    turtle.bk(200)
    turtle.down()
    Lado = Lado / (4 ** NG)
    expressao = ReescreverKochIslandLake(NG)
    turtle.hideturtle()
    for i in expressao:
        if(i == 'F'):
            turtle.fd(Lado)
        if(i == 'f'):
            turtle.up()
            turtle.fd(Lado)
            turtle.down()
        if(i == '-'):
            turtle.left(90)
        if(i == '+'):
            turtle.right(90)
    turtle.update()

def ReescreverKochPyramid(NI):
    iniciador = "F"
    gerador = "F-F+F+F-F"
    saida = iniciador
    for i in range(NI):
        saida = ''
        for i in iniciador:
            if(i == 'F'):
                saida = saida + gerador
            else:
                saida = saida + i
        iniciador = saida
    return saida

def InterpretarKochPyramid(Lado, NG):
    turtle.speed(0)
    tela = turtle.getscreen()
    tela.tracer(8,25)
    turtle.up()
    turtle.bk(333)
    turtle.right(90)
    turtle.fd(250)
    turtle.left(90)
    turtle.down()
    Lado = Lado / (3 ** NG)
    expressao = ReescreverKochPyramid(NG)
    turtle.hideturtle()
    for i in expressao:
        if(i == 'F'):
            turtle.fd(Lado)
        elif i == '-':
            turtle.left(90)
        else:
            turtle.right(90)
    turtle.update()

def ReescreverKochBox(NI):
    iniciador = 'F-F-F-F'
    gerador = 'FF-F-F-F-FF'
    saida = iniciador
    for i in range(NI):
        saida = ''
        for i in iniciador:
            if(i == 'F'):
                saida = saida + gerador
            elif i == '-':
                saida = saida + '-'
            else:
                saida = saida + '+'
        iniciador = saida
    return saida

def InterpretarKochBox(Lado,NG):
    turtle.speed(0)
    turtle.up()
    turtle.bk(250)
    turtle.right(90)
    turtle.fd(250)
    turtle.left(90)
    turtle.down()
    expressao = ReescreverKochBox(NG)
    Lado = Lado/(4 ** NG)
    tela = turtle.getscreen()
    tela.tracer(8,25)
    turtle.hideturtle()
    for i in expressao:
        if(i == 'F'):
            turtle.fd(Lado)
        elif i == '-':
            turtle.left(90)
        else:
            turtle.right(90)
    turtle.update()

def ReescreverKochSquare(NI):
    iniciador = 'F-F-F-F-'
    gerador = 'F_F+F_F'
    saida = iniciador
    for i in range(NI):
        saida = ''
        for i in iniciador:
            if(i == 'F'):
                saida = saida + gerador
            elif i == '-':
                saida = saida + '-'
            elif i == '+':
                saida = saida + '+'
            else:
                saida = saida + '_'
        iniciador = saida
    return saida

def InterpretarKochSquare(Lado,NG):
    Lado = Lado / (3 ** NG)
    expressao = ReescreverKochSquare(NG)
    turtle.speed(0)
    turtle.up()
    tela = turtle.getscreen()
    tela.tracer(12,25)
    turtle.bk(250)
    turtle.right(90)
    turtle.fd(250)
    turtle.left(90)
    turtle.down()
    turtle.hideturtle()
    for i in expressao:
        if(i == 'F'):
            turtle.fd(Lado)
        elif i == '-':
            turtle.left(90)
        elif i == '_':
            turtle.left(85)
        else:
            turtle.right(170)
    turtle.update()

def ReescreverKochStar(NI):
    iniciador = 'F-F-F-F'
    gerador = 'FF-F-F-F-F-F+F'
    saida = iniciador
    for i in range(NI):
        saida = ''
        for i in iniciador:
            if(i == 'F'):
                saida = saida + gerador
            elif i == '-':
                saida = saida + '-'
            else:
                saida = saida + '+'
        iniciador = saida
    return saida

def InterpretarKochStar(Lado,NG):
    turtle.speed(0)
    tela = turtle.getscreen()
    tela.tracer(15,30)
    turtle.up()
    turtle.fd(200)
    turtle.right(90)
    turtle.fd(100)
    turtle.left(90)
    turtle.down()
    Lado = Lado / (4 ** NG)
    expressao = ReescreverKochStar(NG)
    turtle.hideturtle()
    for i in expressao:
        if(i == 'F'):
            turtle.fd(Lado)
        elif i == '-':
            turtle.left(90)
        else:
            turtle.right(90)
    turtle.update()

def ReescreverKochRets(NI):
    iniciador = 'F-F-F-F'
    gerador = 'FF-F+F-F-FF'
    saida = iniciador
    for i in range(NI):
        saida = ''
        for i in iniciador:
            if(i == 'F'):
                saida = saida + gerador
            elif i == '-':
                saida = saida + '-'
            else:
                saida = saida + '+'
        iniciador = saida
    return saida

def InterpretarKochRets(Lado,NG):
    turtle.speed(0)
    tela = turtle.getscreen()
    tela.tracer(5,25)
    turtle.up()
    turtle.down()
    Lado = Lado/(4**NG)
    expressao = ReescreverKochRets(NG)
    turtle.hideturtle()
    for i in expressao:
        if(i == 'F'):
            turtle.fd(Lado)
        elif i == '-':
            turtle.left(90)
        else:
            turtle.right(90)
    turtle.update()

def ReescreverKochDragon(NI):
    iniciador = 'F'
    geradorA = 'F+f+'
    geradorB = '-F-f'
    saida = iniciador
    for i in range(NI):
        saida = ''
        for i in iniciador:
            if(i == 'F'):
                saida = saida + geradorA
            elif i == 'f':
                saida = saida + geradorB
            elif i == '-':
                saida = saida + '-'
            else:
                saida = saida + '+'
        iniciador = saida
    return saida

def InterpretarKochDragon(Lado,NG):
    turtle.speed(0)
    tela = turtle.getscreen()
    tela.tracer(5,25)
    turtle.up()
    turtle.bk(200)
    turtle.down()
    Lado = Lado / (2 ** NG)
    expressao = ReescreverKochDragon(NG)
    turtle.hideturtle()
    for i in expressao:
        if(i == 'F' or i == 'f'):
            turtle.fd(Lado)
        elif i == '-':
            turtle.left(90)
        else:
            turtle.right(90)
    turtle.update()

def ReescreverKochTrianguloB(NI):
    iniciador = "F-G-G"
    regraF = "F-F+F+F-G"
    regraG = "GG"
    saida = iniciador
    for i in range(NI):
        saida = ''
        for i in iniciador:
            if(i == 'F'):
                saida = saida + regraF
            elif i == 'G':
                saida = saida + regraG
            elif i == '-':
                saida = saida + '-'
            else:
                saida = saida + '+'
        iniciador = saida
    return saida

def InterpretarKochTrianguloB(Lado,NG):
    turtle.speed(0)
    turtle.up()
    tela = turtle.getscreen()
    tela.tracer(5,25)
    turtle.bk(300)
    turtle.right(90)
    turtle.fd(250)
    turtle.left(90)
    turtle.down()
    Lado = Lado/(2 ** NG)
    expressao = ReescreverKochTrianguloB(NG)
    turtle.hideturtle()
    for i in expressao:
        if(i == 'F' or i == 'G'):
            turtle.fd(Lado)
        elif i == '-':
            turtle.left(120)
        else:
            turtle.right(120)
    turtle.update()

def ReescreverKochHex(NI):
    iniciador = 'F'
    geradorA = 'F+f++f-F--FF-f+'
    geradorB = '-F+ff++f+F--F-f'
    saida = iniciador
    for i in range(NI):
        saida = ''
        for i in iniciador:
            if(i == 'F'):
                saida = saida + geradorA
            elif i == 'f':
                saida = saida + geradorB
            elif i == '-':
                saida = saida + '-'
            else:
                saida = saida + '+'
        iniciador = saida
    return saida

def InterpretarKochHex(Lado,NG):
    turtle.speed(0)
    tela = turtle.getscreen()
    tela.tracer(15,25)
    turtle.up()
    turtle.fd(250)
    turtle.left(90)
    turtle.fd(150)
    turtle.right(90)
    turtle.down()
    Lado = Lado / (3 ** NG)
    expressao = ReescreverKochHex(NG)
    turtle.hideturtle()
    for i in expressao:
        if(i == 'F' or i == 'f'):
            turtle.fd(Lado)
        elif i == '-':
            turtle.left(60)
        else:
            turtle.right(60)
    turtle.update()

def ReescreverKochMaze(NI):
    iniciador = '-f'
    geradorA = 'FF-f-f+F+F-f-fF+f+FFf-F+f+FF+f-Ff-f-F+F+ff-'
    geradorB = '+FF-f-f+F+Ff+F-ff-F-f+Fff-F-fF+F+f-f-F+F+ff'
    saida = iniciador
    for i in range(NI):
        saida = ''
        for i in iniciador:
            if(i == 'F'):
                saida = saida + geradorA
            elif i == 'f':
                saida = saida + geradorB
            elif i == '-':
                saida = saida + '-'
            else:
                saida = saida + '+'
        iniciador = saida
    return saida

def InterpretarKochMaze(Lado,NG):
    turtle.speed(0)
    tela = turtle.getscreen()
    tela.tracer(15,25)
    turtle.up()
    turtle.bk(200)
    turtle.right(90)
    turtle.fd(250)
    turtle.left(90)
    turtle.down()
    Lado = Lado / (4 ** NG)
    expressao = ReescreverKochMaze(NG)
    turtle.hideturtle()
    for i in expressao:
        if(i == 'F' or i == 'f'):
            turtle.fd(Lado)
        elif i == '-':
            turtle.left(90)
        else:
            turtle.right(90)
    turtle.update()
             
def ReescreverHilbertCurve(NI):
    axioma = 'X'
    regraX = '+YF-XFX-FY+'
    regraY = '-XF+YFY+FX-'
    regraF = 'F'
    saida = axioma
    for i in range(NI):
        saida = ''
        for i in axioma:
            if(i == 'X'):
                saida += regraX
            elif i == 'Y':
                saida += regraY
            elif i == 'F':
                saida += regraF
            else:
                saida += i
        axioma = saida
    return saida

def InterpretarHilbertCurve(Lado,NG):
    expressao = ReescreverHilbertCurve(NG)
    Lado = Lado / (2 ** NG)
    turtle.speed(0)
    tela = turtle.getscreen()
    tela.tracer(5,25)
    turtle.up()
    turtle.bk(250)
    turtle.right(90)
    turtle.fd(250)
    turtle.left(90)
    turtle.down()
    turtle.hideturtle()
    for i in expressao:
        if(i == 'F' or i == 'X' or i == 'Y'):
            turtle.fd(Lado)
        elif i == '-':
            turtle.right(90)
        else:
            turtle.left(90)
    turtle.update()

def ReescreverHilbertCurveII(NI):
    axioma = "X"
    regraX = "XFYFX+F+YFXFY-F-XFYFX"
    regraY = "YFXFY-F-XFYFX+F+YFXFY"
    regraF = "F"
    saida = axioma
    for i in range(NI):
        saida = ''
        for i in axioma:
            if(i == 'F'):
                saida += regraF
            elif i == 'X':
                saida += regraX
            elif i == 'Y':
                saida += regraY
            else:
                saida += i
        axioma = saida
    return saida

def InterpretarHilbertCurveII(Lado, NG):
    expressao = ReescreverHilbertCurveII(NG)
    Lado = Lado / (2 ** NG)
    turtle.speed(0)
    tela = turtle.getscreen()
    tela.tracer(5,25)
    turtle.up()
    turtle.bk(200)
    turtle.right(90)
    turtle.fd(250)
    turtle.left(90)
    turtle.down()
    turtle.left(90)
    turtle.hideturtle()
    for i in expressao:
        if(i == 'F' or i == 'X' or i == 'Y'):
            turtle.fd(Lado)
        elif i == '+':
            turtle.right(90)
        else:
            turtle.left(90)
    turtle.update()

def ReescreverSierpinskiSquare(NI):
    axioma = "X--F--X--F"
    regraX = "+Y-F-Y+"
    regraY = "-X+F+X-"
    regraF = "F"
    saida = axioma
    for i in range(NI):
        saida = ''
        for i in axioma:
            if(i == 'F'):
                saida += regraF
            elif i == 'X':
                saida += regraX
            elif i == 'Y':
                saida += regraY
            else:
                saida += i
        axioma = saida
    return saida

def InterpretarSierpinskiSquare(Lado, NG):
    expressao = ReescreverSierpinskiSquare(NG)
    turtle.speed(0)
    tela = turtle.getscreen()
    tela.tracer(5,25)
    turtle.up()
    turtle.bk(300)
    turtle.down()
    turtle.hideturtle()
    for i in expressao:
        if(i == 'F' or i == 'X' or i == 'Y'):
            turtle.fd(Lado)
        elif i == '-':
            turtle.left(45)
        else:
            turtle.right(45)
    turtle.update()

def ReescreverCrystal(NI):
    axioma = "F+F+F+F"
    regra = "FF+F++F+F"
    saida = axioma
    for i in range(NI):
        saida = ''
        for i in axioma:
            if(i == 'F'):
                saida += regra
            else:
                saida += i
        axioma = saida
    return saida

def InterpretarCrystal(Lado, NG):
    expressao = ReescreverCrystal(NG)
    turtle.speed(0)
    turtle.up()
    turtle.bk(250)
    turtle.right(90)
    turtle.fd(250)
    turtle.left(90)
    turtle.down()
    tela = turtle.getscreen()
    tela.tracer(5,25)
    turtle.hideturtle()
    for i in expressao:
        if(i == 'F'):
            turtle.fd(Lado)
        elif i == '-':
            turtle.right(90)
        else:
            turtle.left(90)
    turtle.update()

def ReescreverString(iniciador, regras, NI):
    saida = iniciador
    termos = IdentificarTermos(regras)
    ListaRegras = IdentificarRegras(regras)
    for i in range(NI):
        saida = ''
        for i in iniciador:
            if(ReconhecerTermo(termos,i) == -1):
                saida = saida + i
            else:
                j = ReconhecerTermo(termos,i)
                saida = saida + ListaRegras[j]
        iniciador = saida
    return saida

def InterpretarString(iniciador,gerador,ae,ad,Lado,NG,randomL = 0,randomAn = 0):
    turtle.speed(0)
    tela = turtle.getscreen()
    tela.tracer(8,25)
    turtle.up()
    turtle.bk(100)
    turtle.down()
    expressao = ReescreverString(iniciador,gerador,NG)
    p,h = [0,0],0
    ultimo = 0
    stack = []
    turtle.hideturtle()
    i = 0
    while(i < len(expressao)):
        if(expressao[i].isalpha() and expressao[i] != 'f' and expressao[i] != 'b' and expressao[i] != 'S'):
            if(randomL > 0):
                LadoR = random.randint(int((Lado - (randomL * Lado)/100)),int((Lado + (randomL * Lado)/100)))
                turtle.fd(LadoR)
            else:
                turtle.fd(Lado)
        if(expressao[i] == 'f'):
            if(randomL > 0):
                LadoR = random.randint(int((Lado - (randomL * Lado)/100)),int((Lado + (randomL * Lado)/100)))
                turtle.up()
                turtle.fd(LadoR)
                turtle.down()
            else:
                turtle.up()
                turtle.fd(Lado)
                turtle.down()
        if(expressao[i] == 'S'):
            Lado = Lado/2
        if(expressao[i] == 'b'):
            turtle.up()
            turtle.bk(100)
            turtle.down()
        if expressao[i] == '-':
            if(randomAn > 0):
                aeR = random.randint(int((ae - (randomAn * ae)/100)),int((ae + (randomAn * ae)/100)))
                turtle.left(aeR)
            else:
                turtle.left(ae)
        if(expressao[i] == '<'):
            turtle.left(90)
        if(expressao[i] == '>'):
            turtle.right(90)
        if(expressao[i] == '|'):
            turtle.left(180)
        if expressao[i] == '+':
            if(randomAn > 0):
                adR = random.randint(int((ad - (randomAn * ad)/100)),int((ad + (randomAn * ad)/100)))
                turtle.right(adR)
            else:
                turtle.right(ad)
        if expressao[i] == '[':
            p = turtle.position()
            h = turtle.heading()
            stack.insert(ultimo,(p,h,Lado))
            ultimo+=1
        if expressao[i] == ']':
            ultimo-=1
            turtle.up()
            turtle.setposition(stack[ultimo][0][0],stack[ultimo][0][1])
            turtle.setheading(stack[ultimo][1])
            Lado = stack[ultimo][2]
            turtle.down()
        if(expressao[i] == '('):
            j = i
            ang = ''
            rotacao = ''
            while(expressao[j] != ')'):
                if(expressao[j] == '-'):
                    rotacao = '-'
                elif(expressao[j] == '+'):
                    rotacao = '+'
                elif(expressao[j].isdigit()):
                    ang += expressao[j]
                j+=1
            angInt = int(ang)
            if(rotacao == '-'):
                turtle.left(angInt)
            elif rotacao == '+':
                turtle.right(angInt)
            i = j
        i+=1
    turtle.update()

def IdentificarRegras(regras):
    saida = []
    for i in range(len(regras)):
        if regras[i] == '=':
            regra = ''
            j = i+1
            while(regras[j] == ' '):
                j+=1
            while(regras[j] != ';' and j < len(regras)):
                regra += regras[j]
                j+=1
            saida.append(regra)
    return saida

def IdentificarTermos(regras):
    saida = regras[0]
    i = 0
    while(i < len(regras)):
        while(i < len(regras)and regras[i] != ';'):
            i+=1
        i+=1
        while(i < len(regras) and (not regras[i].isalpha())):
            i+=1
        if(i < len(regras)):
            saida = saida + regras[i]
        i+=1
    return saida

def ReconhecerTermo(termos, termo):
    i = 0
    while(termo != termos[i]):
        i+=1
        if (i >= len(termos)):
            return - 1
    return i

