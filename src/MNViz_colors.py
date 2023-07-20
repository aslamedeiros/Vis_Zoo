# Paletas de cores
## ORDEM
cores_ordem = {   # p.s.: Caudata is an error and should be removed
    'Squamata': '#BF4417',
    'Testudines': '#D9CB0B', 
    'Crocodylia': '#284021'   
}

cores_infraordem = {
    'Nan':'#000000',
    'Ascacidae':'#fece5f',
    'Anomura':'#007961',
    'Achelata':'#7a2c39',
    'Axiidea':'#b67262',
    'Brachyura':'#ee4454',
    'Caridea':'#3330b7',
    'Gebiidea':'#d867be',
    'Stenopodidea':'#b8e450',
    'Astacidea':'#a0a3fd',
    'Polychelida':'#deae9e',
    'Grapsoidea':'#58b5e1',  # removed as asked by Cristiana Serejo (It should be reported as Brachyura)
    'Xanthoidea':'#8b9388'
}

cores_familia_crustacea = {
    # known errors are marked in black
    'Nan':'#000000',
    # infraorder: Ascacidea - #fece5f
    'Cambaridae':'#fece5f',
    'Enoplometopidae':'#fece5f', 
    'Nephropidae':'#fece5f',    
    'Parastacidae':'#fece5f', 
        # p.s.: a cris classificou, mas não são decapoda.
        #'Cambaridae'
        #'Enoplometopidae'
        #'Parastacidae'
    # infraorder: Anomura  - #007961 (obs: Lithodidae e Coenobitidae não foram classificadas pela Cris, mas são decapoda)
    'Aeglidae':'#007961', 
    'Albuneidae':'#007961',
    'Blepharipodidae':'#007961', 
    'Chirostylidae':'#007961', 
    'Coenobitidae':'#007961',
    'Diogenidae':'#007961', 
    'Galatheidae':'#007961', 
    'Hippidae':'#007961', 
    'Lithodidae':'#007961', 
    'Munididae':'#007961', 
    'Munidopsidae':'#007961',
    'Paguridae':'#007961', 
    'Parapaguridae':'#007961', 
    'Porcellanidae':'#007961',
    
    # infraorder: Achelata - #7a2c39
    'Palinuridae':'#7a2c39',
    'Scyllaridae':'#7a2c39',

    # infraorder: Axiidea - #b67262
    'Axiidae':'#b67262',
    'Callianassidae':'#b67262',
    'Ctenochelidae':'#b67262',
    'Micheleidae':'#b67262',

    # infraorder: Brachyura - #ee4454
    'Aethridae':'#ee4454', 
    'Atelecyclidae':'#ee4454',
    'Bythograeidae':'#ee4454', 
    'Calappidae':'#ee4454',
    'Cancridae':'#ee4454', 
    'Carpiliidae':'#ee4454', 
    'Chasmocarcinidae':'#ee4454', 
    'Cryptochiridae':'#ee4454',
    'Cyclodorippidae':'#ee4454', 
    'Dairidae':'#ee4454', 
    'Domeciidae':'#ee4454', 
    'Dorippidae':'#ee4454', 
    'Dromiidae':'#ee4454', 
    'Epialtidae':'#ee4454', 
    'Eriphiidae':'#ee4454', 
    'Ethusidae':'#ee4454',
    'Euryplacidae':'#ee4454', 
    'Gecarcinidae':'#ee4454', 
    'Geryonidae':'#ee4454', 
    'Goneplacidae':'#ee4454',
    'Grapsidae':'#ee4454',
    'Homolidae':'#ee4454', 
    'Homolodromiidae':'#ee4454', 
    'Hymenosomatidae':'#ee4454', 
    'Inachidae':'#ee4454', 
    'Inachoididae':'#ee4454', 
    'Leucosiidae':'#ee4454', 
    'Majidae':'#ee4454', 
    'Menippidae':'#ee4454',
    'Mictyridae':'#ee4454',
    'Mithracidae':'#ee4454', 
    'Ocypodidae':'#ee4454',
    'Ovalipidae':'#ee4454', 
    'Palicidae':'#ee4454', 
    'Panopeidae':'#ee4454', 
    'Parthenopidae':'#ee4454',
    'Percnidae':'#ee4454',
    'Pilumnidae':'#ee4454', 
    'Pilumnoididae':'#ee4454',
    'Pinnotheridae':'#ee4454', 
    'Plagusiidae':'#ee4454', 
    'Platyxanthidae':'#ee4454',
    'Polybiidae':'#ee4454', 
    'Portunidae':'#ee4454', 
    'Pseudorhombilidae':'#ee4454', 
    'Pseudothelphusidae':'#ee4454', 
    'Raninidae':'#ee4454', 
    'Sesarmidae':'#ee4454', 
    'Symethidae':'#ee4454',
    'Trichodactylidae':'#ee4454', 
    'Trichopeltariidae':'#ee4454', 
    'Ucididae':'#ee4454', 
    'Varunidae':'#ee4454', 
    'Xanthidae':'#ee4454', 

    # infraorder: Caridea - #3330b7
    'Acanthephyridae':'#3330b7', 
    'Alpheidae':'#3330b7',
    'Anchistioididae':'#3330b7',
    'Atyidae':'#3330b7', 
    'Bathypalaemonellidae':'#3330b7', 
    'Crangonidae':'#3330b7', 
    'Disciadidae':'#3330b7', 
    'Glyphocrangonidae':'#3330b7',
    'Hippolytidae':'#3330b7', 
    'Lysmatidae':'#3330b7',
    'Nematocarcinidae':'#3330b7', 
    'Ogyrididae':'#3330b7', 
    'Oplophoridae':'#3330b7', 
    'Palaemonidae':'#3330b7',
    'Pandalidae':'#3330b7', 
    'Pasiphaeidae':'#3330b7',
    'Processidae':'#3330b7', 
    'Pseudochelidae':'#3330b7', 
    'Rhynchocinetidae':'#3330b7', 

    
    # infraorder: Polychelida - #deae9e
    'Polychelidae':'#a0a3fd', # aloquei a cor do grupo Astacidea, que não está mais sendo usada (para diferenciar do outro marrom)
    
    # infraorder: Stenopodídea - b8e450
    'Stenopodidae':'#b8e450',

    # infraorder: Gebiidea - #d867be
    'Upogebiidae':'#d867be',

    # OBS: a partir daqui, não foram classificados pela Cris
    # infraorder: Astacidea
        #'Cambaridae':'#a0a3fd',    
        #'Enoplometopidae':'#a0a3fd', 
        #'Nephropidae':'#a0a3fd', 
        #'Parastacidae':'#a0a3fd', 
    
    
    # infraorder: Grapsoidea
    # 'Grapsidae': '#d867be',
}

