## 1.	Charakterystyka oprogramowania

Nasza aplikacja nazywa się Crypto Oracle Analytics - w skrócie - COA.

Nasza aplikacja służy do prognozowania cen kryptowalut z wykorzystaniem modelu ARIMA. System analizuje historyczne dane cenowe (kursy zamknięcia), identyfikuje zależności czasowe i na ich podstawie generuje krótkoterminowe (jednodniowe) predykcje wraz z związanymi z tymi predykcjami niepewnościami. Wyniki prezentowane są w czytelnej formie wykresów i prognoz.
Celem COA jest dostarczenie użytkownikom prostego, ale solidnego narzędzia prognostycznego opartego na klasycznej metodzie statystycznej, które wspiera podejmowanie świadomych decyzji inwestycyjnych. Aplikacja ma ponadto na celu pokazanie praktycznego zastosowania modelu ARIMA w analizie finansowych szeregów czasowych.

## 2.	Prawa autorskie
Autorami aplikacji są: Natalia Kurczyńska, Łukasz Filipkowski.

Zdecydowaliśmy się na jedną z licencji *Common Creative*, a konkretnie na licencję “Użycie niekomercyjne” (ang. Noncommercial). Wybrana licencja pozwala na kopiowanie, rozpowszechnianie oraz publiczne udostępnianie utworu objętego prawem autorskim, a także na tworzenie opracowań i utworów zależnych, pod warunkiem, że są one wykorzystywane wyłącznie w celach niekomercyjnych.

Zdecydowaliśmy się na tą licencję, ponieważ chcieliśmy umożliwić swobodne korzystanie z projektu, szczególnie w celach edukacyjnych i badawczych, przy jednoczesnym zabezpieczeniu go przed wykorzystaniem komercyjnym. Dzięki temu projekt może być dalej rozwijany i wykorzystywany przez inne osoby, bez ryzyka jego komercyjnego użycia.

## 3. Specyfikacja wymagań

|ID | NAZWA | OPIS | PRIORYTET | KATEGORIA |
|---|-------|------|-----------|-----------|
|F-01|Wybór kryptowaluty| Użytkownik może wybrać kryptwalutę, dla której zostanie wykonana analiza.|1|Funkcjonalne - Dobór danych|
|F-02|Wizualizacja danych historycznych| Aplikacja umozliwia użytkownikowi sprawdzenie zmienności cen kryptowalut we wskazanym okresie.|1|Funkcjonalne - Wizualizacja|
|F-03|Generowanie prognozy| Po wybraniu kryptowaluty przez użytkownika, aplikacja wyświetli prognozę ceny tej kryptowaluty na następny dzień.|1| Funkcjonalne - Prognozowanie|
|F-04|Zwizualizowanie prognozy| Użytkownik będzie miał możliwość zobaczenia na wykresie wygenerowanej wartości prognozy wraz z wyznaczonym dla niej przedziałem ufności.|1|Funkcjonalne - Wizualizacja|
|F-05|Eksport wykresów|Użytkownik ma możliwość zapisania wykresów po ich wygenerowaniu.|2|Funkcjonalne - Eksport|
|F-06|Czytelny interfejs|Korzystanie z aplikacji jest dla użytkownika intuicyjne; interfejs aplikacji jest czysty.|1|Niefunkcjonalne|
|F-07|Czas oczekiwania|Czas oczekiwania na odpowiedź aplikacji jest krótki, prognoza pojawia się na ekranie w zaledwie kilka sekund po wysłaniu zapytania.|1|Niefunkcjonalne|

(Priorytet: 1 - wymagane, 2 - przydatne, 3 - opcjonalne)

## 4. Architektura systemu/oprogramowania

Architektura rozwoju

|Technologia|Przeznaczenie|Nr wersji|
|-----------|-------------|---------|
|Python|Język programowania|3.14|
|Spyder|IDE do programowania w Pythonie| 5.4.1|
|Git|Kontrola wersji|2.52|
|GitHub|Hosting repozytorium|-|
|Biblioteka "pandas"|Analiza danych|2.3.3|
|Biblioteka "statsmodels"|Model ARIMA|0.14.6|
|Biblioteka "tkinter"|Graficzny interfejs użytkownika|8.6|
|Biblioteka "matplotlib"|Wizualizacja danych|3.10.0|
|Biblioteka "os"|Interakcja z systemem operacyjnym"|3.14 (jak Python)|
|Biblioteka "time"|Obsługa i mierzenie czasu|3.14 (jak Python)|
|Biblioteka "datatime"|Praca z datami i czasem|3.14 (jak Python)|

Architektura uruchomieniowa

|Technologia|Przeznaczenie| Nr wersji|
|-----------|-------------|----------|
|Python|Uruchamianie aplikacji|3.14|
|Wymagane biblioteki z architektury rozwoju|Możliwość pracy z aplikacją|-|

## 5. Testy

Scenariusze testów:

1. Test działania GUI:
    - Uruchomienie aplikacji
    - Wybranie kryptowaluty
    - Wygenerowanie prognozy
    - Srawdzenie wykresu
    - Zapisanie wykresów






