import os

def limpesa_global():
    input("Press enter to continue")
    os.system('cls' if os.name == 'nt' else 'clear')

class NewGame:
    def __init__(self):
        self.new_game = int #reposnsavel por pegar o valor da posição do save que irá implementar
        self.action = ''         #uma string que definirar um simples sim e não para o save
        self.select = ''         #uma string que irá direcionar o local do save.

    def NG(self):
        self.new_game = int(input("Digite o local que deseja iniciar novo jogo:\n"))
        self.Local()        #encaminhará junto com self.select, gerará o nome para o diretório que será acessado

    def Select(self):   
        self.Verify_Past()#encaminhará a verificação da pasta
        self.NG()

        if self.new_game >=1 and 5 > self.new_game:

            
            try:     #verifica se ao caminho já existe conteúdo 
                with open(self.select, 'r'):           
                    print("Alerta! conta existente criada! deseja apagar?") 
                self.DelSave()          #encaminhará a seleção de deletamento
            except:
                with open(self.select, 'w'):    #cria a pasta txt do save
                    del self.action,self.select,self.new_game
        else:
            print("local não existente.")   
            del self.action,self.select,self.new_game

    def DelSave(self): #junto com action você definirá se quer remover o save.txt
        self.action =input("Delete this? (Y/N):\n")
        self.action = self.action.lower()
        if self.action == 'y' or self.action == 'ye' or self.action == 'yes' or self.action == 'yep':
            try:
                os.remove(self.select) #se sim estará apagado
            except OSError as e:
                print(e)    #caso haja algum erro, apresentará inexistencia da pasta (para casos especifivos e raros de manipulação de terminal e manual)
            else:
                print("Deletado com sucesso.")
                del self.action,self.select,self.new_game

        elif self.action == 'n' or self.action == 'no' or self.action == 'not' or self.action == 'nop' or self.action == 'not' or self.action == 'noti' or self.action == 'notin' or self.action == 'noting':
            print("Cancelado.")             #Caso usuário desista, simplesmente não fazer nada
            del self.action,self.select,self.new_game 
        else:
            print("Não conseguimos identificar seu desejo, Tente novamente.")   #caso as duas opções não sejam atendidas, simplesmente mandar um balão notificando que não foi entendido 
            del self.action,self.select,self.new_game
    
    def Local(self): #simples local para gerar nome local do arquivo acessado em txt em seu diretório final especificado
        self.select = str("save//save"+str(self.new_game)+".txt") 
    
    def Verify_Past(self): #verificação simples da pasta
        GREEN = "\033[0;32m"
        RED   = "\033[1;31m" 
        RESET= "\033[0;0m"
        x= str("./save")
        if os.path.exists("./save") == True:
            for i in range(1,5,1):
                if os.path.exists(x+"/save"+str(i)+".txt") == True:
                    print( GREEN +"save[",i,"] : SALVO"+RESET)
                else:
                    print(RED + "save[",i,"] : VASIO"+RESET)
        else:
            os.makedirs(x)
        del x,GREEN,RED,RESET


class LoadGame(NewGame):
    
    def Load_save(self):
        self.verify_past()

    
    def verify_past(self):
        CYAN = "\033[1;36m"
        RESET= "\033[0;0m"
        if os.path.exists("./save") == True:
            for i in range(1,5,1):
                if os.path.exists("./save/save"+str(i)+".txt") == True:
                    print(CYAN +"save[",i,"]"+RESET)
        else:
            print("pasta não existe.")
        del CYAN,RESET
    
    def Select(self):
        print("Selecione o save que desejar(B-back)")
        return super().Select()

class menu:
    def __init__(self,language):
        self.language =language
    

if (__name__) == "__main__": #menu.

    i = ''
    while i != '3':
        print(".==================================================================================================================================.")
        
        i = input("|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t   |\n|\t\t\t\t\t\t\t  New Game = 1\t\t\t\t\t\t\t\t   |\n|\t\t\t\t\t\t\t  Load Game = 2\t\t\t\t\t\t\t\t   |\n|\t\t\t\t\t\t\t  Config = 3\t\t\t\t\t\t\t\t   |\n|\t\t\t\t\t\t\t  Exit = 3\t\t\t\t\t\t\t\t   |\n|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t   |\n.==================================================================================================================================.\n\nSelect:\n")
        if i == '1':
            
            NewGame().Select()
        elif i == '2':
            LoadGame().Load_save()
        limpesa_global()
    


#menu iniciar vai necessitar disto, new game com 4 opções de save