cores_familia_reptiles = {
    # known errors treatment
#     '#n/d':'#000000',
#     'nan':'#000000',
    # grupo 1: Crocodylia
    'Alligatoridae':'#142611',
    # grupo 2: Testudines
    'Cheloniidae':'#bafd62',
    'Chelydridae':'#9feb3f',
    'Dermochelyidae':'#85d907',
    'Emydidae':'#6cc700',
    'Geoemydidae':'#52b700',
    'Kinosternidae':'#35a600',
    'Testudinidae':'#0b9700',
    'Trionychidae':'#008800',
    'Chelidae':'#006400',
    'Podocnemididae':'#004100',
    # grupo 4: Amphisbaenia - Amphisbaenia
    'Amphisbaenidae':'#F2CB07',
    # grupo 5: Sauria - Iguania
    'Dactyloidae':'#f8dcf9',
    'Agamidae':'#ebc5ed',
    'Chamaeleonidae':'#ddafe2',
    'Iguanidae':'#ce9ad6',
    'Hoplocercidae':'#bf86cc',
    'Leiosauridae':'#af73c2',
    'Polychrotidae':'#a160b8', 
    'Liolaemidae':'#924fae',
    'Phrynosomatidae':'#833fa4',
    'Tropiduridae':'#803da1',
    # grupo 6: Sauria - Scleroglossa
    'Scincidae':'#c9fff9',
    'Anguidae':'#b3eff2',
    'Lacertidae':'#9cdcea',
    'Gymnophthalmidae':'#83c9e2',
    'Helodermatidae':'#68b7da',
    'Xantusiidae':'#4aa6d2',
    'Gekkonidae':'#2096ca',
    'Phyllodactylidae':'#0087c1',
    'Sphaerodactylidae':'#0079b7',
    'Varanidae':'#226ca2',
    'Teiidae':'#005e98',
    # grupo 7: Serpentes - Scolecophidia
    'Anomalepididae':'#bfbfbf',
    'Leptotyphlopidae':'#8a8a8a',
    'Typhlopidae':'#595959', 
    # grupo 8: Alethinophidia
    'Dipsadidae':'#ffce9f',
    'Natricidae':'#ffb683',
    'Homalopsidae':'#ff9f69',
    'Colubridae':'#ff8851',
    'Lamprophiidae':'#f5723b',
    'Pythonidae':'#e75b25',
    'Boidae':'#d9430d', 
    'Aniliidae':'#cb2800',
    'Loxocemidae':'#bc0000',
    'Elapidae':'#c62f00',
    'Tropidophiidae':'#b41b00',
    'Xenopeltidae':'#a40300',
    'Viperidae':'#930000'
}

