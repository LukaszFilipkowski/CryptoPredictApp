## 1.	Charakterystyka oprogramowania

Nasza aplikacja nazywa się Crypto Oracle Analytics - w skrócie - COA.

Nasza aplikacja służy do prognozowania cen kryptowalut z wykorzystaniem modelu ARIMA. System analizuje historyczne dane cenowe (kursy zamknięcia), identyfikuje zależności czasowe i na ich podstawie generuje krótkoterminowe (jednodniowe) predykcje wraz z związanymi z tymi predykcjami niepewnościami. Wyniki prezentowane są w czytelnej formie wykresów i prognoz.
Celem COA jest dostarczenie użytkownikom prostego, ale solidnego narzędzia prognostycznego opartego na klasycznej metodzie statystycznej, które wspiera podejmowanie świadomych decyzji inwestycyjnych. Aplikacja ma ponadto na celu pokazanie praktycznego zastosowania modelu ARIMA w analizie finansowych szeregów czasowych.

## 2.	Prawa autorskie
Autorami aplikacji są: Natalia Kurczyńska, Łukasz Filipkowski.

Nasze oprogramowanie jest udostępnione na licencji MIT License, co oznacza, że każdy może korzystać z kodu, kopiować go, modyfikować, łączyć, publikować, rozpowszechniać, sublicencjonować oraz sprzedawać kopie oprogramowania. Jedynym warunkiem jest zachowanie informacji o prawach autorskich oraz treści licencji w każdej kopii lub istotnej części oprogramowania.

## 3. Specyfikacja wymagań

|ID | NAZWA | OPIS | PRIORYTET | KATEGORIA |
|---|-------|------|-----------|-----------|
|F-01|Wybór kryptowaluty| Użytkownik może wybrać kryptwalutę, dla której zostanie wykonana analiza.|1|Funkcjonalne - Dobór danych|
|F-02|Wizualizacja danych historycznych| Aplikacja umożliwia użytkownikowi sprawdzenie zmienności cen kryptowalut we wskazanym okresie.|1|Funkcjonalne - Wizualizacja|
|F-03|Generowanie prognozy| Po wybraniu kryptowaluty przez użytkownika, aplikacja wyświetli prognozę ceny tej kryptowaluty na następny dzień.|1| Funkcjonalne - Prognozowanie|
|F-04|Zwizualizowanie prognozy| Użytkownik będzie miał możliwość zobaczenia na wykresie wygenerowanej wartości prognozy wraz z wyznaczonym dla niej przedziałem ufności.|1|Funkcjonalne - Wizualizacja|
|F-05|Eksport wykresów|Użytkownik ma możliwość zapisania wykresów po ich wygenerowaniu.|2|Funkcjonalne - Eksport|
|F-06|Czytelny interfejs|Aplikacja posiada czytelny i intuicyjny interfejs graficzny (GUI), umożliwiający łatwą obsługę programu przez użytkownika.|1|Niefunkcjonalne|
|F-07|Czas oczekiwania|Czas oczekiwania na odpowiedź aplikacji jest krótki, prognoza pojawia się na ekranie w zaledwie kilka sekund po wysłaniu zapytania.|1|Niefunkcjonalne|

(Priorytet: 1 - wymagane, 2 - przydatne, 3 - opcjonalne)

## 4. Architektura systemu/oprogramowania

Architektura rozwoju

|Technologia|Przeznaczenie|Nr wersji|
|-----------|-------------|---------|
|Python|Język programowania|3.12.11|
|Spyder|IDE do programowania w Pythonie| 5.15.11|
|Git|Kontrola wersji|2.52|
|GitHub|Hosting repozytorium|-|
|Biblioteka "pandas"|Analiza danych|2.3.3|
|Biblioteka "statsmodels"|Model ARIMA|0.14.6|
|Biblioteka "tkinter"|Graficzny interfejs użytkownika|8.6|
|Biblioteka "matplotlib"|Wizualizacja danych|3.10.8|
|Biblioteka "os"|Interakcja z systemem operacyjnym"|jak Python|
|Biblioteka "time"|Obsługa i mierzenie czasu|jak Python|
|Biblioteka "datatime"|Praca z datami i czasem|jak Python|

Architektura uruchomieniowa

|Technologia|Przeznaczenie| Nr wersji|
|-----------|-------------|----------|
|Python|Uruchamianie aplikacji|3.12.11|
|Wymagane biblioteki z architektury rozwoju|Możliwość pracy z aplikacją|-|

## 5. Procedura uruchomieniowa
Aplikacja została napisana w języku Python i działa jako aplikacja okienkowa.
W aktualnej wersji uruchamiana jest poprzez wykonanie kodu źródłowego, bez użycia pliku wykonywalnego .exe.

1. Wymagania systemowe.
 - Python 3.10 lub nowszy
 - System operacyjny Windows/macOS
 - Dostęp do terminala

2. Instalacja wymaganych bibliotek

Przed pierwszym uruchomieniem należy zainstalować wszystkie wymagane biblioteki wskazane w architekturze rozwoju.

3. Uruchomienie aplikacji

Aplikacja uruchamiana jest poprzez wykonanie głównego pliku programu. Należy otworzyć terminal w katalogu z plikiem programu (MAIN.py) i  wykonać polecenie "python MAIN.py"

Po wykonaniu tego polecenia otwiera się graficzne okno aplikacji Crypto Oracle Analytics.

## 6. Testy akceptacyjne

W projekcie zastosowano kilka testów akceptacyjnych, z których każdy weryfikuje inną kluczową funkcjonalność aplikacji z perspektywy użytkownika końcowego.

Scenariusze testów:

### Test A1: Wczytanie danych i wizualizacja

Warunki początkowe:

- Aplikacja uruchomiona
- Brak danych w tabeli i na wykresie

Kroki:

- Użytkownik klika przycisk „Wczytaj dane”
- Wybiera poprawny plik CSV zawierający daty i wartości
- Dane zostają wczytane do tabeli
- Wykres zostaje automatycznie odświeżony

Oczekiwany rezultat:

- Tabela zawiera dane z pliku CSV
- Wykres przedstawia dane historyczne
- Tytuł wykresu odpowiada nazwie wczytanego pliku

### Test A2: Wykonanie predykcji

Warunki początkowe:

- Dane zostały poprawnie wczytane
- Liczba obserwacji ≥ 20

Kroki:

- Użytkownik klika przycisk „Predykcja (t+1)”
- Aplikacja oblicza prognozę kolejnej wartości
- Wynik zostaje dodany do tabeli
- Wykres aktualizuje się o punkt predykcji

Oczekiwany rezultat:

- W tabeli pojawia się nowy wiersz z datą t+1
- Predykcja jest oznaczona innym kolorem
- Widoczny jest przedział ufności 95%

### Test A3: Reset stanu po wczytaniu nowych danych

Warunki początkowe:

- Wykonano co najmniej jedną predykcję

Kroki:

- Użytkownik ponownie wczytuje nowy plik CSV
- Aplikacja czyści poprzednie predykcje

Oczekiwany rezultat:

- Licznik predykcji zostaje zresetowany
- Czas predykcji zostaje wyczyszczony
- Wykres pokazuje wyłącznie nowe dane

### Test A4: Eksport wykresu

Warunki początkowe:

- Wykres jest widoczny w aplikacji

Kroki:

- Użytkownik klika przycisk „Eksport wykresu”
- Wybiera lokalizację zapisu pliku

Oczekiwany rezultat:

- Plik PNG z wykresem zostaje zapisany na dysku
- Wykres w pliku odpowiada aktualnemu widokowi aplikacji

