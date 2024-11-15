### Opis aplikacji
Aplikacja odczytuje przykładowy artykuł zapisany w pliku tekstowym, następnie w celu obróbki wraz z odpowiednim promptem(uwzględniającym odpowiednie wymagania) oraz treścią artykułu są przekazywane do OpenAi(wykorzystując w tym celu API OpenAi). Następnie, otrzymany od OpenAi kod html jest zapisywany w pliku artykul.html.
W pliku szablon_i_podglad.html znajduje się szablon, który może zostać wykorzystany do podglądu wygenerowanego artykułu po wlejeniu jego treści do sekcji <body>. Dodatkowo w tym pliku znajduje się także pełny podgląd przetworzonego artykułu.

### Opis uruchomienia aplikacji
* ### Sklonowanie repozytorium:
```
git clone https://github.com/lukaszlegenc/ZadanieRekrutacyjne.git
```
* ### Instalacja odpowiednich bibliotek:
W przypadku tej aplikacji konieczna jest instalacja biblioteki openai (wersja biblioteki: openai==1.54.4)
```
pip install openai
```
* ### Wpisanie w pliku .py w miejsce openai.api_key = '<API_KEY>' własnego klucza do API OpenAi
* ### Uruchomienie aplikacji w celu wygenerowania artykułu
