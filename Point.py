
from Terminal import *
from info_person import*
import time
class PointHistory(Damage,UP,Set,MenuTerminal):
    def __init__(self,language,**dictinfo):
        Damage.__init__(self,language,**dictinfo)
        UP.__init__(self,language,**dictinfo)
        Set.__init__(self,language,**dictinfo)
        MenuTerminal.__init__(self,language)

        

    def __str__(self,string):
        MenuTerminal(self.language).__str__(string)

    def historypoint(self):
        

        if int(self.dictinfo['Point']) == int(0):
            Mission = True
            self.__str__('_Point1')
            for i in range(0,7,1):
                self.__str__(('_Point_'+str(i)))
                time.sleep(0.0)
                if i == 6 :
                    print(self.dictinfo['Nick'])
                    x=0
                    while x != int(1):
                        time.sleep(0.0)
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
                    

            self.__str__('_Point_7')
            self.dictinfo = self.take('$key_0001')
            self.limpesa_global()
            while Mission != 0:
                
                print("Agora você precisa sair dessas algemas...")
                print(Mission)
                Mission = self.acess_backpack(Mission)
                print(Mission)
                if Mission == False:
                    self.STS('Xp','100')
                    return self.dictinfo
            return self.dictinfo
        elif int(self.dictinfo['Point']) != int(0):
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


