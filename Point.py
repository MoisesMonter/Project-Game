
from Terminal import *

from info_person import*
import time
class PointHistory(Damage,UP,Set,MenuTerminal):

    def __init__(self,language,local_save,**dictinfo):
        Damage.__init__(self,language,local_save,**dictinfo)
        UP.__init__(self,language,local_save,**dictinfo)
        Set.__init__(self,language,local_save,**dictinfo)
        MenuTerminal.__init__(self,language)

        

    def __str__(self,string):
        MenuTerminal(self.language).__str__(string)

    def historypoint(self):
        RED   = "\033[1;31m"  
        BLUE  = "\033[1;34m"
        CYAN  = "\033[1;36m"
        GREEN = "\033[0;32m"
        RESET = "\033[0;0m"
        BOLD    = "\033[;1m"
        REVERSE = "\033[0;0m"
        

        if int(self.dictinfo['Point']) == int(0):
            Mission = bool
            self.__str__('_Point0')
            for i in range(0,7,1):
                self.__str__(('_Point_'+str(i)))
                time.sleep(2.0)
                if i == 6 :
                    print(self.dictinfo['Nick'])
                    x=0
                    input("press_ENTER_to_continue..")
                    self.limpesa_global()
                    
                    while x != int(1):
                        time.sleep(0.0)
                        self.__str__('_Point1_inf')
                        y = self.Action_Option(Mission)
                        if y ==-1 or y ==0 or y ==1:
                            self.__str__(('_Point1_'+str(i)))
                            self.__str__(('_Point2_'+str(i)))
                        elif y == 5:
                            self.__str__(('_Point3_'+str(i)))
                        elif y == 2:
                            self.__str__(('_Point4_'+str(i)))
                            x=int(input())
                            if x == 1:
                                break
                            if x == 2:
                                self.__str__(('_Point5_'+str(i)))
                            if x == 3:
                                self.__str__(('_Point6_'+str(i)))
                        elif y == 3:
                            self.__str__('_Pointcant')
                        input("press_ENTER_to_continue..")
                        self.limpesa_global()
                    

            self.__str__('_Point_7')
            self.dictinfo = self.take('$key_0001')
            input("press_ENTER_to_continue..")
            self.limpesa_global()
            while Mission != False:
                self.__str__('_Point_7_Key')
                Mission = True
                Mission = self.acess_backpack(Mission)
                input("press_ENTER_to_continue..")
                self.limpesa_global()
                if Mission == False:
                    break
            for i in range (0,3,1):
                self.__str__(('_Point8_'+str(i)))
                time.sleep(1)
            input("press_ENTER_to_continue..")
            self.limpesa_global()
            self.dictinfo = self.take('6_right0')
            self.limpesa_global()
            Life_Monster=int(30)
            contint = 0
            Power_Monster=int(10)
            damage=0
            while Life_Monster!=0:
                if Life_Monster <= 0:
                    break
                print("HP: ",self.dictinfo['Hp'],'\nMP: ',self.dictinfo['Mp'],'\n\n')
                self.__str__('_Point_LifeMonster');print(Life_Monster)
                self.__str__('_Point_ForceMonster');print(Power_Monster,'\n\n')
                action = self.Action_Option(Mission) # pucha informações que o personagem deve usar
                
                if action == int(self.dictinfo['For']) or int(action == self.dictinfo['Int']):
                    damage = action #vai no dano magico e recolhe informações de magia e se pode usar magia
                    if damage >=1:
                        self.__str__('DamageAll')
                        print(' :'+RED+str(damage)+REVERSE+"!")
                        Life_Monster = int(Life_Monster) - int(damage)
                    elif damage == 0:
                        print ("MISS.....")
                    damage = self.sense_damage(Power_Monster)
                    self.__str__('DamageMonster');print(RED,damage,REVERSE,"!")
                
                if action == 2:
                    
                    if contint <=2:
                        self.__str__(('_Point_InteractIMonster_'+str(contint)))
                        action=int(input())

                        if action == 1:
                            self.__str__(('_Point_InteractIMonster'+str(contint)))
                        else:
                            if contint <=2:
                                contint= contint+1
                            self.__str__(('_Point_InteractIMonster'+str(contint)))
                            Power_Monster = Power_Monster*2
                    else:
                        self.__str__(('_Point_InteractIMonster_'+str(contint)))
            
                if action == 3:
                    pass
                elif action == 4:
                    pass
                
                elif action == 5:
                    if contint == 0:
                        self.__str__('_Point_RunIMonster'+str(contint))
                    else:
                        self.__str__('_Point_RunIMonster')
                input("press_ENTER_to_continue..")
                self.limpesa_global()

            self.__str__('_broken')    
            self.broken_item('right-hand')
            
            if Life_Monster <=0:    
                self.dictinfo =self.STS('Xp','100')
            else:
                pass
            input("press_ENTER_to_continue..")
            self.Next_Point()
            return self.dictinfo

        elif int (self.dictinfo['Point']) == int (1):
            self.limpesa_global()
            Mission = False
            self.__str__("_Point1")
            for i in range (0,4,1):
                time.sleep(1.5)
                self.__str__(('_Point1_'+str(i)))

            input("press_ENTER_to_continue..")
            self.limpesa_global()
            Mission = True
            self.dictinfo = self.take('$key_0002')
            select=int(0)
            while Mission != False:
                self.__str__('_Point1_4')
                Mission = True
                Mission = self.acess_backpack(Mission)
                input("press_ENTER_to_continue..")
                self.limpesa_global()
                if Mission == False:
                    self.__str__('_Point1_5')
                    select = int(input())
                    break
                if Mission != bool:
                    Mission = True

            if select == 1:
                if self.dictinfo['Gen']=='M':
                    self.dictinfo = self.take('8_helm9')
                    self.dictinfo = self.take('5_armr9')
                    self.dictinfo = self.take('2_legs9')
                    self.dictinfo = self.take('4_left8')
                    self.dictinfo = self.take('6_right6')
                else:
                    self.dictinfo = self.take('8_helm8')
                    self.dictinfo = self.take('5_armr8')
                    self.dictinfo = self.take('2_legs8')
                    self.dictinfo = self.take('4_left9')
                    self.dictinfo = self.take('6_right9')

            elif select == 2:
                self.dictinfo = self.take('8_helm10')
                self.dictinfo = self.take('5_armr10')
                self.dictinfo = self.take('2_legs10')
                self.dictinfo = self.take('4_left10')
                self.dictinfo = self.take('6_right10')

            if self.dictinfo['Gen'] =='F':
                if select ==1:
                    time.sleep(1.5)
                    self.__str__('_Point1_6');time.sleep(1.5);print(BLUE,self.dictinfo['Nick'],RESET,end='');time.sleep(1.5);self.__str__('_Point1_7');time.sleep(1.5)
                else:
                    self.__str__('_Point1_8');time.sleep(1.5);print(BLUE,self.dictinfo['Nick'],RESET,end='');time.sleep(1.5);self.__str__('_Point1_9');time.sleep(1.5)
            if self.dictinfo['Gen'] =='M':
                if select ==1:
                    self.__str__('_Point1_10');time.sleep(1.5);print(BLUE,self.dictinfo['Nick'],RESET,end='');time.sleep(1.5);self.__str__('_Point1_11');time.sleep(1.5)
                else:
                    self.__str__('_Point1_12');time.sleep(1.5);print(BLUE,self.dictinfo['Nick'],RESET,end='');time.sleep(1.5);self.__str__('_Point1_13');time.sleep(1.5)
            time.sleep(1.5)
            self.__str__('_Point1_14')
            time.sleep(1.5)
            self.__str__('_Point1END')
            
            input("press_ENTER_to_continue..")
            self.limpesa_global()
            self.Next_Point()
            return self.dictinfo

        elif int(self.dictinfo['Point'])== int(2):
            self.__str__('_Boss1')
            for st in range(0,8,1):
                time.sleep(1.5)
                self.__str__(('_Boss1_'+str(st)))
                if st == 5:
                    self.broken_item('left-hand')
            input("press_ENTER_to_Continue")
            Life_Monster=int(100)
            contint = 0
            contitens = 0
            Power_Monster=int(60)
            damage=0
            while Life_Monster!=0:
                if Life_Monster <= 0:
                    break
                print("HP: ",self.dictinfo['Hp'],'\nMP: ',self.dictinfo['Mp'],'\n\n')
                self.__str__('_Point_LifeMonster');print(Life_Monster)
                self.__str__('_Point_ForceMonster');print(Power_Monster,'\n\n')
                action = self.Action_Option(0) # pucha informações que o personagem deve usar
                
                if action == int(self.dictinfo['For']) or int(action == self.dictinfo['Int']):
                    damage = action #vai no dano magico e recolhe informações de magia e se pode usar magia
                    if damage >=1:
                        self.__str__('DamageAll')
                        print(' :'+RED+str(damage)+REVERSE+"!")
                        Life_Monster = int(Life_Monster) - int(damage)
                    elif damage == 0:
                        print ("MISS.....")
                    damage = self.sense_damage(Power_Monster)
                    if contitens ==0:
                        if self.dictinfo['helmet'] != 'None':
                            self.broken_item('helmet')
                            
                            self.__str__('_Boss1_cont0')
                    if contitens ==1:
                        if self.dictinfo['armor'] != 'None':
                            self.broken_item('armor')
                            
                            self.__str__('_Boss1_cont1')         
                    if contitens ==2:
                        if self.dictinfo['legs'] != 'None':
                            self.broken_item('legs')
                
                            self.__str__('_Boss1_cont2')  
                    if contitens ==3:
                        if self.dictinfo['right-hand'] != 'None':
                            self.broken_item('right-hand')
                            self.__str__('_Boss1_cont3')  
                    contitens+=contitens+1
                    self.__str__('DamageMonster');print(RED,damage,REVERSE,"!")
                
                if action == 2:
                    
                    if contint <=2:
                        self.__str__(('_Boss1_int'+str(contint)))
                        action=int(input())
                        if action == 1:
                            self.__str__("_Boss1_intRescuse")
                        else:
                            contint= contint+1
                            self.__str__((str("_Boss1_puto")+str(contint)))
                            Power_Monster= Power_Monster*2

                    else:   
                        self.__str__('_Boss1_intNone')

            
                if action == 3:
                    pass
                elif action == 4:
                    pass
                
                elif action == 5:
                    if contint == 0:
                        self.__str__('_Point_RunIMonster'+str(contint))
                    else:
                        self.__str__('_Point_RunIMonster')
                input("press_ENTER_to_continue..")
                self.limpesa_global()

            self.__str__('_broken')    
            self.broken_item('right-hand')
            
            if Life_Monster <=0:    
                self.dictinfo =self.STS('Xp','100')
            else:
                pass
            self.__str__("_Boss1_End")
            input("press_ENTER_to_continue..")
            self.Next_Point()
            return self.dictinfo

        elif int(self.dictinfo['Point']) >= int(3):
            print("Parabens voce zerou o jogo")
            time.sleep(3)
            print("CREDITOS: Programador...-> MOISES ALEXANDRE MONTEIRO ARAUJO.")
            time.sleep(3)
            print("CREDITOS: Roterista...-> MOISES ALEXANDRE MONTEIRO ARAUJO.")
            time.sleep(3)
            print("CREDITOS: Tradutor...-> MOISES ALEXANDRE MONTEIRO ARAUJO.")
            time.sleep(3)
            print("CREDITOS: Auxiliar...-> MOISES ALEXANDRE MONTEIRO ARAUJO.")
            time.sleep(3)
            print("CREDITOS: Estilista...-> MOISES ALEXANDRE MONTEIRO ARAUJO.")
                
            return self.dictinfo

