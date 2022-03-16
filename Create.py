
from Terminal import *
from Menu import*

class Create_char(MenuTerminal):

    def __init__(self,language,save):
        MenuTerminal.__init__(self,language)
        self.aux = ''
        self.local = 'save/save'
        self.save = save

    def delete(self):
        os.remove(str(self.local)+str(self.save))

    def create_account(self):
        for i in range(0,6,1):
            MenuTerminal(0).limpesa_global()
            MenuTerminal(self.language).__str__('_create_account0')
            if i == 0: self.Check_point()
            elif i == 1:self.create_name()
            elif i == 2:self.create_sex()
            elif i == 3:self.create_status()
            elif i == 4:self.create_set()
            else:self.create_bag()
            if self.aux ==0:
                self.delete
                return 0
            MenuTerminal(self.language).limpesa_global()
            self.reader()
        return self.save
    

    def Check_point(self): #CHECK POINT
        self.aux = "|Save|\n\nPOINT=0\n"

    def create_name(self): #CHARACTER NICK CREATE
        MenuTerminal(0).limpesa_global()
        MenuTerminal(self.language).__str__('_create_account0')
        MenuTerminal(self.language).__str__('_create_name0')
        while len(self.aux) != -1:
            self.aux=input()
            if self.aux == 0 and len(self.aux) != 0:
                break
            if len(self.aux) <= 10:
                break
        print("ola:",self.aux)
        self.aux='|Person|\n\nNick='+self.aux

    def create_sex(self): #CREATE SEX
        MenuTerminal(0).limpesa_global()
        MenuTerminal(self.language).__str__('_create_account0')
        MenuTerminal(self.language).__str__('_create_sex0')
        while self.aux != 'M' and self.aux != 'F' and self.aux != 'm' and self.aux != 'f':
            self.aux=input()
            if self.aux == 0:
                break
        if str(self.aux).lower() == 'm':
            MenuTerminal(self.language).__str__('_create_sexM')
        else:
            MenuTerminal(self.language).__str__('_create_sexF')
        self.aux='Gen='+self.aux.upper()

    def create_status(self):   #CREATE STATUS
        self.aux="\n|Status|\n\nLVL=0\nXP=0\nHP=100\nMP=50\nFOR=1\nINT=1\nDEF=1"

    def create_set(self):   #CREATE SET 
        self.aux="\n|EQUIP|\n\nhelmet=None\narmor=None\nlegs=None\nleft-hand=None\nright-hand=None\nAmulet=None"

    def create_bag(self):   #CREATE BAG, BACKPACK
        self.aux="\n|BAG-Itens|\n\n1item=None\n2item=None\n3item=None\n4item=None\n5item=None\n6item=None\n7item=None\n8item=None\n9item=None\n10item=None"

    def reader(self):
        name = str(self.local+str(self.save)+'.txt')
        try:
            with open(name, mode='a',encoding='utf-8') as archive:
                archive.write(self.aux+'\n')
        except:
            MenuTerminal(self.language).__str__('_reader')

