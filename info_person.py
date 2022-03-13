from Terminal import*
from Terminal import MenuTerminal
from ballon import*
from config import Config_Menu
       
class Person(MenuTerminal):
    def __init__(self,language,local_save):
        MenuTerminal.__init__(self,language)
        self.local_save = local_save
        self.local= 'save/save'+str(local_save)+'.txt'
        self.all = {}
        self.persona_info={}
        self.information_user =[]
        self.listk=['Point','Nick','Gen','Lvl','Xp','Hp','Mp','For','Int','Def','helmet','armor','legs','left-hand','right-hand','amulet']
        self.listv=['POINT=','Nick=','Gen=','LVL=','XP=','HP=','MP=','FOR=','INT=','DEF=','helmet=','armor=','legs=','left-hand=','right-hand=','Amulet=']

    def __str__(self,string):
        MenuTerminal(self.language).__str__(string)

    def Open_and_read(self):    #Ler arquivo. por isso >>> mode='r'
        with open(self.local,mode='r',encoding='utf-8') as save_local:
            self.information_user = save_local.readlines()

    def Open_and_write(self):    #limpar e salvar. por isso >>> mode='w'
        with open(self.local,mode='w',encoding='utf-8') as write_local:
            for i in self.information_user: #acessando linha a linha para incrementar  no texto as informações para serem colhidas na proxima leitura
                #print(i,end='')
                write_local.write(i)

    def dict_all(self): #transformar duas listas em dict
        for k,v in zip(self.listk,self.listv):
            self.all[k]=v

    def alocate_info(self): #função propria para pegar os valores do save ou salvar existentes

        self.backpack_search()
        self.dict_all()
        self.Acess_info()
        return self.all
    
    def save_info(self,**dictall): #gerando uma lista de comparações iguais  

        self.persona_info= dictall.copy()
        self.alocate_info
        self.backpack_search()
        self.dict_all()
        self.saved_info()

    def saved_info(self):
        
        self.Open_and_read()# 
        loop =len(self.information_user)
        for x in range(0,loop,1):
            boop = True
            for k,v,k1,v1 in zip(self.persona_info.keys(),self.persona_info.values(),self.all.keys(),self.all.values()):
                if v1 in self.information_user[x] and boop == True:
                    self.information_user.pop(x)
                    self.information_user.insert(x,str(v1)+str(v)+'\n')
                    #self.information_user = str(v1)+str(v)
                    boop = False


        self.Open_and_write()
        
    def backpack_search(self): 
        self.Open_and_read()
        for x in self.information_user:
            if '|BAG-Itens|' in x:
                for i in range(1,10+1,1):
                    self.listk.append(str(i)+ 'item')
                    self.listv.append(str(i)+ 'item=')
            if '|BAG-Itens-I|' in x:
                for i in range(1,20+1,1):
                    self.listk.append(str(i)+ 'item')
                    self.listv.append(str(i)+ 'item=')
            if '|BAG-Itens-II|' in x:
                for i in range(1,30+1,1):
                    self.listk.append(str(i)+ 'item')
                    self.listv.append(str(i)+ 'item=')
        del self.information_user

    def Acess_info(self):
        self.Open_and_read()
        for key,value, in zip(self.all.keys(),self.all.values()):
            for comparation in self.information_user:
                if value in comparation:
                    self.all[key] = str(comparation[len(value):-1])