### POLYCHAETE
## ORDER
# p.s.: o agrupamento é feito por famílias (ordem daquelas famílias deve assumir certa cor)
cores_ordem_polychaete = {
    'Oweniida_incertae_sedis': '#548235',
    'Amphinomida': '#ffd966',
    'Capitellida': '#f4b084',
    'Chaetopteriformia_incertae_sedis': '#7b7b7b',
    'Cirratulida': '#9bc2e6',
    'Eunicida': '#00b0f0',
    'Orbiniida': '#ffc000',
    'Phyllodocida': '#2f75b5',
    'Sabellida': '#7030a0',
    'Sedentaria_Order_incertae_sedis': '#c00000',
    'Spionida': '#c65911',
    'Sternaspida': '#333f4f',
    'Terebeliida': '#7b7b7b',
    'Terebellida': '#7b7b7b',
    'Non-identified': '#000000'}


cores_ordem_polychaete_velho = {
    'Spionida':'#41A681',   # verde
    'Sabellida':'#7ACAAB',  # verde claro
    'Canalipalpata':'#78a1a1',  # azul
    'Amphinomida':'#8ABFB0',  # azul claro
    'Eunicida':'#A66C4B', # marrom claro
    'Phyllodocida':'#732C02', # marrom2
    'Terebellida':'#ed845e', # laranja claro1
    'Scolecida':'#D94B18', # laranja 2
    'Sedentaria_order_incertae_sedis':'#D94B18',  # OBS: não manter junto com scolecida
    'Nan':'#0D0D0D',  # preto ### original np.nan
    'Non-identified':'#0D0D0D',  # preto
    'Order_incertae_sedis':'#0D0D0D',  # preto
    
    # ordens não citadas na planilha:
    'Sipuncula':'#D9C2AD', # bege
    'Crassiclitellata':'#FFB27C', # cor de pele clara
    'Aspidosiphonida':'#F29877',  # cor de pele
    
}


