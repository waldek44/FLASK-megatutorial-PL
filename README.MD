# FLASK MEGATUTORIAL PL

> Na podstawie tutoriala https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

### 1. Hello World

1. Instaluję Flask `pip install Flask`

2. Tworzę package (katalog app z plikiem __init__.py)
> Podkatalog zawierający plik **__init__.py** jest traktowany jako pakiet i można go zaimportować.
> Skrypt w **__init__.py** tworzy obiekt app jako instancję klasy Flask importowaną z pakietu flask. 

3. Tworzę moduł widoków (plik routes.py w katalogu app)

4. Aby ukończyć aplikację, musisz mieć skrypt Python na najwyższym poziomie, który definiuje instancję aplikacji Flask. 
Nazywam ten skrypt **microblog.py** i definiuję go jako pojedynczą linię, która importuje instancję **app**

5. W teminalu ustawiam zmienną środowiskową FLASK_APP aby Flask wiedział, jak zaimportować aplikację `set FLASK_APP=microblog.py`.
Aby nie wykonywać tego za każdym razem instaluję pakiet `pip install python-dotenv` i tworzę plik **.flaskenv** w którym
ustawiam zmienne środowiskowe.

### 2. TEMPLATES
> W Flask szablony są zapisywane jako osobne pliki, przechowywane w folderze szablonów templates, wewnątrz pakietu app. 

1. W katalogu app tworzę katalog **templates**, w którym będą przechowywane szablony

2. W **templates** robię **index.html**

3. W **routes.py** renderuję szablon **index.html** za pomocą funkcji **render_template()**

4. Dodaję szablon bazowy **base.html** który dziedziczę w **index.html**

### 3. WEB FORMS

1. Instaluję rozszerzenie obsługi formularzy internetowych **Flask-WTF**
```
pip install flask-wtf
```

2. Tworzę nowy moduł **config.py** do zarządzania konfiguracją aplikacji

3. Gdy mam plik konfiguracyjny, muszę powiedzieć Flaskowi, by go przeczytał i zastosował. 
Robię to za pomocą metody **app.config.from_object()** w **__init.py__**

4. Tworzę nowy moduł **app/forms.py** do przechowywania moich klas formularzy internetowych.
Klasa formularza po prostu definiuje pola formularza jako zmienne klasy.

5. Dodaję formularz do szablonu HTML. Tworzę **app/templates/login.html**

6. Teraz zanim zobaczę ten formularz w przeglądarce, muszę dodać funkcję widoku, która renderuje szablon w **app/routes.py**.

> Metoda `form.validate_on_submit( )` wykonuje wszystkie operacje przetwarzania formularzy. Kiedy przeglądarka wyśle 
>żądanie GET, aby otrzymać stronę internetową z formularzem, ta metoda zwróci False, w takim przypadku funkcja pominie 
>instrukcję if i przejdzie bezpośrednio do renderowania szablonu w ostatnim wierszu funkcji. 

>Kiedy przeglądarka wysyła żądanie POST w wyniku naciśnięcia przez użytkownika przycisku "Wyślij", 
> `form.validate_on_submit( )` zbierze wszystkie dane, uruchomi wszystkie walidatory dołączone do pól, a jeśli wszystko
> jest w porządku, zwróci True, wskazujące, że dane są poprawne i mogą być przetwarzane przez aplikację. 
>Ale jeśli co najmniej jedno pole nie przejdzie procesu sprawdzania poprawności, funkcja zwróci False, co spowoduje 
> powrót formularza do użytkownika, jak w przypadku żądania GET.  

> Gdy `form.validate_on_submit( )` zwraca True, funkcja widoku logowania wywołuje dwie nowe funkcje, zaimportowane z Flask. 
>Funkcja **redirect( )** nakazuje przeglądarce klienta automatyczne przejście do innej strony, podanej jako argument.
> Funkcja **flash( )** to przydatny sposób wyświetlania wiadomości użytkownikowi. Kiedy wywołujesz funkcję **flash( )**,
> Flask przechowuje wiadomość, ale błyskające wiadomości nie pojawiają się magicznie na stronach internetowych. 
> Szablony aplikacji muszą renderować te komunikaty w sposób, który działa w układzie strony.

7. Dodaję link do strony logowania w **app/templates/base.html** oraz instrukcję with dla wiadomości flash implementującą
 funkcję **get_flashed_messages()**
 
 8. W szablonie logowania **app/templates/login.html** dodaję walidatory. W rzeczywistości weryfikatory w **forms.py** 
 generują już opisowe komunikaty o błędach, więc brakuje tylko dodatkowej logiki w szablonie, aby je renderować.
 
 9. używam funkcji **Url_for( )** do przekierowań w **app/templates/base.html**
> Formularz logowania jest kompletny. Warto jeszcze tylko zmienić sposób umieszczania linków w szablonach i przekierowaniach.
> Aby mieć lepszą kontrolę nad tymi łączami, Flask dostarcza funkcję **url_for( )**, która generuje adresy URL za pomocą
> wewnętrznego mapowania adresów URL do przeglądania funkcji. 