class Set(MenuTerminal):
    glogal_itens_name={
        'None':'None',
        '8_helm0': 'chapel de couro',
        '8_helm1': 'chapel de festa-pontudo',
        '8_helm2': 'chapel? de Bau',
        '8_helm3': 'chapel? de Mimico-Bau',
        '8_helm4': 'capacete de latao',
        '8_helm5': 'capacete de ferro',
        '8_helm6': 'chapel de Bruxo cinzento',
        '8_helm7': 'chapel de aprendiz de bruxa',
        '8_helm8': 'coroa de lillith',
        '8_helm9': 'chapel do Mago Implacavel',
        '8_helm10': 'coroa de ouro Rei-Arthur',
        '8_helm11': 'capacete enferrujado quebrado',
        #/\helmet
        '5_armr0':'camisa de couro',
        '5_armr1':'camisa de festa',
        '5_armr2':'camisa de trapo',
        '5_armr3':'camisa de trapo de calaboço',
        '5_armr4':'armadura de latao',
        '5_armr5':'armadura de ferro',
        '5_armr6':'manto do bruxo cinzento',
        '5_armr7':'manto de aprendiz de bruxa',
        '5_armr8':'Vestido de lillith',
        '5_armr9':'manto do mago implacavel',
        '5_armr10':'armadura de Ouro do Rei arthur',
        '5_armr11':'armadura enferrujado quebrado',
        #/\armor
        '2_legs0':'short de couro',
        '2_legs1':'calça de bolinha',
        '2_legs2':'tanga de trapo',
        '2_legs3':'tanga fina de trapo',
        '2_legs4':'calça da armadura de latao',
        '2_legs5':'calça da armadura de ferro',
        '2_legs6':'calça longa do bruxo cinzento',
        '2_legs7':'Saia longa da aprendiz de bruxa',
        '2_legs8':'Conjunto de cintura do vestido da lillith',
        '2_legs9':'Sunga de pato',
        '2_legs10':'Conjunto de calça da armadura de Ouro do Rei arthur',
        '2_legs11':'calça de armadura enferrujado quebrado',
        #/\legs
        '7_amulet_0':'Amuleto da facçao do Deus da Reencarnacao',
        '7_amulet_0':'Amuleto da facçao do Deus do Paraiso',
        '7_amulet_0':'Amuleto da facçao do Mago Supremo',
        '7_amulet_0':'Amuleto da facçao da Primeira!',
        #/\amulet
        '4_left0':'escudo redondo de madeira',
        '4_left1':'escudo redondo de latao',
        '4_left2':'escudo quadrado de ferro',
        '4_left3':'livro do antigo mago cinzento',
        '4_left4':'escudo de ferro com perola de dragao',
        '4_left5':'livro antigo de ferro da bruxa',
        '4_left6':'orbe de cristal fajudo',
        '4_left7':'escudo de Prata leve',
        '4_left8':'Livro com gravuras',
        '4_left9':'Orbe de Cristal Sombrio da lillith',
        '4_left10':'Duplo-Bracelhete de ouro do Rei Arthur',
        '4_left10':'Escudo enferrujado',
        #/\shield
        '6_right0':'Espada de madeira',
        '6_right1':'cajado de madeira',
        '6_right2':'cajado do pantano',
        '6_right3':'espada de madeira de latao',
        '6_right4':'espada de latao',
        '6_right5':'espada de ferro',
        '6_right6':'cajado de sabugueiro magica',
        '6_right7':'varinha de condao',
        '6_right8':'maça de ferro bruto',
        '6_right9':'Luvas da lillith',
        '6_right10':'Grande Espada do Rei Arthur',
        '6_right11':'espada enferrujada',
        
        '#HPotion':'Healt Potion',
        '#HPotionS':'Great Potion',
        '#MPotion':'Mana Potion',
        '#MPotionS':'Great Potion',
        '$key_0001':'Chave de Missao primeira sala',
        '$key_0002':'Chave de Missao Segunda sala',
        #/\arm
    }
    glogal_itens_status_int={
        'None':0,
        '8_helm0':0,
        '8_helm1':0,
        '8_helm2':2,
        '8_helm3':5,
        '8_helm4':0,
        '8_helm5':0,
        '8_helm6':3,
        '8_helm7':4,
        '8_helm8':10,
        '8_helm9':10,
        '8_helm10':10,
        '8_helm11':-1,
        #/\Helmet inteligence
        '5_armr0':0,
        '5_armr1':0,
        '5_armr2':1,
        '5_armr3':2,
        '5_armr4':0,
        '5_armr5':0,
        '5_armr6':4,
        '5_armr7':5,
        '5_armr8':10,
        '5_armr9':10,
        '5_armr10':10,
        '5_armr10':10,
        '5_armr11':-1,
        #/\armor inteligence
        '2_legs0':0,
        '2_legs1':0,
        '2_legs2':1,
        '2_legs3':2,
        '2_legs4':0,
        '2_legs5':4,
        '2_legs6':5,
        '2_legs7':6,
        '2_legs8':10,
        '2_legs9':10,
        '2_legs10':10,
        '2_legs11':-1,
        #/\legs inteligence
        '7_amulet0':0,
        '7_amulet1':0,
        '7_amulet2':0,
        '7_amulet3':0,
        #/\amulet inteligence
        '4_left0':0,
        '4_left1':0,
        '4_left2':0,
        '4_left3':7,
        '4_left4':5,
        '4_left5':7,
        '4_left6':3,
        '4_left7':0,
        '4_left8':10,
        '4_left9':25,
        '4_left10':25,
        '4_left10':-1,
        #/\shield inteligence
        '6_right0':0,
        '6_right1':0,
        '6_right2':9,
        '6_right3':0,
        '6_right4':0,
        '6_right5':0,
        '6_right6':13,
        '6_right7':15,
        '6_right8':0,
        '6_right9':25,
        '6_right10':25,
        '6_right11':0,
        #/\arm inteligence
        '#HPotion':0,
        '#HPotionS':0,
        '#MPotion':0,
        '#MPotionS':0,
        '$key_0001':0,
        '$key_0002':0,
    }
    glogal_itens_status_for={
        'None':0,
        '8_helm0':0,
        '8_helm1':0,
        '8_helm2':2,
        '8_helm3':3,
        '8_helm4':2,
        '8_helm5':2,
        '8_helm6':0,
        '8_helm7':0,
        '8_helm8':10,
        '8_helm9':10,
        '8_helm10':10,
        '8_helm11':-1,
        #/\helmet force
        '5_armr0':1,
        '5_armr1':0,
        '5_armr2':0,
        '5_armr3':1,
        '5_armr4':2,
        '5_armr5':3,
        '5_armr6':1,
        '5_armr7':2,
        '5_armr8':10,
        '5_armr9':5,
        '5_armr10':10,
        '5_armr11':-1,
        #/\armor force
        '2_legs0':1,
        '2_legs1':0,
        '2_legs2':0,
        '2_legs3':1,
        '2_legs4':2,
        '2_legs5':3,
        '2_legs6':1,
        '2_legs7':2,
        '2_legs8':10,
        '2_legs9':8,
        '2_legs10':25,
        '2_legs11':-1,
        #/\legs force
        '7_amulet_0':0,
        '7_amulet_1':0,
        '7_amulet_2':0,
        '7_amulet_3':0,
        #/\amulet force
        '4_left0':0,
        '4_left1':0,
        '4_left2':0,
        '4_left3':0,
        '4_left4':0,
        '4_left5':0,
        '4_left6':0,
        '4_left7':0,
        '4_left8':0,
        '4_left9':10,
        '4_left10':10,
        '4_left10':-1,
        #/\shield force
        '6_right0':10,
        '6_right1':3,
        '6_right2':5,
        '6_right3':8,
        '6_right4':11,
        '6_right5':12,
        '6_right6':6,
        '6_right7':3,
        '6_right8':15,
        '6_right9':25,
        '6_right10':25,
        '6_right11':15,
        #/\armr force
        '#HPotion':0,
        '#HPotionS':0,
        '#MPotion':0,
        '#MPotionS':0,
        '$key_0001':0,
        '$key_0002':0,
    }
    glogal_itens_status_def={
        'None':0,
        '8_helm0':1,
        '8_helm1':0,
        '8_helm2':3,
        '8_helm3':3,
        '8_helm4':2,
        '8_helm5':3,
        '8_helm6':0,
        '8_helm7':1,
        '8_helm8':10,
        '8_helm9':4,
        '8_helm10':10,
        '8_helm11':-1,
        #/\helmet def
        '5_armr0':2,
        '5_armr1':2,
        '5_armr2':1,
        '5_armr3':0,
        '5_armr4':5,
        '5_armr5':6,
        '5_armr6':3,
        '5_armr7':4,
        '5_armr8':10,
        '5_armr9':7,
        '5_armr10':25,
        '5_armr11':-1,
        #/\armor def
        '2_legs0':1,
        '2_legs1':1,
        '2_legs2':0,
        '2_legs3':0,
        '2_legs4':5,
        '2_legs5':6,
        '2_legs6':3,
        '2_legs7':4,
        '2_legs8':10,
        '2_legs9':6,
        '2_legs10':25,
        '2_legs11':-1,
        #/\legs def
        '7_amulet_0':0,
        '7_amulet_1':0,
        '7_amulet_2':0,
        '7_amulet_3':0,
        #/\amulet def
        '4_left0':3,
        '4_left1':4,
        '4_left2':5,
        '4_left3':2,
        '4_left4':7,
        '4_left5':5,
        '4_left6':3,
        '4_left7':8,
        '4_left8':10,
        '4_left9':25,
        '4_left10':25,
        '4_left10':-1,
        #/\shield def
        '6_right0':0,
        '6_right1':0,
        '6_right2':0,
        '6_right3':0,
        '6_right4':0,
        '6_right5':0,
        '6_right6':0,
        '6_right7':0,
        '6_right8':0,
        '6_right9':25,
        '6_right10':25,
        '6_right11':-1,
        #/\armr def
        #\/item...
        '#HPotion':0,
        '#HPotionS':0,
        '#MPotion':0,
        '#MPotionS':0,
        '$key_0001':0,
        '$key_0002':0,
    }
    global_intens={
        'None':'None',
        '#HPotion':50,
        '#HPotionS':100,
        '#MPotion':25,
        '#MPotionS':50,
        '$key_0001':'Key_0001',
        '$key_0002':'Key_0002',
        #itens
    } #self.glogal_itens_name[item]

    def __init__(self,language,**Dictinfo):
        MenuTerminal.__init__(self,language)
        self.dictinfo = Dictinfo
        self.x = [ '8','5','2','7','4','6']
        self.y = [ 'helmet','armor','legs','amulet','left-hand','right-hand']
        self.z=['Point','Nick','Gen','Lvl','Xp','Hp','Mp','For','Int','Def']

    def __str__(self,string):
        MenuTerminal(self.language).__str__(string)

    def take(self,item):
        for i in range(0,len(self.x),1):
            if item[0] in self.x[i]: # item helmet only
                self.SET(item,i)
                return self.dictinfo
        self.BP_direct(item)
        return self.dictinfo
        
    def acess_set(self):
        lista = [i for i in self.dictinfo.keys()]
        cont=int(0)
        for lista in self.y:
            print('\n[',cont,']',lista,':\t',self.glogal_itens_name[self.dictinfo[lista]],end='')
            cont=int(cont)+int(1)
        number= int(input("\nDigite o numero da tabela para alterar item <Digite (-1) Para Sair>:\n"))
        if number == int(-1) :
            return self.dictinfo
        self.acess_set1(number)
        


    def acess_set1(self,number): 
        contador = int(1)#contador que servirá para medir o tamanho da mochila
        lista = [i for i in self.dictinfo.keys()] #lista especifica para percorres
        for i in lista[16:]:
            print("{}={}".format(i,self.glogal_itens_name[self.dictinfo[i]])) #mostrar itens
            contador=int(contador)+int(1)                #contador está reponsável pelas casa que tem na lista do backpack de itens, no caso o tamanho da backpack
        select = self.recursive(contador) #select éresponsável de receber o valor da recursividade
        self.comparation(select,number)#>item da mochila #number é o numero do set

    def comparation(self,select,number): #select=backpack.number=set
        take_item = str(self.dictinfo[str(select)+'item']) #seleciona item da mochila
        cont_position_set=''
        for i in range(0,len(self.x),1): #pegar item do set
            if str(i) in str(number): # as listas self.x e self.y são do mesmo tamanho, então...
                cont_position_set = self.y[i] #pegar valor correspondente com o numero do item na lista em y
        set_item = str(self.dictinfo[cont_position_set])
        for i in self.x: #possiveis espaço que podem ser preenchidos 2=lefs,8=helmet,7=amulet...
            if take_item[0] in i: #diz se o item pode ser trocado sim ou não.. se sim, trocar e voltar para o set. Mostrar erro e voltar ao set
                if str(i)  in str(take_item[0]):
                    self.update_status_item(take_item,set_item)#-set,+backpack
                    self.dictinfo.update({str(select)+'item': set_item , cont_position_set:take_item})
                    return self.dictinfo 
                elif str(i)  not in str(take_item[0]):
                    self.__str__('_comparation0')
                    
                
    def recursive(self,cont): #tamanho da mochila
        self.__str__('_recursive0')
        select_this = int(input())
        if int(select_this) >= int(1) and int(select_this) <= int(cont):
            return select_this  #só sair quando selecionar um valor da mochila.
        elif select_this == -1:
            self.acess_set()
        self.recursive(cont)

    def SET(self,item,i):
        if self.dictinfo[self.y[i]]=='None':
            self.update_status_item('None',item)
            self.dictinfo[self.y[i]] = item #self.glogal_itens_name[item]
        else:
            x = input("Deseja jogar na mochila?(Y/N):").lower()
            if x=='y' or x =='ye' or x =='yes' or x=='yep':
                self.BP_direct(item)
            else:
                return self.dictinfo
            
    def acess_backpack(self,Mission):
        lista =[]
        lista =self.len_backpack(lista,Mission)

        Mission = self.select_item(lista,Mission)

        return Mission
        

    def len_backpack(self,lista,Mission):#Mostrar imagem da mochila
        lis = [ i for i in self.dictinfo.keys()]
        for i in lis[16:]:
            lista.append(i)
            print('(',i,' :',self.glogal_itens_name[self.dictinfo[i]],')',end=' ')
        return lista

    def select_item(self,lista,Mission):
        self.__str__('_select_item')
        item = input()
        if item == '0':
            return self.dictinfo
        item = str(item)+'item'
        strng=''
        for x in lista:
            if item in x:
                strng = str(self.dictinfo[item])
                if strng == 'None':
                    self.__str__('_select_item0')
                elif strng[0] == '8' or strng[0] == '5' or strng[0] == '2' or strng[0] == '7' or strng[0] == '4' or strng[0] == '6':
                    self.__str__('_selct_status0')
                    print("For:{}\nDef:{}\nInt:{}\n".format(self.glogal_itens_status_for[strng],self.glogal_itens_status_def[strng],self.glogal_itens_status_int[strng]))
                    self.__str__('_selct_status1')
                    x=input()
                    if x ==1:self.acess_set()
                    if x ==2:self.BP_Dell(strng)
                elif strng[0] == '$':
                    self.__str__('_select_item1')
                    x = int(input())
                    if  x == int(1) :self.BP_Dell(strng)
                    if  x == int(2) :
                        Mission = self.BP_Use(strng,Mission)
                        return Mission
                elif strng[0] == '#':
                    self.__str__('_select_item2')
                    x = int(input())
                    if  x == 1 :self.BP_Dell(strng)
                    if  x == 2 :self.BP_Use(strng)
                del strng
        del item 
        self.__str__('_select_item3')
        x=str(input())
        if x =='y' or x =='Y':
            self.select_item(lista,Mission)
       
    def acess_status(self):
        self.list_status()

    def list_status(self): #vê status
        for i in self.z:
            print(str(i),':',self.dictinfo[i])
    
    def update_status_item(self,item1,item2): #só faz sentido implementar no momento em que estiver trocando intem, em outro local isso é desnecessario e vulgar
            self.dictinfo['Def']= (int(self.dictinfo['Def'])-int(self.glogal_itens_status_def[item1]))+int(self.glogal_itens_status_def[item2]) #tirando poder de item 1 e incrementando item_2
            self.dictinfo['For']= (int(self.dictinfo['For'])-int(self.glogal_itens_status_for[item1]))+int(self.glogal_itens_status_for[item2]) #o mesmo para forca
            self.dictinfo['Int']= (int(self.dictinfo['Int'])-int(self.glogal_itens_status_for[item1]))+int(self.glogal_itens_status_for[item2]) # e o mesmo para inteligencia

    def update_status_per_lvl(self):
        self.__str__('update_status_per_level')
        update = int(input())
        if update == 3:self.dictinfo['For']
        elif update == 1:self.dictinfo['Int']
        else:self.dictinfo['Def']= int(self.dictinfo['Def'])
    
    def BP_Dell(self,item):
        lista = [i for i in self.dictinfo.keys()]
        item = str(item)
        for i in lista[16:]:
            if self.dictinfo[i] == item:
                if item[0] == '$':
                    self.__str__('_BP_Dell_0')
                else:
                    self.dictinfo == 'None'

    def BP_Use(self,item,Mission):
        lista = [i for i in self.dictinfo.keys()]
        item = str(item)
        for i in lista[16:]:
            if self.dictinfo[i] == item:
                
                if item[0] =='$':
                    if Mission == True:
                        
                        self.dictinfo[i] == 'None'
                        Mission = False 
                        return Mission

                if item[0] == '#':
                    self.dictinfo[i] == 'None'
                else:
                    self.__str__('_BP_Use_0')


    def BP_direct(self,item): #jogue itens direto para backpack caso haja espaço vasio nela

        lista = [i for i in self.dictinfo.keys()]
        lista_espaco_vasio =[]
        cont = int(0)
        for i in lista[16:]:
            if self.dictinfo[i] =='None':
                cont=int(cont)+int(1)

        if cont == 0:
            self.__str__('_BP_direct_0')
            x =input()
            if x == 'y' or x =='Y' or x =='YES' or x =='Yes' or x =='yes' or x =='0':
                lista_item = [ i for i in self.dictinfo]
                contador = 1
                for i in lista_item[16:]:
                    print('\n'+str(i)+':'+str(self.dictinfo[str(contador)+'item'])+'=='+str(contador),end='')
                    contador= contador+1
                self.__str__('_BP_direct_1')
                x1 = input()
                if int(x1) == 0:
                    self.__str__('_BP_direct_2')
                    return self.dictinfo
                elif int(x1) >= 1 and int(x1) <=contador: # verifica
                    self.dictinfo[str(x1)+'item'] = item ##self.glogal_itens_name[item]
                    return self.dictinfo
        elif cont !=0:
            for z in lista_espaco_vasio:
                print("|",z,':None',end='')
            b=int(1)
            self.loop_search(lista,b,item)
        return self.dictinfo
    
    def loop_search(self,lista,var,item):
        if var == 0:
            return self.dictinfo
        else:
            for i in lista[16:]:
                if self.dictinfo[i] == 'None':
                    self.dictinfo[i] = item #self.glogal_itens_name[item]
                    return self.dictinfo
                    
        self. loop_search(lista,var,item)