## Family
cores_familia_polychaete = {
    'Magelonidae': '#548235',
    'Oweniidae': '#548235',
    'Amphinomidae': '#ffd966',
    'Euphrosinidae': '#ffd966',
    'Opheliidae': '#f4b084',
    'Capitellidae': '#f4b084',
    'Chaetopteridae': '#7b7b7b',
    'Apistobranchidae': '#7b7b7b',
    'Cirratulidae': '#9bc2e6',
    'Flabelligeridae': '#9bc2e6',
    'Lumbrineridae': '#00b0f0',
    'Dorvilleidae': '#00b0f0',
    'Oenonidae': '#00b0f0',
    'Eunicidae': '#00b0f0',
    'Onuphidae': '#00b0f0',
    'Orbiniidae': '#ffc000',
    'Syllidae': '#2f75b5',
    'Typhloscolecidae': '#2f75b5',
    'Aphroditidae': '#2f75b5',
    'Acoetidae': '#2f75b5',
    'Alciopidae': '#2f75b5', ###
    'Chrysopetalidae': '#2f75b5',
    'Eulepethidae': '#2f75b5',
    'Lopadorrhynchidae': '#2f75b5',
    'Polynoidae': '#2f75b5',
    'Nereididae': '#2f75b5',
    'Nephtyidae': '#2f75b5',
    'Glyceridae': '#2f75b5',
    'Goniadidae': '#2f75b5',
    'Tomopteridae': '#2f75b5',
    'Pilargidae': '#2f75b5',
    'Lacydoniidae': '#2f75b5',
    'Pontodoridae': '#2f75b5',
    'Sigalionidae': '#2f75b5',
    'Hesionidae': '#2f75b5',
    'Sphaerodoridae': '#2f75b5',
    'Phyllodocidae': '#2f75b5',
    'Iospilidae': '#2f75b5',
    'Serpulidae': '#7030a0',
    'Sabellidae': '#7030a0',
    'Cossuridae': '#c00000',
    'Spionidae': '#c65911',
    'Trochochaetidae': '#c65911',
    'Poecilochaetidae': '#c65911',
    'Longosomatidae': '#c65911',
    'Sabellariidae': '#c65911',
    'Sternaspidae': '#333f4f',
    'Paraonidae': '#333f4f',
    'Maldanidae': '#7b7b7b',
    'Ampharetidae': '#7b7b7b',
    'Pectinariidae': '#7b7b7b',
    'Trichobranchidae': '#7b7b7b',
    'Terebellidae': '#7b7b7b',
    'Arenicolidae': '#7b7b7b',
    'Scalibregmatidae': '#7b7b7b',
    'Non-identified': '#000000'
    }
