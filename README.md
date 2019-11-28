# NAI - AI tools classes
Data minning project <br />
The script is computing Pearson correlation score between choosen person and all the other people defined in data. <br />
Based on fixed numer of three people that have highest score similairity, script is creating arrays of recommended and unrecommended movies for choosen person. <br />

### Requirements
```
Anaconda (Python 3.7) or Python 3.7
Python IDE (for development)
CSV data file

```

### CSV data file guide

Create CSV named "Dane_filmowe.csv" in folder where script "main.py" is located. <br />
File should contain data formated as following: <br />
In below example line one is header and two following lines are data records. <br />
You can have as many data records as you like. There is also no restriction to <br />
header length and record length.
```
Person,Group,Movie,Grade Scale(1-10),2,,3,,4,,5,,6,,7,,8,,9,,10,,11,,12,,13,,14,,15,,16,,17,,18,,19,,20,,21,,22,,23,,24,,25,,26,,27,,28,,29,,30,,31,,32,,33,,34,,35,,36,,37,,38,,39,,40,,41,,42,,43,,44,,45,
Some Person,Some Group,Polowanie na Czerwony Październik,10,Rick i Morty,10,Teoria Wielkiego Podrywu,8,Braveheart - Waleczne Serce,10,The Expanse,7,Miasteczko South Park,9,Kraina Lodu,5,Dziennik Bridget Jones,6,Kapitan Ameryka: Wojna bohaterów,3,Avengers: Czas Ultrona,2,Terminator 2,9,Planeta Singli,7,List do M. ,7,List do M. 2,2,Detektyw,7,Forrest Gump,9,Ex Machina,10,Gran Torino,9,Cicha Noc,1,Battleship: Bitwa o Ziemię,1,Narodziny Gwiazdy,2,Kapitan Phillips,9,Grand Budapest Hotel,9,Wyjazd integracyjny,1,John Wick,5,Narcos,10,Terminal,8,Ona,8,Whipslash,10,Diabeł ubiera się u Prady,9,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
Some Person2,Some Group,Komando,7,Uciekinier,8,Upadek,9,Armia ciemności,8,Flash Gordon,10,Ex Machina,8,Raport z europy,7,Otchłań,7,To nie jest kraj dla starych ludzi,10,Wywiad z wampirem,9,Blade - wieczny łowca,8,Conan barbarzyńca,10,Pokłosie,2,Diuna,4,Avengers: koniec gry,3,Botoks,1,"Piłsudski",2,Star trek: w nieznane,3,Ad astra,5,"Corgi, psiak królowej",3,Glass,7,Iron sky. Inwazja,3,John Wick 3,6,Kapitan Marvel,5,Men in Black: International,2,Róża,10,Kevin sam w domu,1,Rekinado,2,Rekinado 2:Drugie ugryzienie,3,Gran torino,8,Tropiciel,7,Polowanie na Czerwony Październik,7,Rick i Morty,5,Teoria Wielkiego Podrywu,7,Braveheart - Waleczne Serce,7,The Expanse,5,Miasteczko South Park,9,Kraina Lodu,3,Dziennik Bridget Jones,3,Kapitan Ameryka: Wojna bohaterów,5,Avengers: Czas Ultrona,5,Terminator 2,9,Złe mięso,3,Pacific Rim,7,,

```


### Running Application

To run script use following syntax in Python console <br />
```
In Spyder IDE (Anaconda):
runfile('disk:\path\to\script\main.py', args='--user "some person"', wdir='disk:\path\to\script\')

Example usage:
runfile('D:/Informatyka/NAI/lab4/main.py', args='--user "Some Person"', wdir='D:/Informatyka/NAI/lab4')

In Anaconda terminal (use it inside folder containing script):
python main.py --user "Paweł Czapiewski"

In PyCharm IDE (Python):
main.py --user "Some Person"

In Python terminal (not tested, but it should work):
python main.py --user "Paweł Czapiewski"

```


## Authors

* **Jakub Wąsowski** - [JWasowski](https://github.com/jwasowski)
* **Grzegorz Żukowski** - 