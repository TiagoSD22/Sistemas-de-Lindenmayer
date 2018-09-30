import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import colorchooser

import Figuras

def Desenhar(index,lado,geracoes,axioma = '', regras = '', ae = 90, ad = 90,cor = "#000000",espessura = 0,randomL = 0,randomAn = 0):
        Figuras.SetColor(cor,espessura)
        if(index == 0):
            Figuras.InterpretarKochIsland(lado,geracoes)
        if(index == 1):
            Figuras.InterpretarKochSnowFlake(lado,geracoes)
        if(index == 2):
            Figuras.InterpretarKochIslandLake(lado,geracoes)
        if(index == 3):
            Figuras.InterpretarKochBox(lado,geracoes)
        if(index == 4):
            Figuras.InterpretarKochRets(lado,geracoes)
        if(index == 5):
            Figuras.InterpretarKochStar(lado,geracoes)
        if(index == 6):
            Figuras.InterpretarKochDragon(lado,geracoes)
        if(index == 7):
            Figuras.InterpretarKochTrianguloB(lado,geracoes)
        if(index == 8):
            Figuras.InterpretarKochMaze(lado,geracoes)
        if(index == 9):
            Figuras.InterpretarKochHex(lado,geracoes)
        if(index == 10):
            Figuras.InterpretarKochPyramid(lado,geracoes)
        if(index == 11):
            Figuras.InterpretarKochSquare(lado,geracoes)
        if(index == 12):
            Figuras.InterpretarHilbertCurve(lado,geracoes)
        if(index == 13):
            Figuras.InterpretarHilbertCurveII(lado, geracoes)
        if(index == 14):
            Figuras.InterpretarSierpinskiSquare(lado,geracoes)
        if(index == 15):
            Figuras.InterpretarCrystal(lado,geracoes)
        if(index == 16):
            Figuras.InterpretarString(axioma,regras,ae,ad,lado,geracoes,randomL,randomAn)