cores_familia_polychaete_velho =  {
    # grupo 1 - Order_incertae_sedis
    'Magelonidae':'#238762',    # verde escuro 
    'Oweniidae':'#3CA67F',      # verde (centroide)  
    'Chaetopteridae':'#77c8a5', # verde
    'Amphinomidae':'#bbebd3',   # verde claro
    'Euphrosinidae':'#cce8cc',
    # grupo 2 - Eunicida
    'Lumbrineridae':'#e7e5df',  # azul claro 1
    'Dorvilleidae':'#b2c0d0',   # azul claro2
    'Oenonidae':'#7A9FBF',      # azul (centroide)
    'Eunicidae':'#3c81ae',      # azul
    'Onuphidae':'#00669a',      # azul escuro
    # grupo 3 (1) - Phyllodocida
    'Syllidae':'#FFE5CA', 
    'Typhloscolecidae':'#FFCEAC', 
    'Aphroditidae':'#FFB891', 
    'Acoetidae':'#FFBD84', 
    'Chrysopetalidae':'#FFAA74', 
    'Eulepethidae':'#FFA178',
    'Lopadorrhynchidae':'#FF9760',  # laranja (centroide)
    'Polynoidae':'#F38C60',
    'Nereididae':'#F18E56',
    # grupo 3 (2) - Phyllodocida
    'Nephtyidae':'#FF814B',
    'Glyceridae':'#E6774B',         # laranja 2 (centroide)
    'Goniadidae':'#FC6B36',
    'Tomopteridae':'#D96236',
    'Pilargidae':"#EB5824",
    'Lacydoniidae':'#D94814',
    'Iospilidae':'#C04A21',
    'Pontodoridae':'#C83B03',
    'Sigalionidae':'#BF381B',
    'Hesionidae':'#B23209',
    'Sphaerodoridae':'#B73000',
    'Phyllodocidae':'#8B0000',
    # grupo 4 - Sabellida
    'Serpulidae':'#bf0753',
    'Sabellidae':'#f17997', # cor de pele (centroide)
    #'Iospilidae':'#e8a287',
    # grupo 5 - Spionida
    'Spionidae':'#c9d5ff', 
    'Trochochaetidae': '#b8b4fe',
    'Poecilochaetidae': '#a78ff6',
    'Apistobranchidae': '#9762e4',
    'Longosomatidae': '#7a30c8',
    # grupo 6 - Terebeliida
    'Ampharetidae':'#821f48',  #d27666
    'Pectinariidae':'#af4c70',  #b48061 # marrom 1 (centroide),
    'Trichobranchidae':'#c66485',  #a66c4b
    'Terebellidae':'#dd7c9a',  #975b39
    'Cirratulidae':'#f594b0',  #874c2c
    'Flabelligeridae':'#ffacc6',  #774124  
    'Sternaspidae':'#ffc4dc',  #683720  # vermelho (nova centroide)
    # grupo 7 - Sedentaria_Order_incertae_sedis
    # cor sobrando: '#eebd93'
    'Orbiniidae':'#dfa47a',
    'Opheliidae':'#d28d60',
    'Capitellidae':'#c37746',
    'Arenicolidae':'#b4622f',
    'Cossuridae':'#a3501d',
    'Scalibregmatidae':'#92420e',
    'Paraonidae':'#823606',
    'Maldanidae':'#732c02', # marrom 2 (centroide)

    # erros conhecidos
    #'NaN':'#0D0D0D',  # preto
    'Non-identified': '#0D0D0D' 
}

### ANNELIDA
cores_ordem_annelida = {'Oweniida_incertae_sedis': '#e2efda',
 'Amphinomida': '#92d050',
 'Chaetopteriformia_incertae_sedis': '#548235',
 'Protodrilida': '#ddebf7',
 'Eunicida': '#00b0f0',
 'Phyllodocida': '#2f75b5',
 'Sabellida': '#fff2cc',
 'Sedentaria_Order_incertae_sedis': '#ffd966',
 'Spionida': '#ffc000',
 'Sternaspida': '#bf8f00',
 #'Terebeliida': '#806000',
 'Terebellida': '#806000',
 'Capitellida': '#fce4d6',
 'Cirratulida': '#f4b084',
 'Orbiniida': '#ed7d31',
 'Oligochaeta': '#c65911',
 'Sipuncula ': '#833c0c',
 'Non-identified': '#000000'}

