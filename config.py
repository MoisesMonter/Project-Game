from os import path,makedirs
class Config_Menu:
    def __init__(self):
        self.locale = "./save"          #nome da pasta
        self.archive   = "/config.txt"  #nome od arquivo
        self.file = ''                  #responsável arbitrario caso haja  diferença no texto não ocorra erro

    def conf_languages(self):               #vai configurar caso não haja pasta ou caminho, seja criado
        if path.exists(self.locale) == True:
            pass
        else:
            makedirs(self.locale)
            try:     #verifica se ao caminho já existe conteúdo 
                with open(self.locale+self.archive, mode ='r', encoding = 'utf-8') as arc_test:
                    self.atler = arc_test.readlines()
            except:
                with open(self.locale+self.archive, mode='w',encoding='utf-8'):pass       
                with open(self.locale+self.archive, mode='a',encoding='utf-8') as archives:
                    archives.write("Language: 0 (alter it is simple, modify 0 - 1 only ||0-En-US||1-Pt-BR||\n")
                return 0
             

        

    def Reconf_languages(self,boolean):     #responsável por identificar a linguagem e já deixar salvo em um arquivo
        print(boolean)
        try:
            with open(self.locale+self.archive, 'r'):
                if int(boolean) == 1:
                    with open(self.locale+self.archive, mode='w',encoding='utf-8') as archives:
                        archives.write("Language: 1 (alter it is simple, modify 0 - 1 only ||0-En-US||1-Pt-BR||\n")
                        return 1
                elif int(boolean) == 0:

                    with open(self.locale+self.archive, mode='w',encoding='utf-8') as archives:
                        archives.write("Language: 0 (alter it is simple, modify 0 - 1 only ||0-En-US||1-Pt-BR||\n")
                        return 0

        except:
            pass




    def loading_lang(self):        #resposável por interpretar se haja alguma mudança manual no proprio arquivo save
        fix=["Language: 0 (alter it is simple, modify 0 - 1 only ||0-En-US||1-Pt-BR||\n","Language: 1 (alter it is simple, modify 0 - 1 only ||0-En-US||1-Pt-BR||\n"]
        try:
            with open(self.locale+self.archive, mode='r', encoding='utf-8') as archive:
                self.file=archive.readlines()

            if self.file[0] == fix[0] or self.file[0] == fix[1]:
                if self.file[0]==fix[1]:
                    return 1
                else:
                    return 0

            else:
                self.file.insert(0,fix[0])
                self.file.pop(1)
                with open(self.locale+self.archive,mode='w', encoding='utf-8') as archive:
                    for i in self.file:
                        archive.write(i)


        except:
            self.conf_languages()
        del fix
            

'''Config_Menu().conf_languages()
Config_Menu().reconf_languages(True)'''
