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
            '0_create_name0':"Type your name[ 10-character's]:\n",
            '1_create_name0':'Digite seu Nome[ 10-caracteres]:\n',
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
            #return_Point
            '0_return':"You died...\n",
            '1_return':"Voce Morreu\n",
            '0_Point1':'Return in [',
            '1_Point1':'Retornando em[',

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
            '0_select_item1':'This item is quest! ([1]-Deleted/[2]-using)..\n',
            '1_select_item1':'Esse item é de missão! ([1]-excluir/[2]-usar).\n',
            '0_select_item2':'This item is consumable. < ([1]-Deleted/[2]-Consume). >:\n',
            '1_select_item2':'Esse item é consumivel. ([1]-excluir/[2]-Consumir).:\n',
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
            '0_BP_Use_None':"There's nothing to be used in this space\n",
            '1_BP_Use_None':"Não há nada pra ser usado nesse espaco\n",
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
            '0_Point0':"\t1-First Pilot... Prision!\n\n",
            '1_Point0':"\t1-Piloto Um... Prisão!\n\n",
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
            '0_Point1_inf':"You're handcuffed, you need to find a way out of this...\nYou see keys matching your handcuffs!\nThis key is in the chair... what do you do?\n",
            '1_Point1_inf':"Você está algemado, precisa encontrar um meio de sair dessa...\n VocÊ vê chaves correspondentes a suas algemas!\nEsta chave está na cadeira... o que você faz?\n",
            '0_Pointcant':"You can't move your backpack... your hands are tied",
            '1_Pointcant':'Você não pode mecher na mochila... está com as mãos presas',
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
           
            '0_Point_7_Key':'Now you need to get out of those handcuffs...\n',
            '1_Point_7_Key':"Agora você precisa sair dessas algemas...\n",
            '0_Point8_0':'The hand chains came loose with this key!.. it worked!\n',
            '1_Point8_0':'As correntes das mãos soltaram com essa chave!.. funcionou!\n',
            '0_Point8_1':"Beware... It seems to be Someone... Who is lurking in the Dark\n",
            '1_Point8_1':"Cuidado...Parece ser Alguem... Que está a espreita no Escuro\n",
            '0_Point8_2':"Luckily... You find something on the floor and pick it up...\n",
            '1_Point8_2':"Por sorte... Você encontra algo no chão e pega...\n",
            
            '0_Point_LifeMonster':'LIFE OF MONSTER: ',
            '1_Point_LifeMonster':'VIDA DO MONSTRO: ',
            '0_Point_ForceMonster':'FORCE OF MONSTER: ',
            '1_Point_ForceMonster':'FORCA DO MONSTRO: ',
            
            '0DamageAll':'DAMAGE! CAUSED BY UR ACTION',
            '1DamageAll':'DANO! CAUSADO PELA SUA AÇÃO !',

            '0DamageMonster':"You take damage! ",
            '1DamageMonster':"Você sofre dano! ",

            '0_Point_InteractIMonster_0':'[1]-You try to convince him not to fight\n[2]-You  swear his Mother.[Select]\n',
            '1_Point_InteractIMonster_0':'[1]-Você tenta convencer ele a não lutar\n[2]-Você xinga a Mãe dele.[Selecione]\n',
            '0_Point_InteractIMonster_1':'[1]-You try to convince him not to fight\n[2]-You  swear his Father.[Select]\n',
            '1_Point_InteractIMonster_1':'[1]-Você tenta convencer ele a não lutar\n[2]-Você xinga o Pai dele.[Selecione]\n',
            '0_Point_InteractIMonster_2':'[1]-You try to convince him not to fight\n[2]-You  swear his Sister.[Select]\n',
            '1_Point_InteractIMonster_2':'[1]-Você tenta convencer ele a não lutar\n[2]-Você xinga a Irmã dele.[Selecione]\n',
            '0_Point_InteractIMonster_3':'No more dialogue\n',
            '1_Point_InteractIMonster_3':'Não há mais dialogo\n',

            '0_Point_InteractIMonster_3':'here is no more dialogue... Quiz what? He swears his family all...\n',
            '1_Point_InteractIMonster_3':'Não existe mais dialogo... Quiz oq? Xingou a familia dele todim...\n',            
            '0_Point_InteractIMonster0':"Let's not fight... Fighting is wrong\n",
            '1_Point_InteractIMonster0':'Não vamos Lutar... É errado\n',
            '0_Point_InteractIMonster1':'\nYour mother is so fat that when they went to bury her, the townspeople gathered together gossiping\nThinking that the gravedigger was digging his way to China!\n',
            '1_Point_InteractIMonster1':'Sua Mãe é tão gorda que quando foram enterrar ela, o povo da cidade se reuniu fofocando\nPensando que o coveiro estava cavando pra chegar na china!\n',
            '0_Point_InteractIMonster2':'',
            '1_Point_InteractIMonster2':'Seu pai é tão feio mais tão feio, que quando ele olhou pro espelho, ele não rachou... FEZ FOI CHORAR!\n',
            '0_Point_InteractIMonster3':'I know you... You are Carlos or Eduardo, Famoso... I took that hot sister of yours a lot.\n Sorry for having spoken badly about my father-in-law and mother-in-law\n',
            '1_Point_InteractIMonster3':'Eu conheço você... Você é Carlos o Eduardo, Famoso... Peguei muito aquela tua irmã gostosa.\n Desculpa ter falado mal do meu sogro e da minha sogra\n',
            

            '0_Point_RunIMonster0':"e's distracted... You manage to avoid a deadly confrontation...\n",
            '1_Point_RunIMonster0':'Ele está distraído... Você consegue evitar um confronto Mortal...\n',
            '0_Point_RunIMonster':"Can't run away, he's too pissed to let you escape\n",
            '1_Point_RunIMonster':'Não dá para fugir, ele está Puto de mais para deixar você escapar\n',
             
            '0_broken':'Your item has been broken...\n',
            '1_broken':'Seu item foi quebrado...',
             #sense_damage
            '0Damage':'Bloqued!',
            '1Damage':'Bloqueado',
             #Death_return

            '0_Point1':"\t2-New start...\n",
            '1_Point1':"\t2-Novo recomeço...\n",
            '0_Point1_0':"Okay... you left the cave\n",
            '1_Point1_0':"Okay... você saiu da caverna\n",
            '0_Point1_1':"You got rid of a boring illness that awaited you\n",
            '1_Point1_1':"Desprendeu-se de um mal enfadonho que vos aguardava\n",
            '0_Point1_2':"Leaving outside the castle, you find another key\n",
            '1_Point1_2':"Saindo para fora do castelo, você encontra outra chave\n",
            '0_Point1_3':"the key is in the floor! You take....\n",
            '1_Point1_3':"a chave está no chão! Você pega....\n",
            '0_Point1_4':"Up the Stairs Find two Chests...\nYou go to the chests and take the key from your bag...\n",
            '1_Point1_4':"Subindo as Escadas Encontra dois Baús...\nVocê vai até os baús e pega a chave da sua bolsa...\n",
            '0_Point1_5':"You are about to use they in one of two\n[1]-Mages and Sorceress's Chest\n[2]-Great Knight's Chest...:\n[Choose ONE]:",
            '1_Point1_5':"Você está para usar ela em um dos dois\n[1]-Baú dos Magos e Feiticeiras\n[2]-Baú do Grande Cavaleiro...:\n[Escolha apenas UM]:",
            '0_Point1_6':"You were chosen by the sages to be The Supreme Mage:.\n",
            '1_Point1_6':"Você foi escolhida pelos sábios para ser A Maga suprema:.\n",
            '0_Point1_7':".\nAs it was written on the scrolls... Noble Adventurer\n",
            '1_Point1_7':".\nComo estava escrito nos pergaminhos... Nobre Aventureira\n",
            '0_Point1_8':"You have been chosen by the Strong! to be The Golden Knight!:.",
            '1_Point1_8':"Você foi escolhida pelos Fortes! para ser A Cavaleira Dourada!:.",
            '0_Point1_9':".\nAs it was written on the carvings of the Knights Guild... Noble Adventurer\n",
            '1_Point1_9':".\nComo estava escrito nos entalhes da Guilda dos Cavaleiros... Nobre Aventureira\n",
            '0_Point1_10':"you were chosen by the sages to be THE UNFORTUNATE MAGICIAN!!!:.",
            '1_Point1_10':"Você foi escolhido pelos sábios para ser O MAGO IMPLACÁVEL!!!:.",
            '0_Point1_11':".\nFood..Cold Will heat up...when Bewitching..\nWaving..Your...Hands...The hot dog\n EXPlooodeEEEEEE\nO GALANT Relentless Mage.\n",
            '1_Point1_11':".\nComida.. Fria Vai esquentar... ao Enfeitiçar..\nBalançando as.. Suas... Mãos... O cachorro quente\n EXPlooodiráAÁÁÁÁÁÁ\n Ó Nobre Mago Implacável.\n",
            '0_Point1_12':"You have been chosen by the Strong! to be The Golden Knight!:.",
            '1_Point1_12':"Você foi escolhido pelos Fortes! para ser O Cavaleiro Dourado!:.",
            '0_Point1_13':"As it was written on the carvings of the Knights' Guild... Noble Adventurer\n",
            '1_Point1_13':"Como estava escrito nos entalhes da Guilda dos Cavaleiros... Nobre Aventureiro\n",
            '0_Point1_14':"Now the boss awaits you, fate is in your hands!... Good luck\n",
            '1_Point1_14':"\nAgora o chefe te aguarda, o destino está em suas Mãos!... Boa sorte\n",
            '0_Point1END':"You have \033[1;31m powerful \033[0;32m items!! \033[0;0m\n Now you can face the Final Boss!\n",
            '1_Point1END':"Você tem \033[1;31m itens \033[0;32m poderosos!! \033[0;0m\n Agora pode enfrentar o Chefe Final!\n",
            
            '0_Boss1':'\t3-Last Visions of the End of the World\n',
            '1_Boss1':"\t3-Ultimas Visões do Fim do Mundo\n",
            '0_Boss1_0':"The Final Boss Feels a Mighty Presence...\n",
            '1_Boss1_0':"O chefão Final Sente uma presença Poderosa...\n",
            '0_Boss1_1':"He sees you, the powerful presence is you!\n",
            '1_Boss1_1':"Ele te vê, a presença poderosa é você!\n",
            '0_Boss1_2':"He's slowly walking towards you...\n",
            '1_Boss1_2':"Ele vem andando Lentamente até você...\n",
            '0_Boss1_3':"He launches a powerful bolt, you try to defend yourself...\n",
            '1_Boss1_3':"Ele lança um raio poderoso, você tenta se defender...\n",
            '0_Boss1_4':"Your shield protection is destroyed...\n",
            '1_Boss1_4':"\033[1;31m Sua proteção escudo é destruída...\033[0;0m\n",
            '0_Boss1_5':"BOSS: Do you think you'll last with these items for a long time?\n",
            '1_Boss1_5':"BOSS: você acha que você vai durar com esses itens por muito tempo?\n",
            '0_Boss1_6':"BOSS: Don't make me laugh, this isn't a roleplaying game where you only depend on good items...\n",
            '1_Boss1_6':"BOSS: Não Me faça rir, isso não é um Jogo de RPG que você só depende de itens bons...\n",
            '0_Boss1_7':"BOSS: I'll show you HELL!\n",
            '1_Boss1_7':"BOSS:Vou mostrar pra você o INFERNO!\n",
            '0_Boss1_cont0':"\033[1;31m He tore your helmet apart!\033[0;0m\n",
            '1_Boss1_cont0':"\033[1;31m Ele dilacerou seu capacete!\033[0;0m\n",
            '0_Boss1_cont1':"\033[1;31m He tore your armor apart!\033[0;0m\n",
            '1_Boss1_cont1':"\033[1;31m Ele dilacerou sua armadura!\033[0;0m\n",
            '0_Boss1_cont2':"\033[1;31m Ele dilacerou suas Calças!\033[0;0m\n",
            '1_Boss1_cont2':"\033[1;31m Ele dilacerou suas Calças!\033[0;0m\n",
            '0_Boss1_cont3':"033[1;31m He lacerated your Sword... You lost your Set of your fate!\033[0;0m\n",
            '1_Boss1_cont3':"\033[1;31m Ele dilacerou sua Espada... Você perdeu seu Set do teu destino!\033[0;0m\n",
            '0_Boss1_int0':"You interact with THE BOSS:\n[1]-speaks of Unite with Him\n[2]-Curses His Mother:\n",
            '1_Boss1_int0':"Você interage com O BOSS:\n[1]-fala em Unir-se a Ele\n[2]-Xinga Mãe dele:\n",
            '0_Boss1_int1':"You interact with THE BOSS:\n[1]-speaks of Unite with Him\n[2]-Curses His Father:\n",
            '1_Boss1_int1':"Você interage com O BOSS:\n[1]-fala em Unir-se a Ele\n[2]-Xinga O Pai dele:\n",
            '0_Boss1_int2':"You interact with THE BOSS:\n[1]-speaks of Unite with Him\n[2]-Swears His sister:\n",
            '1_Boss1_int2':"Você interage com O BOSS:\n[1]-fala em Unir-se a Ele\n[2]-Xinga Irmã dele:\n",
            '0_Boss1_intNone':"He'll kill you easier...easier Why was he cursing the boss?\n",
            '1_Boss1_intNone':"Ele vai te matar mais facil...facil Praq foi xingar o boss?\n",
            '0_Boss1_intRecuse':"I refuse to be an ally of such a weak being!!\n",
            '1_Boss1_intRescuse':"Me recuso ser aliado de um ser tão fraco!!\n",
            '0_Boss1_puto1':"\n[You]:Your mother is fat!!!!\n[Boss]: You'll pay for it with your life",
            '1_Boss1_puto1':"\n[Você]:Sua Mae é gordaaaa!!!!\n[Boss]: Vai pagar Por com Sua vida",
            '0_Boss1_puto2':"\n[You]:Your father is Corno!!!!\n[Boss]: Ahhhhh killing you WILL BE LITTLE!!!",
            '1_Boss1_puto2':"\n[Você]:Seu pai é Corno!!!!\n[Boss]: Ahhhhh te matar VAI SER POUCO!!!",
            '0_Boss1_puto3':"\n[You]:After I defeat you, I want your sister's Contact!!!!!\n[Boss]: My consecrated.... IT'S FUCKED....!!!",
            '1_Boss1_puto3':"\n[Você]:Depois de eu te derrotar quero Contato de sua irmã!!!!!\n[Boss]: Meu consagrado.... SE TÁ FUDIDO....!!!",
            
            '0_Boss1_End':"Congratulations!!! You killed the big boss, now the world is free from his terrible clutches!!\nThank you!!! Thank you!!!!",
            '1_Boss1_End':"Parabéns!!! Você Matou o chefão, agora o mundo esta livre de suas terriveis garras!!\nObrigado!!! Obrigado!!!!",




        }
        
        self.__str__()