cores_familia_annelida = {'Magelonidae': '#e2efda',
 'Oweniidae': '#e2efda',
 'Amphinomidae': '#92d050',
 'Euphrosinidae': '#92d050',
 'Chaetopteridae': '#548235',
 'Apistobranchidae': '#548235',
 'Saccocirridae': '#ddebf7',
 'Lumbrineridae': '#00b0f0',
 'Dorvilleidae': '#00b0f0',
 'Oenonidae': '#00b0f0',
 'Eunicidae': '#00b0f0',
 'Onuphidae': '#00b0f0',
 'Syllidae': '#2f75b5',
 'Typhloscolecidae': '#2f75b5',
 'Aphroditidae': '#2f75b5',
 'Acoetidae': '#2f75b5',
 'Chrysopetalidae': '#2f75b5',
 'Eulepethidae': '#2f75b5',
 'Lopadorrhynchidae': '#2f75b5',
 'Polynoidae': '#2f75b5',
 'Nereididae': '#2f75b5',
 'Nephtyidae': '#2f75b5',
 'Glyceridae': '#2f75b5',
 'Goniadidae': '#2f75b5',
 'Tomopteridae': '#2f75b5',
 'Pilargidae': '#2f75b5',
 'Lacydoniidae': '#2f75b5',
 'Pontodoridae': '#2f75b5',
 'Sigalionidae': '#2f75b5',
 'Hesionidae': '#2f75b5',
 'Sphaerodoridae': '#2f75b5',
 'Phyllodocidae': '#2f75b5',
 'Iospilidae': '#2f75b5',
 'Serpulidae': '#fff2cc',
 'Sabellidae': '#fff2cc',
 'Cossuridae': '#ffd966',
 'Spionidae': '#ffc000',
 'Trochochaetidae': '#ffc000',
 'Poecilochaetidae': '#ffc000',
 'Longosomatidae': '#ffc000',
 'Sabellariidae': '#ffc000',
 'Sternaspidae': '#bf8f00',
 'Paraonidae': '#bf8f00',
 'Maldanidae': '#806000',
 'Ampharetidae': '#806000',
 'Pectinariidae': '#806000',
 'Trichobranchidae': '#806000',
 'Terebellidae': '#806000',
 'Arenicolidae': '#806000',
 'Scalibregmatidae': '#806000',
 'Opheliidae': '#fce4d6',
 'Capitellidae': '#fce4d6',
 'Thalassematidae': '#fce4d6',
 'Cirratulidae': '#f4b084',
 'Flabelligeridae': '#f4b084',
 'Orbiniidae': '#ed7d31',
 'Megascolecidae': '#c65911',
 #'Sipunculidae': '#833c0c',
 'Aspidosiphonidae': '#833c0c',
 'Non-identified': '#000000'}


## CONTINENTE
# cores_continente = {
#     "#N/D":"#5e4028",
#     "América do Sul":"#10b651",
#     "América Central":"#bce091",
#     "América do Norte":"#21638f",
#     "Ásia":"#d963cf",
#     "África":"#52e9e6",
#     "Europa":"#8d102b"
# }

cores_continente= {
    "#N/D":"#000000",
    #"nan":"#000000",  # tratei separado, por ora
    "América do Sul":"#40a43b",
    "América Central":"#bbe272",
    "América do Norte":"#255026",
    "Ásia":"#db11ac",
    "África":"#a96370",
    "Europa":"#208eb7"
}


## COUNTRY (different shades of its CONTINENT color - selected using Colorcrafter)
### América do Sul
### ['#bbffd4', '#94efc6', '#57d5c9', '#00b8cc', '#0096c9', '#0071ba', '#004da4', '#002e8b', '#00237a']
### '#a6d2eb', '#9ebdcb'
### América Central
### ['#e3ff63', '#caf94f', '#b2e439', '#9acf1c', '#81ba00', '#69a600', '#519200', '#3a7e00', '#256b00']
### Ásia
### ['#f0c0d7', '#e5aec6', '#d89bb2', '#cb879c', '#bc7386', '#ad6274', '#9e5466', '#8f485a', '#803e4c']
### África
### ['#ffceb2', '#ffba94', '#efaa79', '#d39a5f', '#ba8a47', '#a57b34', '#956c25', '#895d1a', '#815010']
### Europa
### ['#ffcea9', '#ffb996', '#ffa583', '#ff916f', '#ff7d5c', '#eb6949', '#d25638', '#ba4327', '#a52e17']