class UP(Set,MenuTerminal):    

    def __init__(self,language,**dictinfo):
        Set.__init__(self,language,**dictinfo)
        MenuTerminal.__init__(self,language)
        self.dictinfo = dictinfo

    def __str__(self,string):
        MenuTerminal(self.language).__str__(string)

    def up(self,up):
        #level_up ={}
        y = self.dictinfo['Lvl']
        x = int(MenuTerminal(self.language).infolist(0,y))
        z = str(self.dictinfo['Xp'])
        print(z)
        z = int(z)+int(up)
        while x != -1:
            if int(z) >=int(x):
                self.update_status_per_lvl()
                z = int(z)-int(x)
                y = int(y)+1
                self.__str__('_UP0') #remover depois:
                x = MenuTerminal(self.language).infolist(0,y)     #(level_up[str(y)])
            else:
                y = str(y)
                self.dictinfo['Lvl']=y
                self.dictinfo['Xp']=str(z)
                break        
        del y,z,x

    def life_mana(self,ty,up):
        aux = int(self.dictinfo[ty])
        aux = int(aux) - int(up)
        self.dictinfo[ty]= aux
        if  ty == 'Hp':
            if aux <=0:
                del aux
                return 1 #informar que acabou a vida
            else:return 0 #informar que acabou que não acabou
        elif ty == 'Mp':
            if aux <0:
                aux = int(aux) + int(up)
                self.dictinfo[ty]= aux
                del aux
                return 1 #informar que acabou a mana
            else:return 0 #informar que acabou que não acabou

    def STS(self,ty,up):
        lista =[i for i in self.dictinfo.keys()]
        for i in lista[0:8]:
            if ty in i:
                if ty =='Xp':
                    self.up(up)
                elif ty == 'Hp' or ty == 'Mp':
                    pass
                else:
                    self.dictinfo.update({i:str(up)})
        return self.dictinfo


    def Newxt_Point(self):
        aux =int(self.dictinfo['Point'])
        aux =+1
        self.dictinfo['Point'] = aux

    def returnpoint(self,i):

        if i == 0:
            aux = int(self.dictinfo['Point'])
            if aux >=1:
                aux-=1
            self.dictinfo['Point']=aux
            self.dictinfo['Hp']=100
            self.dictinfo['Mp']=50
            del aux

        elif i == 1:
            self.__str__('_mana')



