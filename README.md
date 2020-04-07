# Omówienie głównych plików
Części serwera:
  - database.py odpowiada za komunikację z bazą danych SQLite
  - menu.py odpowiada za komunikację z użytkownikiem, jest możliwa edycja, usuwanie, dodawanie oraz przeglądanie informacji 
  - server.py zajmuję się przetwarzaniem odczytów od 
  - pomniejsze pliki odpowiadające za funkcjonalności aplikacji
  
Części klienta (terminale)
  - client.py skrypt działający na terminalu, skanujący karty i przesyłający ich numer RFID, do zapisania w bazie danych w tabeli odczytów


Funkcjonalności
  - Tworzenie wykazu czasu pracy pracownika w arkuszu kalkulacyjnym
  - dodawanie, usuwanie i edycja bazy danych
  - spis odczytów pracowników

### Technologie

* [Python] - Python ftw!
* [SQLite] - simple database for applications.
* [MQTT] - lightweight messaging protocol, perfect for IoT!


### Uruchomienie

Aplikacja zajmująca się bazą danych to skrypt pod nazwą menu.py. Znajdą się tam funkcjonalności pozwalające na zarządzanie danymi w aplikacji.

Aby sprawdzić komunikację  SERWER - KLIENT. Proszę w jednej konsoli odpalić server.py a w drugiej client.py. 
W kliencie podać nazwę terminalu oraz to czy zajmuję się on wejściem pracowników czy wyjściem.
Nastepnie można dodać odczyt. Tutaj lista kilku identyfikatorów RFID w mojej bazie danych: 
513465
856143
315135
451532
515325
543626
51532

Gdy poda się nieistniejący identyfikator, serwer powinien dodać nową kartę bez przypisanego użytkownika (karte anonimową) oraz dodać odczyt karty do tabeli Readings.

### Plany

Zrobić refactoring kodu oraz dodać detale, które pozwolą o wiele wygodniej pracować w aplikacji.
Również czekam na odpowiedź prowadzącego na temat podziału pliku serwer.py oraz menu.py.