### p.s.: old approach
# cores_pais = {
#     '#N/D':'#5e4028',
#     'nan':'#000000',  # preto
#     # América do Sul
#     'Brasil':'#00237a',
#     'Uruguai':'#002e8b',
#     'Colômbia':'#004da4',
#     'Peru':'#0071ba',
#     'Paraguai':'#0096c9',
#     'Argentina':'#00b8cc',
#     'Guiana Francesa':'#57d5c9',
#     'Venezuela':'#94efc6',
#     'Guiana':'#9ebdcb',
#     'Chile':'#bbffd4',
#     'Equador':'#a6d2eb',
#     # América Central
#     'Guatemala':'#e3ff63',
#     'Panamá':'#caf94f',
#     'Porto Rico':'#b2e439',
#     'Costa Rica':'#9acf1c',
#     'México':'#256b00',
#     'Nicarágua':'#81ba00',
#     'Honduras':'#69a600',
#     'Cuba':'#519200',
#     'República Dominicana':'#3a7e00',
#     # América do Norte
#     'Estados Unidos':'#80c6b8',
#     # Ásia
#     'Israel':'#803e4c',
#     'Indonésia':'#9e5466',
#     'Índia':'#bc7386',
#     'Filipinas':'#d89bb2',
#     # África
#     'África do Sul':'#ba8a47',
#     'Egito':'#efaa79',
#     # Europa
#     'Bósnia e Herzegovina':'#ffb996',
#     'Romênia':'#ff916f',
#     'Alemanha':'#eb6949',
#     'Kingdom':'#ba4327'
# }


### new approach: inspired on Hans Rosling (countries are colored the same as its continents)
# colors chosen according to the old olympics convention (see https://www.npr.org/sections/thetorch/2012/08/10/158569089/seeing-the-world-through-the-olympic-rings-and-infographicsinfographics#:~:text=The%20Olympic%20Charter%20once%20ascribed,Oceania%2C%20and%20red%20for%20America.)

# Each ring symbolizes one of the five continents competing at the Olympics: Africa (yellow), the Americas (red), Asia (green), Europe (black), and Oceania (blue)
cores_pais = {
    '#N/D':'#000000',
    'nan':'#000000',  # preto
    # América do Sul
    'Brasil':'#40a43b',
    'Uruguai':'#40a43b',
    'Colômbia':'#40a43b',
    'Peru':'#40a43b',
    'Paraguai':'#40a43b',
    'Argentina':'#40a43b',
    'Guiana Francesa':'#40a43b',
    'Venezuela':'#40a43b',
    'Guiana':'#40a43b',
    'Chile':'#40a43b',
    'Equador':'#40a43b',
    # América Central
    'Guatemala':'#bbe272',
    'Panamá':'#bbe272',
    'Porto Rico':'#bbe272',
    'Costa Rica':'#bbe272',
    'México':'#bbe272',
    'Nicarágua':'#bbe272',
    'Honduras':'#bbe272',
    'Cuba':'#bbe272',
    'República Dominicana':'#bbe272',
    # América do Norte
    'Estados Unidos':'#255026',
    # Ásia
    'Israel':'#db11ac',
    'Indonésia':'#db11ac',
    'Índia':'#db11ac',
    'Filipinas':'#db11ac',
    # África
    'África do Sul':'#a96370',
    'Egito':'#a96370',
    # Europa
    'Bósnia e Herzegovina':'#208eb7',
    'Romênia':'#208eb7',
    'Alemanha':'#208eb7',
    'Kingdom':'#208eb7'
}



### South America countries (only)
cores_AS = {
    'Brasil':'#40a43b',
    'Uruguai':'#40a43b',
    'Colômbia':'#40a43b',
    'Peru':'#40a43b',
    'Paraguai':'#40a43b',
    'Argentina':'#40a43b',
    'Guiana Francesa':'#40a43b',
    'Venezuela':'#40a43b',
    'Guiana':'#40a43b',
    'Chile':'#40a43b',
    'Equador':'#40a43b',
}



### BRAZILIAN REGION
cores_regioes = {
    'N':'#22695e',   # forest
    'NE':'#ea1349',  # hot
    'CO':'#69ef7b',   # light green vegetation (Cerrado)
    'SE':'#992a1c',  # emphatic color
    'S':'#7ee7d3'   # cold
}

cores_regioes2 = {
    'N':'#2a6866',   # forest
    'NE':'#cc4c3e',  # hot
    'CO':'#7fa69d',
    'SE':'#bb8377',
    'S':'#48bf8e'   # cold
}

