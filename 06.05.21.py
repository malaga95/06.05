class Processing:
    #Funkcja wewnatrz klasy to metoda w tym przypadku jest to funkcja inicjalizatora
    def __init__(self, filename): #po selfie podaje argumenty wchodzace zewnatrz do klasy
        self.filename = filename    #ustawianie atrybutu self.filename
        self.lines = []      #Tworzy pusta liste
        self.read()          #ustawia atrybut self.lines za pomoca metody "read"
        self.work_data = self.preparefilter() #ustawiam atrybut work_data za pomoca metody

    def read(self): # metoda ktora wczytuje dane z pliku
        file = open(self.filename)
        self.lines = file.readlines()
        file.close()
    
    def preparefilter(self):                        #Metoda do budowania struktury danych
        data = {}                                   #wygodny format danych dla których mozna pokazac dane
        
        for line in self.lines[1:]:                 #petla po wszystkich wierszach
            per_day = []                                                        #pomocnicza lista na dane z "dnia"
            line_separator = line.split(",")                                    #separowanie kolumn dzieki kluczowi ","
            per_day_dict = {}                                                   #pomocniczy słownik danych na dzien
            per_day_dict['date'] = line_separator[3]                            #przypisanie wartosci daty, do klucza "date"
            if line_separator[4]:                                               #Sprawdzenie czy total_cases nie jest pustym stringiem, jesli jest, nie mapujemy na float
                per_day_dict['total_cases'] = float(line_separator[4])
            else:
                per_day_dict['total_cases'] = line_separator[4]
            if line_separator[5]:                                               #to samo co w total_cases
                per_day_dict['new_cases'] = float(line_separator[5])            
            else:
                per_day_dict['new_cases'] = line_separator[5]
            per_day.append(per_day_dict)                                        #dodawanie do listy, slownikow zawierajacych dane dla kazdego dnia
            if line_separator[2] in data:                                       #Sprawdzenie czy taki klucz istnieje w slowniku
                data[line_separator[2]].append(per_day_dict)                                         #jesli tak, dokladamy elementy
            else:
                data[line_separator[2]] = per_day                                                    #jesli nie, to tworzymy nowy slownik
        return data                         #zwracamy gotowy slownik z przetworzonymi danymi



proc = Processing("covid_data2021.csv")   #wywolujemy klase
print(proc.work_data['Poland'])

'''data = {'Poland' : [
    {
    'date': '02-02-2020',
    'total_cases': 2,
    'new_cases': 2
    },                                                      #FORMAT DANYCH ATRYBUTU work_data dla klasy Processing()
    {
    'date': '03-02-2020',
    'total_cases': 2,
    'new_cases': 2
    },
    ]
}
'''