class Damage(UP,Set,MenuTerminal):
    def __init__(self,language,**dictinfo):
        UP.__init__(self,language,**dictinfo)
        Set.__init__(self,language,**dictinfo)
        MenuTerminal.__init__(self,language)

        

    def Action_Option(self,Mission):
        MenuTerminal(self.language).__str__('_actopt_0')
        tip = 0
        tip=int(input())
        if tip == 1:
            MenuTerminal(self.language).__str__('_actopt_1');print(self.dictinfo['For'],'>')
            MenuTerminal(self.language).__str__('_actopt_2');print(self.dictinfo['Int'],'/',self.dictinfo['Mp'],'-Mp>')
            tip = 0
            tip = int(input())
            if tip == 1:return 0
            if tip == 2:
                x =self.damage_int()
                return x
        if tip == 2:return 2
        if tip == 3:
            if Mission == False:
                self.acess_backpack(Mission)
            if Mission == True:
                Mission = self.acess_backpack(Mission)
                return Mission
            return 3
        if tip == 4:
            self.acess_status()
            return 4
        else:return 5

    def damage_int(self): #652
        i =self.life_mana('Mp',2)
        if i == 0:
            #self.dictinfo['Mp']=self.dictinfo['Mp']-15
            return 1
        else:
            MenuTerminal(self.language).__str__('_actopt_3')
            return -1
    def sense_damage(self,power):
        power_reflect=int(self.dictinfo['Def'])
        power_reflect= int(power_reflect)-int(power)
        i = int(self.life_mana('Hp',power_reflect))
        if i== 0:
            self.dictinfo['Hp']=self.dictinfo['Hp']-power_reflect
        else:
            self.death_return(i)
    
    def death_return(self,i):
        MenuTerminal(self.language).__str__('_actopt_4')
        print("Você Morreu...")
        self.returnpoint(i)