class Application(Frame):

    def combobox_handler(self,event):
        index = self.lista.current()
        if(index == 16):
            self.axiomaLabel.lift(self.frame)
            self.axiomaLabel.lift(self.frame)   
            self.axioma.lift(self.frame)
            self.regrasLabel.lift(self.frame)
            self.regras.lift(self.frame)
            self.ajuda.lift(self.frame)
            self.aeLabel.lift(self.frame)
            self.ae.lift(self.frame)
            self.adLabel.lift(self.frame)
            self.ad.lift(self.frame)
            self.rpLabel.lift(self.frame)
            self.rp.lift(self.frame)
            self.raLabel.lift(self.frame)
            self.ra.lift(self.frame)
            self.previaLabel.lower(self.frame)
        else:
            self.axiomaLabel.lower(self.frame)
            self.axioma.lower(self.frame)
            self.regrasLabel.lower(self.frame)
            self.regras.lower(self.frame)
            self.aeLabel.lower(self.frame)
            self.ajuda.lower(self.frame)
            self.ae.lower(self.frame)
            self.adLabel.lower(self.frame)
            self.ad.lower(self.frame)
            self.rpLabel.lower(self.frame)
            self.rp.lower(self.frame)
            self.raLabel.lower(self.frame)
            self.ra.lower(self.frame)
            self.previaLabel.lift(self.frame)

        if(index >= 0 and index < 16):
            imagens = ["Imagens/island.gif","Imagens/snowflake.gif","Imagens/islandlake.gif",
                       "Imagens/box.gif","Imagens/rets.gif","Imagens/star.gif",
                       "Imagens/dragon.gif","Imagens/sierp.gif","Imagens/maze.gif",
                       "Imagens/hex.gif","Imagens/pyramid.gif","Imagens/square.gif",
                       "Imagens/hilbert.gif","Imagens/hilbert2.gif","Imagens/sierpsquare.gif",
                       "Imagens/crystal.gif"]
            self.imagem = tkinter.PhotoImage(file = imagens[index])
            self.previa.configure(highlightthickness = 2)
            self.previa.configure(background="#ffffff", highlightbackground=self.MainFrame.cget("bg"))
            self.previa.create_image(2,2,image = self.imagem,anchor = NW)
        else:
            self.previa["background"] = self.frame.cget("bg")
            self.previa.configure(highlightthickness = 0)
            self.imagem = tkinter.PhotoImage()

    def Ajuda(self):
        self.AjudaDialogo = tkinter.messagebox.showinfo("Ajuda","Use a seguinte sintaxe ao digitar as regras:"
                                                        "\n - Use '=' para atribuir uma regra a um símbolo (Ex: F = F)"
                                                        "\n - Separe as regras por ';' (Ex: F = X; X = F)"
                                                        "\n - A última regra também deve ser seguida por um ';' (Ex: F = X; X = F;)"
                                                        "\n - Somente estes símbolos são considerados válidos:"
                                                        "\n\t +Significa girar para a direita"
                                                        "\n\t - Significa girar para a esquerda"
                                                        "\n\t < Significa girar para esquerda 90º graus"
                                                        "\n\t > Significa girar para direita 90º graus"
                                                        "\n\t | Significa girar 180° graus"
                                                        "\n\t [ Significa salvar o atual estado da tartaruga\n\t   (posição,orientação e tamanho do lado)"
                                                        "\n\t ] Significa recuperar o último estado salvo da tartaruga"
                                                        "\n\t f Significa andar para frente sem riscar"
                                                        "\n\t S Significa diminuir o lado pela metade"
                                                        "\n\t b Significa andar 100 pixels para trás sem riscar "
                                                        "\n\tObs: Qualquer outra letra será entendida como 'andar para frente riscando'"
                                                        " assim, para F,X,Z,a,v, por exemplo, não serão feitas distinções."
                                                        "\n - É possível girar um ângulo arbitrário especificando-o entre parênteses, por exemplo:"
                                                        "\n (-90), fará a tartaruga girar 90º para a esquerda, (+45), girar 45° para a direita."
                                                        "Assim, uma regra do tipo F+F-F-F, para um ângulo esquerdo de 60° e direito de 120°, por exemplo,"
                                                        "poderia ser reescrita como: F(+120)F(-60)F(-60)F")

    def SelecionarCor(self):
        self.cor = tkinter.colorchooser.askcolor("black",title = "Tabela de Cores")
        self.corbt["bg"] = self.cor[1]

    def createWidgets(self):
        bg = "#ff9933"
        self.MainFrame = tkinter.Frame(self)
        self.MainFrame.pack(side = "top", fill = "both", expand = "true")
        self.MainFrame.configure(background = "#2a2a2a")
        self.frame = tkinter.Canvas(self,width = 320,height = 485)
        self.frame["relief"] = RIDGE
        self.frame["borderwidth"] = 10
        self.frame["background"] = bg
        self.frame.grid(in_ = self.MainFrame,padx = 10,pady = 10)
        frame_id = self.frame.create_window(0,0,anchor = NW)
        
        self.listaLabel = ttk.Label(self,text = "FIGURAS")
        self.frame.itemconfigure(frame_id,window = self.listaLabel)
        self.listaLabel.place(in_ = self.frame,x = 15, y = 18)
        self.listaLabel.configure(background = bg, foreground = self.MainFrame.cget("bg"))

        self.lista = ttk.Combobox(self.frame)
        self.lista["values"] = ["Island","Snowflake",
                                "IslandLake","Box",
                                "Rectangles","Rings",
                                "Dragon","Sierpiński Triangle",
                                "Maze","Hexagonal Gosper",
                                "Pyramid","Squares","Hilbert Curve","Hilbert Curve II","Sierpiński Square","Crystal","Personalizado"]
        self.lista["width"] = 25
        self.frame.itemconfigure(frame_id,window = self.lista)
        self.lista.place(in_ = self.frame,x = 105, y = 15)
        self.lista.bind('<<ComboboxSelected>>',self.combobox_handler)

        self.ladoLabel = ttk.Label(self.frame,text = "Tamanho do lado: ")
        self.frame.itemconfigure(frame_id,window = self.ladoLabel)
        self.ladoLabel.place(in_ = self.frame,x = 15, y = 53)
        self.ladoLabel.configure(background = bg, foreground = self.MainFrame.cget("bg"))

        self.lado = ttk.Entry(self.frame)
        self.frame.itemconfigure(frame_id,window = self.lado)
        self.lado["width"] = 10
        self.lado["justify"] = "center"
        self.lado.place(in_ = self.frame,x = 238, y = 50)
        
        self.geracoesLabel = ttk.Label(self.frame,text = "Número de gerações: ")
        self.frame.itemconfigure(frame_id,window = self.geracoesLabel)
        self.geracoesLabel.place(in_ = self.frame,x = 15, y = 88)
        self.geracoesLabel.configure(background = bg, foreground = self.MainFrame.cget("bg"))

        self.geracoes = ttk.Entry(self.frame)
        self.frame.itemconfigure(frame_id,window = self.geracoes)
        self.geracoes["width"] = 10
        self.geracoes["justify"] = "center"
        self.geracoes.place(in_ = self.frame,x = 238, y = 85)

        self.axiomaLabel = ttk.Label(self,text = "Axioma: ")
        self.frame.itemconfigure(frame_id,window = self.axiomaLabel)
        self.axiomaLabel.place(in_ = self.MainFrame,x = 25, y = 133)
        self.axiomaLabel.configure(background = bg, foreground = self.MainFrame.cget("bg"))

        self.axioma = ttk.Entry(self)
        self.frame.itemconfigure(frame_id,window = self.axioma)
        self.axioma["width"] = 20
        self.axioma["justify"] = "center"
        self.axioma.place(in_ = self.MainFrame,x = 168, y = 130)

        self.regrasLabel = ttk.Label(self,text = "Regras: ")
        self.frame.itemconfigure(frame_id,window = self.regrasLabel)
        self.regrasLabel.place(in_ = self.MainFrame,x = 25, y = 168)
        self.regrasLabel.configure(background = bg, foreground = self.MainFrame.cget("bg"))

        self.ajuda = tkinter.Button(self)
        self.frame.itemconfigure(frame_id, window=self.ajuda)
        self.ajudaicon = tkinter.PhotoImage(file = "Imagens/ajuda.gif")
        self.ajuda["image"] = self.ajudaicon
        self.ajuda.place(in_ = self.MainFrame, x = 87, y = 165)
        self.ajuda["cursor"] = "question_arrow"
        self.ajuda["command"] = lambda: self.Ajuda()

        self.regras = ttk.Entry(self)
        self.frame.itemconfigure(frame_id,window = self.regras)
        self.regras["width"] = 20
        self.regras["justify"] = "center"
        self.regras.place(in_ = self.MainFrame,x = 168, y = 165)

        self.aeLabel = ttk.Label(self, text = "Ângulo Esquerdo:")
        self.frame.itemconfigure(frame_id,window = self.aeLabel)
        self.aeLabel.place(in_ = self.MainFrame,x = 25, y = 203)
        self.aeLabel.configure(background = bg, foreground = self.MainFrame.cget("bg"))

        self.ae = ttk.Entry(self)
        self.frame.itemconfigure(frame_id,window = self.ae)
        self.ae["width"] = 10
        self.ae["justify"] = "center"
        self.ae.place(in_ = self.MainFrame,x = 248, y = 200)
        self.ae.insert(0,"90")

        self.adLabel = ttk.Label(self, text = "Ângulo Direito:")
        self.frame.itemconfigure(frame_id,window = self.adLabel)
        self.adLabel.place(in_ = self.MainFrame,x = 25, y = 238)
        self.adLabel.configure(background = bg, foreground = self.MainFrame.cget("bg"))

        self.ad = ttk.Entry(self)
        self.frame.itemconfigure(frame_id,window = self.ad)
        self.ad["width"] = 10
        self.ad["justify"] = "center"
        self.ad.place(in_ = self.MainFrame,x = 248, y = 235)
        self.ad.insert(0,"90")

        self.bt = ttk.Button(self.MainFrame,text = "DESENHAR")
        self.bt["command"] = lambda:Desenhar(self.lista.current(),float(self.lado.get()),int(self.geracoes.get()),
                                             str(self.axioma.get()),str(self.regras.get()),float(self.ae.get()),float(self.ad.get()),
                                             self.corbt.cget("bg"),int(self.espessura.get()),int(self.rp.get()),int(self.ra.get()))
        self.bt.grid(pady = 20)
        self.bt["cursor"] = "hand2"
        self.bticon = tkinter.PhotoImage(file = "Imagens/apply.gif")
        self.bt["image"] = self.bticon
        self.bt["compound"] = tkinter.LEFT

        self.corLabel = ttk.Label(self,text = "Cor:")
        self.corLabel.configure(background = bg, foreground = self.MainFrame.cget("bg"))
        self.corLabel.place(x = 25, y = 265)

        self.corbt = tkinter.Button(self,width = 1,highlightthickness = 0)
        self.corbt.place(x = 55,y = 263)
        self.corbt["bg"] = "#000000"
        self.corbt["cursor"] = "hand1"
        self.corbt["command"] = lambda:self.SelecionarCor()

        self.espessuraLabel = ttk.Label(self,text = "Espessura:")
        self.espessuraLabel.configure(background = bg, foreground = self.MainFrame.cget("bg"))
        self.espessuraLabel.place(x = 25, y = 290)

        self.espessura = ttk.Entry(self,width = 3)
        self.espessura.place(x = 28, y = 310)
        self.espessura.insert(0,"0")

        self.rpLabel = ttk.Label(self,text = "Randomizar Passo(%):")
        self.rpLabel.place(in_ = self.MainFrame, x = 145, y = 260)
        self.rpLabel.configure(background = bg, foreground = self.MainFrame.cget("bg"))

        self.rp = ttk.Entry(self,width = 3,justify = CENTER)
        self.rp.place(in_ = self.MainFrame, x = 304, y = 260)
        self.rp.insert(0,"0")

        self.raLabel = ttk.Label(self, text="Randomizar Ângulo(%):")
        self.raLabel.place(in_=self.MainFrame, x=145, y=285)
        self.raLabel.configure(background=bg, foreground=self.MainFrame.cget("bg"))

        self.ra = ttk.Entry(self, width=3, justify=CENTER)
        self.ra.place(in_=self.MainFrame, x=304, y=285)
        self.ra.insert(0, "0")

        self.previaLabel = ttk.Label(self,text = "PRÉVIA")
        self.frame.itemconfigure(frame_id,window = self.previaLabel)
        self.previaLabel.place(in_ = self.MainFrame,x = 160, y = 290)
        self.previaLabel.configure(background = bg, foreground = self.MainFrame.cget("bg"))

        self.previa = tkinter.Canvas(self,width = 180, height = 180)
        self.previa.configure(background = "#ffffff",highlightbackground = self.MainFrame.cget("bg"))
        self.frame.itemconfigure(frame_id,window = self.previa)
        self.previa.place(in_ = self.MainFrame, x = 90,y = 310)

        self.axiomaLabel.lower(self.frame)
        self.axioma.lower(self.frame)
        self.regrasLabel.lower(self.frame)
        self.regras.lower(self.frame)
        self.aeLabel.lower(self.frame)
        self.ae.lower(self.frame)
        self.adLabel.lower(self.frame)
        self.ad.lower(self.frame)
        self.ajuda.lower(self.frame)
        self.rpLabel.lower(self.frame)
        self.rp.lower(self.frame)
        self.raLabel.lower(self.frame)
        self.ra.lower(self.frame)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.createWidgets()
