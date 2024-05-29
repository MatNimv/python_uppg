#Kod nedan avser en inlämningsuppgift i kursen Grundläggande programmering i Python på Borås Högskola VT 2024.

#Nedan är ett program som arbetar med en två befolkningslistor mellan år 2019 - 2100 respektive 2022 - 2100
#Programmet innehåller 5 olika analyserande funktioner som bearbetar dessa två listor
#Samt visualiserar även dom på olika sätt.
#Främst används datan från befolkningsdata_2019 men i uppg5 används även befolkningdata_2022.

import csv
import matplotlib.pyplot as plt

#Funktioner
#har lagt till funktioner jag anser underlättar
#koden, så jag inte behöver duplicera kod och gör även den mer lättläst.

#tar fram de 10 länder med högsta respektiva lägsta värden baserat på
#sista elementet (i detta fall befolkningsutveckling)
def high_low_utv(lista):
    return sorted(lista, key=lambda x: -x[-1])[:5] + sorted(lista, key=lambda x: x[-1])[:5]

#tar emot en lista av värden och räknar ut den förväntade
#befolkningsutvecklingen för en lista av länder
def calc_expected_growth(land_list):
    last_year = int(land_list[len(land_list) - 1])
    first_year = int(land_list[0])
    return (last_year - first_year)/first_year * 100


# Deluppgift 1: Funktioner från deluppgift 1 i ordning.
# Skriv din kod här:

#printar ut de två första raderna av given fil
def print_rows(file, name):
    if(file == []):
        print(f'{name} är tom.')
    else:
        print(f'{"\nFörsta två raderna av"} {name}:')
        for row in file[:2]:
            print(row)
        print("\n")

#läser in en fil och returnerar filen i sträng-format för 
#lättare hantering.
def read_file(file_name):
    data_list = []

    with open (file_name, 'r', encoding='ISO-8859-1') as file:
        csv_reader = csv.reader(file, delimiter = ';') 
        for rad in csv_reader:                         
            data_list.append(rad)                      

    return data_list

# Deluppgift 2: Funktioner från deluppgift 2 i ordning.
# Skriv din kod här:

#kalkylerar data från befolkningsdata2022 
#för visualisering i uppg3
def analysera_data_uppg2(lista):
    #två min och max funktioner som tar fram
    #högsta resp. lägsta talet och returnerar
    #talet samt dess index för årtal för lätt
    #åtkomst i uppg2 funktionen
    def max_value(num_lista):
        max = 0
        idx_year = 0
        for index, value in enumerate(num_lista):
            if(int(value) > max):
                max = int(value)
                idx_year = index
        return [max, idx_year]
    
    def min_value(num_lista):
        #börjar från det högsta talet då 0 alltid
        #kommer vara lägst.
        min = max_value(num_lista)[0]
        idx_year = 0
        for index, value in enumerate(num_lista):
            if(int(value) < min):
                min = int(value)
                idx_year = index
        return [min, idx_year]
    
    #tar emot lista av länder, indexet av den listan
    #och returnerar en array av ett lands data
    def country_by_index(index, land_list):
        return land_list[index]

    #skapar en ny lista med länder som är formaterat med befolkningsdata och dess utveckling
    #för lättare tabellskrivning i uppg3
    analyserad_lista2 = []

    for land in lista[1:]:
        #för varje land, tas det högsta samt lägsta befolkningsvärdet fram.
        #så jag strukturerat country_by_index() tas även indexet av 
        #befolkningsvärdet fram, och kan därför direkt komma åt året med hjälp av årslistan.
        country_data = []
        low_bef = min_value(land[1:])
        low_bef_year = country_by_index(low_bef[1], lista[0][1:])

        high_bef = max_value(land[1:])
        high_bef_year = country_by_index(high_bef[1], lista[0][1:])

        expected_growth = calc_expected_growth(land[1:])
        
        #skapar en array med den analyserade datan, vars indexdata
        #läggs till för varje land i den nya listan för uppg2
        data_for_analysed_list = [land[0], int(low_bef[0]), int(low_bef_year), int(high_bef[0]), int(high_bef_year), float(round(expected_growth, 2))]
        for data in data_for_analysed_list:
            country_data.append(data)

        analyserad_lista2.append(country_data)

    return analyserad_lista2



# Deluppgift 3: Funktioner från deluppgift 3 i ordning.
# Skriv din kod här:

#finskriver data från uppgift 2 till en tydlig tabell med befolkningsmassa, årtal och befolkningsutveckling.
def analysera_data_uppg3(lista):
    #variabler för att strukturera tabellen.
    delare="------------------------------------------------------"
    delare2="====================================================="
    delare3="-------------------------"

    print(f'{delare:^100} \n \n {"Förväntad befolkningsutveckling för tio länder inom EU under åren 2022 -- 2100":^100}\n \n {"(Tabellen visar de fem länder med störst respektive minst förväntad befolkningsökning)":^100}\n {delare2:^100} \n {"Estimerad befolkning":^100} \n {delare3:^100}')
    print(f'{'Land':<20} {"Lägst befolkningsantal":>20} {"Högst befolkningsantal":>27} {"Förändring [%]":>14}')
    print(f'{"Befolkning":>31} {"År":>10} {"Befolkning":>16} {"År":>10} {"2022-2100":>14}')

    #de tio länderna med högst resp. lägst befutv
    high_low_utv_lands = high_low_utv(lista)

    #visualisera ländernas data under titlarna som skrivits ut ovan
    for land in high_low_utv_lands:
        print(f'{land[0]:<18}', end='')
        for data in land[1:]:
            print(f'{data:>13}', end='')
        print("\n")

# Deluppgift 4: Funktioner från deluppgift 4 i ordning.
# Skriv din kod här:

#funktionen tar emot en lista av länder och normerar ländernas data
#till ett linjediagram - de 10 länderna med högst och lägst befutv
def analysera_data_uppg4(lista):
    #få ut lista av namn på länderna 
    #med högst/lägst befutv
    #uppg2 listan skickas med då funkionen kräver den strukturen av data
    #med befolkningsutveckling i %
    high_lows = high_low_utv(analysera_data_uppg2(befolkningsdata_2022))
    high_low_lands = []
    for land in high_lows:
        #namnet på landet sparas för 
        #filtrering nedan
        high_low_lands.append(land[0])

    # år 2022 har värdet 100
    norm_bas = 100 
    normerad_data = []
    for i in range(1, len(lista[1:][1:])):
        #filtrera ut de länderna med högsta och 
        #lägsta befutv till tabellen
        if (lista[1:][i][0] in high_low_lands):
            #lägger till landnamn och varje års normerad data
            #med år 2022 som bas / första året som data finns för
            rel_utv = []
            rel_utv.append(lista[1:][i][0]) #namn på landet
            norm_siffra = lista[i][1] #data för år 2022
            for data in lista[i][1:]:
                #med norm_siffran (året som data relateras till), data (årets data) och norm_bas (värdet datan normeras till)
                #kan vi räkna ut året av ett lands befolkningsdata utväxt i jämförelse med basåret
                norm_year = (int(data) / int(norm_siffra)) * norm_bas
                rel_utv.append(round(norm_year, 1))
            normerad_data.append(rel_utv)
    
    #plotta datan. listan för färger och länder är lika långa så de 
    #går parallellt för att få ut en färg för varje land
    years_list = lista[0][1:]
    land_colours = ["blue", "green", "red", "purple", "orange", "black", "yellow", "brown", "cyan", "pink"]
    for i in range(len(normerad_data)):
        #förtydligar datan till variabler, sätter in de för
        #x, y-axeln, färg och landnamn.
        data = normerad_data[i][1:]
        land_label = normerad_data[i][0]
        colour= land_colours[i]
        plt.plot(years_list, data, color=colour, label=land_label)

    #inställningar och beskrivningar för
    #plottgrafen.
    plt.legend(loc='upper left')
    plt.xlabel("År")
    plt.ylabel("Relativ befolkningsutveckling. Indexår 2022")
    plt.title("Förväntad befolkningsutveckling inom EU för tidsperioden 2022 - 2100")
    plt.grid(True)
    plt.show()


# Deluppgift 5: Funktioner från deluppgift 5 i ordning.
# Skriv din kod här:

#funktionen räknar ut varje lands förväntade befutv 
#från både datasetten - befolkningsutväxt_2019 & befolkningsutväxt_2022
#och plottar/jämför detta på ett horisontellt stapeldiagram. 
def analysera_data_uppg5(lista_1, lista_2):
    #funktionen kan bara köras om båda listorna har lästs in
    if(lista_1 == []) or (lista_2 == []):
        print("Se till att hämta båda listorna i menyval 1!")
        return
    else:
        country_data_2019 = []
        country_data_2022 = []
        expect_growth_2019 = []
        expect_growth_2022 = []
        bef_sort_2019 = []
        bef_sort_2022 = []
        countries = []

        for i in range(1, len(lista_1[1:])):
            #respektive data från 2019 och 2022 + land samt befutv slås samman
            country_data_2019.append([lista_1[i][0], int(round(calc_expected_growth(lista_1[i][1:]),0))])
            country_data_2022.append([lista_2[i][0], int(round(calc_expected_growth(lista_2[i][1:]),0))])

        #sorterar både bef_utv listorna med landet - högst till lägst
        bef_sort_2019 = sorted(country_data_2019, key=lambda x: x[1])
        bef_sort_2022 = sorted(country_data_2022, key=lambda x: x[1])
        
        #sätter tillslut isär datan. länderna i egen array
        #samt respektive årsdata för egen stapel.
        #nu har listorna samma struktur för diagramet nedan
        for i in range(len(bef_sort_2019)):
            countries.append(bef_sort_2019[i][0])
            expect_growth_2019.append(bef_sort_2019[i][1])
            expect_growth_2022.append(bef_sort_2022[i][1])

        #plottar ut datan i ett horisontellt diagram.
        #ser till att ett land i y-axeln innefattar två olika års data
        #ovan/under varandra med varsin stapel
        stack_w = 0.40
        plt.barh([i - stack_w/2 for i in range(len(countries))], expect_growth_2019, stack_w, color="yellow", label="2019-2100") 
        plt.barh([i + stack_w/2 for i in range(len(countries))], expect_growth_2022, stack_w, color="blue", label="2022-2100")
        plt.yticks(range(len(countries)), countries)

        plt.legend(loc="lower right")
        plt.grid(True)
        plt.show()


# Huvudprogram med Meny från deluppgift 0. Använd menyrubriker enl. uppgiftsbeskrivningen.
# Skriv din kod här:

#Deluppgift 0
programme_is_running = True
befolkningsdata_2019 = []
befolkningsdata_2022 = []

#programmet fortsätter tills användaren själv trycker avbryt (6)
while (programme_is_running == True):
    print(f'{"Meny":>20} \n {"=====":>20}')
    menyval = input("1. Hämta data från fil – uppgift 1 \n 2. Analysera data - uppgift 2 \n 3. Analysera data - uppgift 3 \n 4. Analysera data - uppgift 4 \n 5. Analysera data - uppgift 5 \n 6. Avsluta \n \n Välj menyalternativ (1-6) \n")
    
    if (menyval == "1"):
        
        #användaren har möjligheten att skriva ut filnamnen för inläsning av båda 
        #filerna, eller för enkelhetens skull endast trycka enter.
        indata_bef_utv2019 = input("Skriv filnamn befolkningdata_2019 eller ENTER.\n")
        if(indata_bef_utv2019 == "befolkningsdata_2019") or ( indata_bef_utv2019 == ""):
            befolkningsdata_2019 = read_file('befolkningsdata_2019.csv')
        else: 
            print("Vänligen följ instruktionerna.")
            continue

        indata_bef_utv2022 = input("Skriv filnamn befolkningdata_2022 eller ENTER.\n")
        if(indata_bef_utv2022 == "befolkningsdata_2022") or ( indata_bef_utv2022 == ""):
            befolkningsdata_2022 = read_file('befolkningsdata_2022.csv')
        else: 
            print("Vänligen följ instruktionerna.")
            continue

        #printar ut så användaren kan se om datan ser ok ut
        print_rows(befolkningsdata_2019, "befolkningsdata_2019")
        print_rows(befolkningsdata_2022, "befolkningsdata_2022")
        continue

    elif(menyval == "2"):
        #iomed att det inte ska vara någon utskrift
        #av analyseringen printas det en bekräftelse
        #att funktionen har utförts för användaren 
        analysera_data_uppg2(befolkningsdata_2022)
        print("Data har analyserats.")
        continue

    elif(menyval == "3"):
        list_data = analysera_data_uppg2(befolkningsdata_2022)
        analysera_data_uppg3(list_data)
        continue

    elif(menyval == "4"):
        analysera_data_uppg4(befolkningsdata_2022)
        continue

    elif(menyval == "5"):
        analysera_data_uppg5(befolkningsdata_2019, befolkningsdata_2022)
        continue

    elif (menyval == "6"):
        programme_is_running = False
        print("Du har avslutat programmet.")
        break
    else:
        print("Vänligen välj en siffra mellan 1-6. \n")
        continue