# SE: ['#f6ccd0', '#eababc', '#dba9a6', '#cb968e', '#bb8377', '#ab7364', '#9c6556', '#8d594b', '#7d4f3f']
# NE: ['#ffc7aa', '#ffb499', '#ffa389', '#ff917a', '#ff7f68', '#f36e5a', '#df5d4b', '#cc4c3e', '#b83b2f']
# S: ['#9bffff', '#72f7fd', '#3be5f4', '#00d3ea', '#00c2e0', '#00b2d6', '#00a2cc', '#0093c1', '#0084b5']
# N: ['#c5e1cf', '#afd2c1', '#97c2b3', '#7db2a6', '#63a098', '#4c908a', '#3d827d', '#337570', '#2a6866']
# CO: ['#fffdfd', '#efeef0', '#d8dee3', '#c1ccd7', '#a8bac9', '#94aabb', '#869bad', '#7b8d9f', '#738093']

## old approach
# cores_estados = {
#     # SE
#     'Rio de Janeiro':'#8d594b',
#     'São Paulo':'#ab7364',
#     'Espírito Santo':'#cb968e',
#     'Minas Gerais':'#eababc',
#     # NE
#     'Pernambuco':'#b83b2f',
#     'Bahia':'#cc4c3e',
#     'Ceará':'#df5d4b',
#     'Paraíba':'#f36e5a',
#     'Alagoas':'#ff7f68',
#     'Piauí':'#ff917a',
#     'Rio Grande do Norte':'#ffa389',
#     'Sergipe':'#ffb499',
#     # S
#     'Paraná':'#0084b5',
#     'Santa Catarina':'#00a2cc',
#     'Rio Grande do Sul':'#00c2e0',
#     'Santa Catarina-Rio Grande do Sul':'#3be5f4',        # ERRO NA BASE
#     # N
#     'Amazonas':'#2a6866',
#     'Roraima':'#337570',
#     'Pará':'#3d827d',
#     'Acre':'#4c908a',
#     'Rondônia':'#63a098',
#     'Maranhão':'#7db2a6',
#     'Amapá':'#97c2b3',
#     'Tocantins':'#afd2c1',
#     # CO
#     'Goiás':'#7b8d9f',
#     'Mato Grosso':'#869bad',
#     'Mato Grosso do Sul':'#94aabb',
#     'Distrito Federal':'#a8bac9',
#     'Brasília':'#c1ccd7',
#     'Minas Gerais/Goiás/Distrito Federal':'#d8dee3',    # ERRO NA BASE
# }

## new approach: inspired in Hans Rosling (each state is colored after its region)
cores_estados = {
    # N
    'Acre':'#22695e',
    'Amapá':'#22695e',
    'Amazonas':'#22695e',
    'Maranhão':'#22695e',
    'Pará':'#22695e',
    'Rondônia':'#22695e',
    'Roraima':'#22695e',
    'Tocantins':'#22695e',
    # NE
    'Alagoas':'#ea1349',
    'Bahia':'#ea1349',
    'Ceará':'#ea1349',
    'Paraíba':'#ea1349',
    'Pernambuco':'#ea1349',
    'Piauí':'#ea1349',
    'Rio Grande do Norte':'#ea1349',
    'Sergipe':'#ea1349',
    # CO
    'Brasília':'#69ef7b',
    'Distrito Federal':'#69ef7b',
    'Goiás':'#69ef7b',
    'Mato Grosso':'#69ef7b',
    'Mato Grosso do Sul':'#69ef7b',
    'Minas Gerais/Goiás/Distrito Federal':'#69ef7b',    # ERROR IN DATABASE
    # SE
    'Espírito Santo':'#992a1c',
    'Minas Gerais':'#992a1c',
    'Rio de Janeiro':'#992a1c',
    'São Paulo':'#992a1c',
    # S
    'Paraná':'#7ee7d3',
    'Rio Grande do Sul':'#7ee7d3',
    'Santa Catarina':'#7ee7d3',
    'Santa Catarina-Rio Grande do Sul':'#7ee7d3',        # ERROR IN DATABASE

}
