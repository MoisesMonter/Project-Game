from Terminal import*
from sys import stdout
class BallonInfo(MenuTerminal):
    def __init__(self,language,info):
        MenuTerminal.__init__(self,language)
        self.info=info
        self.ballon={}

    def __str__(self):
        stdout.write(self.ballon[str(self.language)+str(self.info)])
        

    def Ballon(self):
        self.ballon={
            #END-Menu.py
            #\/NewGame\/#
            '0linkstart':"[1]-Save-and-continue/[2]-Save-back-to-menu?",
            '1linkstart':'"[1]-Salvar-e-continuar/[2]-Salvar-voltar-para-o-Menu?"',

            '0_def_NG_0': "Press the location you will start the new game(0-to back):\n",
            '1_def_NG_0': "Digite o local que deseja iniciar novo jogo(0-para voltar):\n",

            '0_def_Select_0':"Alert! Existing account created! Do you want to delete it?\n",
            '1_def_Select_0':"Alerta! conta existente criada! deseja apagar?\n",
            '0_def_Select_1':"location does not exist.\n",
            '1_def_Select_1':"local não existente.\n",

            '0_def_DelSave_0':"Delete this? (Y/N):\n",
            '1_def_DelSave_0':"Deletar este? (Y/N):\n",
            '0_def_DelSave_1':"Successfully deleted.\n",
            '1_def_DelSave_1':"Deletado com sucesso.\n",
            '0_def_DelSave_2':"canceled\n",
            '1_def_DelSave_2':"Cancelado.\n",
            '0_def_DelSave_3':"We couldn't identify your wish, Try again.\n",
            '1_def_DelSave_3':"Não conseguimos identificar seu desejo, Tente novamente.\n",

            '0_def_New_Verify_Past_0':"archive",
            '1_def_New_Verify_Past_0':"Arquivo",
            '0_def_New_Verify_Past_1':"SALVED",
            '1_def_New_Verify_Past_1':"SALVADO",
            '0_def_New_Verify_Past_2':"EMPTY",
            '1_def_New_Verify_Past_2':"VASIO",            
            #\/LoadGame\/#
            '0_def_Verify_Past_0':"Save Location\n",
            '1_def_Verify_Past_0':"Local Salvo\n",
            '0_def_Verify_Past_1':"folder does not exist.\n",
            '1_def_Verify_Past_1':"pasta não existe.\n",
            '0_def_verify_past_2':'Select(Press[0] to back):\n',
            '1_def_verify_past_2':'Selecione(Digite[0] pra voltar):\n', 

            '0_def_Select_0':'\nSelect Game Save(0 - to back):\n',
            '1_def_Select_0':'\nSelecione o Jogo Salvo(0-volar):\n',
            #\/configuration\/#
            '0_def_select_0':'Available Languages:\nEnglish -0\nPoruguese-1\n',
            '1_def_select_0':'Idiomas Disponíveis:\nInglês -0\nPortugês-1\n',
            '0_def_select_1':'Alter Language?(Any other button to exit):\n',
            '1_def_select_1':'Selecione a Linguagem(Qualquer outro botão para sair):\n',
            '0_def_select_2':'Error... There is no such option\n',
            '1_def_select_2':'Erro... Não existe essa opção\n',       
            #Initial_Menu#
            '0new': "New Game" ,
            '1new': "Novo Jogo" ,
            '0load':"Load Game",
            '1load':"Carregar Jogo",
            '0config':'Configuration',
            '1config':'Configurações',
            '0exit':'Exit',
            '1exit':'Sair',
            '0press':'Press enter to continue',
            '1press':'precione enter para continuar',
        
            #END-Menu.py

            #Create.py
            #\/Create_char
            '0_create_account0':"Loading...\n",
            '1_create_account0':'carregando...\n',
            '0_create_name0':"Type your name[ 6-character's]:\n",
            '1_create_name0':'Digite seu Nome[ 6-caracteres]:\n',
            '0_create_sex0' :'(Male) [ - M - ] || (Female) [ - F -]:\n',
            '1_create_sex0' :'(Homem) [ - M - ] || (Mulher) [ - F -]:\n',
            '0_create_sexM' :'You Choosed Male Genre\n',
            '1_create_sexM' :'Você escolheu Genero Masculino\n',
            '0_create_sexF' :'You Choosed Female Genre\n',
            '1_create_sexF' :'Você escolheu Genero Feminina\n',
            '0_limpesa_global':'<|Filling in Your Account| (press:0 to cancel)>\n',
            '1_limpesa_global':'<|Preenchendo Sua conta| (precione:0 para cancelar)>\n',
            '0_reader':'Error...',
            '1_reader':'Erro...',

            #END-Create.py

            #\/information
            '0_SaveP_0':'LOADING PERSON...\n\n',
            '1_SaveP_0':'CARREGANDO PERSONAGEM... \n\n',
            '0_SaveI_0':'LOADING SET...\n\n',
            '1_SaveI_0':'CARREGANDO SET... \n\n',
            '0_SaveB_0':'LOADING BACKPACK...\n\n',
            '1_SaveB_0':'CARREGANDO MOCHILA... \n\n',

            #Inf_Person.py
            '0_self_info_0':'Save.\n',
            '1_Self_info_0':'Salvo.\n',

            #UP CLASS
            #up
            '0_UP0':"Congratulations! Level UP!\n",
            '1_UP0':"Parabéns! Level UP!\n",
            #Rreturn_Point__
            '0_mana':"No have Mana... for it\n",
            '1_mana':"Nao tem para para isso...\n",
            #SET
            #comparation
            '0_comparation0':'Cannot equip this item...\n',
            '1_comparation0':'Nao pode equipar esse item...\n',
            #recursive
            '0_recursive0':'<select an item from your list (press:(-1) to go back)>:\n',
            '1_recursive0':'<selecione um item de sua lista (precione:(-1) para voltar)>:\n',
            #select_item
            '0_select_item':'\n<Enter which item you want to access (press 0 to go back)>:\n',
            '1_select_item':'\n<Digite que item você deseja acessar(digite 0 para voltar)>:\n',
            '0_select_item0':'There is no item in this position. None position.\n',
            '1_select_item0':'Não há item nessa posição. Posição Vasia.\n',
            '0_select_item1':'This item is quest! (Not Disposable).\n',
            '1_select_item1':'Esse item é de missão! ([1]-excluir/[2]-usar).\n',
            '0_select_item2':'This item is consumable. < Do you want to consume? (Y/N) >:\n',
            '1_select_item2':'Esse item é consumivel. < Deseja Consumir? (Y/N) >:\n',
            '0_select_item3':'Do you want to go back to Backpack? (Y/N):\n',
            '1_select_item3':'Voce deseja voltar a Mochila? (Y/N):\n',
            '0_selct_status0':"This is an equippable item... Let's see its status:\n",
            '1_selct_status0':'Se trata de um item equipavel... Vejamos seus status...',
            '0_selct_status1' :'[1]-Go to Inventory    /[2]-Delete:',
            '1_selct_status1' :'[1]-Ir ao Inventario/[2]-Excluir:',
            #BP_direct
            '0update_status_per_level':"Look! You've earned (1) point to distribute to your stats...\nSelect the stat you want to Level Up (1 - Strength, 2 - Defense, 3 - Intelligence):\n",
            '1update_status_per_level':"Olha só! Você ganhou (1) ponto para distribuir nos teus status...\nSelecione o status que deseja Upar ( 1 - Forca, 2 - Defesa, 3 - Inteligencia):\n",
            '0_BP_direct_0':'There is no space in the Backpack... < Want to see what you have to replace? (Y/N) >:\n',
            '1_BP_direct_0':'Não há espaço na Mochila... < Deseja ver o que tem para substituir? (Y/N)>:\n',
            '0_BP_direct_1':'Be careful, when selecting an item, you will lose it < enter the number (1 to 10) > (or 0 to cancel):\n',
            '1_BP_direct_1':'Cuidado, ao selecionar item, ira perdelo < digite o numero (1 a 10) > (ou 0 para Cancelar):\n',
            '0_BP_direct_2':'Called off',
            '1_BP_direct_2':'Cancelado',
            '0_BP_Dell_0':"Can't Delet it. Mission item!.\n",
            '1_BP_Dell_0':"Nao pode excluir, item de missao!.\n",
            '0_BP_Use_0':"Cannot be consumable, non-consumable item!.\n",
            '1_BP_Use_0':"Nao pode ser consumivel, item não consumivel!.\n",
            #Action_op
            '0_actopt_0':"Select: \n[1]-Act\n[2]-Interact\n[3]-Item-Bag\n[4]-View-Status\n[5]-(Run/Escape)...",
            '1_actopt_0':'Selecione: \n[1]-Agir\n[2]-Interagir\n[3]-Bolsa-de-itens\n[4]-Ver-Status\n[5]-(Corra/Fuja)...',
            '0_actopt_1':"Select:\n[1]-Attack-Physically< fOR/",
            '1_actopt_1':"Selecione:\n [1]-Atacar-Fisicamente< fOR/",
            '0_actopt_2':"Select:\n[2]-Attack-Power< Int/",
            '1_actopt_2':"Selecione:\n [2]-Atacar-Poder< Int/",
            '0_actopt_3':"Cannot use Magic and Witchcraft outside of Hogwarts... due to lack of mana.\n",
            '1_actopt_3':"Não é possível usar Magia e Bruxaria fora de Hogwarts... devido à falta de mana\n",
            '0_actop_4':"You died...",
            '1_actopt_4':"Voce Morreu",
            #'_Point_':'',
            #'_Point_':'',
            '0_Point1':"\tFirst Pilot... Prision!\n\n",
            '1_Point1':"\tPiloto Um... Prisão!\n\n",
            '0_Point_0':"You wake up... you're dirty in a dungeon...\n",
            '1_Point_0':'Você acorda... está sujo em um calabolco...\n',
            '0_Point_1':"You're under arrest... they've chained your hands...\n",
            '1_Point_1':'Você está preso... acorrentaram suas mãos...\n',
            '0_Point_2':'But... \n',
            '1_Point_2':'Porem...\n',
            '0_Point_3':'Seeing ahead there is a bank with keys...\n',
            '1_Point_3':'Vendo logo adiante existe um banco com chaves...\n',
            '0_Point_4':'Yeah... Not every story starts well... but you are the protagonist of this story!\n',
            '1_Point_4':'É... Nem toda história começa bem... mas você é o Protagonista dessa história!\n',
            '0_Point_5':'No matter what, never give up...\n',
            '1_Point_5':'Haja oque houver nunca desista...\n',
            '0_Point_6':'Good Luck...',
            '1_Point_6':'Boa sorte...',
            '0_Point1_6':"you're under arrest... and the guards have left...\n",
            '1_Point1_6':'você está preso... e os guardas Sairam...\n',
            '0_Point2_6':'It cannot and has nothing to attack\n',
            '1_Point2_6':'Não pode e não tem o que atacar\n',
            '0_Point3_6':"Can't Escape, you're trapped...\n",
            '1_Point3_6':'Não pode Fugir, voce esta preso...\n',
            '0_Point4_6':"You find a key, the guards are gone, you're a few meters away in a chair[CHOICE]:\n[1]-You try to reach with your feet.\n[2]-Screams for help. \n[3 ]-Nothing\nType>:\n",
            '1_Point4_6':'Você se depara com uma chave, os guardas sairam, está a poucos metros em uma cadeira[DECIDA]:\n[1]-Você tenta alcancar com os pés.\n[2]-Grita por ajuda.\n[3]-Nada\nDigite>:\n',
            '0_Point5_6':"Nobody listens to you... you're alone\n",
            '1_Point5_6':'Ninguém te escuta... você está só\n',
            '0_Point6_6':'........\n',
            '1_Point6_6':'........\n',
            '0_Point_7':'you got the keys... now check your information in ur inventory.\n',
            '1_Point_7':'você alcançou as chaves... veja agora no seu loot de informacoes.\n',
            '0_Point_8':'Now you need to get out of these handcuffs...\n',
            '1_Point_8':'Agora você precisa sair dessas algemas...\n',
            '0_Point_9':"Congratulation! Mission Conclude!",
            '_Point_9':"Meus Parabéns! Missao Uma concluida!",
            
        }
        
        self.__str__()