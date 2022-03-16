from numpy import save
from Terminal import*
from ballon import*
from config import Config_Menu
import os
from Create import *
class NewGame(Create_char,MenuTerminal):

    def __init__(self,language,new_game):
        Create_char.__init__(self,language,new_game)
        MenuTerminal.__init__(self,language)
        
        self.action = ''         #uma string que definirar um simples sim e não para o save
        self.select = ''         #uma string que irá direcionar o local do save.

    def Local(self): #simples local para gerar nome local do arquivo acessado em txt em seu diretório final especificado
        self.select = str("save//save"+str(self.new_game)+".txt") 

    def NewGame(self):
        self.__str__('_def_NG_0') #BALÃO DE COMENTARIO Geral
        self.new_game = int(input())
        self.Local()        #encaminhará junto com self.select, gerará o nome para o diretório que será acessado

    def Select(self):   
        self.Verify_Past()#encaminhará a verificação da pasta
        self.NewGame()

        if self.new_game == 0:
            return 0

        if self.new_game >=1 and 5 > self.new_game:

            
            try:     #verifica se ao caminho já existe conteúdo 
                with open(self.select, 'r'):
                    self.__str__('_def_Select_0') 
                self.DelSave()          #encaminhará a seleção de deletamento
                return self.new_game
            except:
                with open(self.select, 'w'):    #cria a pasta txt do save
                    pass
                self.create_account()
                return self.new_game  #Retorna numero da posição do jogo salvo para o Terminal  
        else:
            self.__str__('_def_Select_1')  
        
        


    def DelSave(self): #junto com action você definirá se quer remover o save.txt
        self.__str__('_def_DelSave_0')
        self.action =input()
        self.action = self.action.lower()
        if self.action == 'y' or self.action == 'ye' or self.action == 'yes' or self.action == 'yep':
            try:
                os.remove(self.select) #se sim estará apagado
            except OSError as e:
                print(e)    #caso haja algum erro, apresentará inexistencia da pasta (para casos especifivos e raros de manipulação de terminal e manual)
            else:
                self.__str__('_def_DelSave_1') #Balão Exclusão Concluido
                del self.action,self.select,self.new_game

        elif self.action == 'n' or self.action == 'no' or self.action == 'not' or self.action == 'nop' or self.action == 'not' or self.action == 'noti' or self.action == 'notin' or self.action == 'noting':
            self.__str__('_def_DelSave_2')             #Caso usuário desista, simplesmente não fazer nada
            del self.action,self.select,self.new_game 
        else:
            self.__str__('_def_DelSave_3')   #caso as duas opções não sejam atendidas, simplesmente mandar um balão notificando que não foi entendido 
            del self.action,self.select,self.new_game
        self.limpesa_global()
        self.Select()
    
    def Verify_Past(self): #verificação simples da pasta
        GREEN = "\033[0;32m"
        RED   = "\033[1;31m" 
        RESET= "\033[0;0m"
        x= str("./save")
        if os.path.exists("./save") == True:
            for i in range(1,5,1):
                if os.path.exists(x+"/save"+str(i)+".txt") == True:
                    print(GREEN,end='');self.__str__('_def_New_Verify_Past_0');print(' [',i,']'+RESET+':',end='');print(GREEN,end='');self.__str__('_def_New_Verify_Past_1');print(RESET+'.')
                else:
                    print(RED,end='');self.__str__('_def_New_Verify_Past_0');print(' [',i,']'+RESET+':',end='');print(RED,end='');self.__str__('_def_New_Verify_Past_2');print(RESET+'.')
        else:
            os.makedirs(x)
        del x,GREEN,RED,RESET


class LoadGame(MenuTerminal):

    def __init__(self,language):
        MenuTerminal.__init__(self,language)
        self.select = ''


    
    def verify_load_past(self):
        CYAN = "\033[1;36m"
        RED   = "\033[1;31m" 
        RESET= "\033[0;0m"
        local_necessary_array = [] #variavel local cujo a responsabilidade é filtrar caso exista pasta, quais possam retornar o valor de acessalas
        if os.path.exists("./save") == True:

            for i in range(1,5,1): #vai entrar em um laço for e printar na tela caso haja algum save.
                if os.path.exists("./save/save"+str(i)+".txt") == True:
                    print(CYAN);self.__str__('_def_Verify_Past_0');print(RESET,'[',end='');print(CYAN,i,end='');print(RESET,']',end='')
                    local_necessary_array.append(i) #incrementando valor na array
                else:
                    print(RED);self.__str__('_def_Verify_Past_0');print(RESET,'[',end='');print(RED,i,end='');print(RESET,']',end='')
                    #Mostrando que não há arquivos salvos
        else:
            self.__str__('_def_Verify_Past_1')  #DECLARA QUE PASTA NÃO EXISTE
            return 0
            
        i = self.Select_load(local_necessary_array)
        print(i)
        del CYAN,RESET,RED
        return i

    
    def Select_load(self,array):
        self.__str__('_def_Select_0')
        while len(self.select) != '-1':
            self.select = input()
            if self.select == '0':
                return self.select
            for x in array:
                if str(self.select) == str(x):
                    return self.select

    def Load_save(self):
        self.verify_load_past()
        return self.select

class configuration(Config_Menu,MenuTerminal):

    def __init__(self,language):
        MenuTerminal.__init__(self,language)

    def select(self):
        self.__str__('_def_select_0')
        self.__str__('_def_select_1')
        
        i =int(input())
        if i <=1 and i >=0:
            self.Reconf_languages(i)
            return i
        else:
            self.__str__('_def_select_2')
            return self.language


class Initial_Menu(NewGame,LoadGame,configuration,MenuTerminal):

    def __init__(self,language,newgame):
        NewGame.__init__(self,language,newgame)
        LoadGame.__init__(self,language)
        configuration.__init__(self,language)
        MenuTerminal.__init__(self,language)
    def __newstr__(self):
        print (".==================================================================================================================================.",end='')
        print ("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t 1-",end='');self.__str__('new')
        print ("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t 2-",end='');self.__str__('load')
        print ("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t 3-",end='');self.__str__('config')
        print ("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t 0-",end='');self.__str__('exit')
        print ("\n.==================================================================================================================================.")


    def Do_it(self):
        i = ''
        while i != '4':
            self.__newstr__()
            i = input()
            self.limpesa_global()
            if i == '1':

                select_game =self.Select()
                for x in range(1,5,1):
                    if int(select_game) == int(x):
                        return select_game
                
            elif i == '2':
                select_game =self.Load_save()
                for x in range(1,5,1):
                    if int(select_game) == int(x):
                        return select_game

            elif i == '3':
                self.language = configuration(self.language).select()
            elif i == '0':
                sys.exit()
            self.__str__('press')   
            input()
            self.limpesa_global()

    
'''if (__name__) == "__main__": #menu.
    Menu_Inicial(0).Do_it()'''
#menu iniciar vai necessitar disto, new game com 4 opções de save