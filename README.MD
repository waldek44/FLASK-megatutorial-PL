# FLASK MEGATUTORIAL PL

> Na podstawie tutoriala https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

## 1. Hello World

###### 1. 
Instaluję Flask `pip install Flask`

<hr>

###### 2. 
Tworzę package (katalog app z plikiem __init__.py)
> Podkatalog zawierający plik **__init__.py** jest traktowany jako pakiet i można go zaimportować.
> Skrypt w **__init__.py** tworzy obiekt app jako instancję klasy Flask importowaną z pakietu flask. 

<hr>

###### 3. 
Tworzę moduł widoków (plik routes.py w katalogu app)

<hr>

###### 4. 
Aby ukończyć aplikację, musisz mieć skrypt Python na najwyższym poziomie, który definiuje instancję aplikacji Flask. 
Nazywam ten skrypt **microblog.py** i definiuję go jako pojedynczą linię, która importuje instancję **app**

<hr>

###### 5. 
W teminalu ustawiam zmienną środowiskową FLASK_APP aby Flask wiedział, jak zaimportować aplikację `set FLASK_APP=microblog.py`.
Aby nie wykonywać tego za każdym razem instaluję pakiet `pip install python-dotenv` i tworzę plik **.flaskenv** w którym
ustawiam zmienne środowiskowe.

## 2. TEMPLATES
> W Flask szablony są zapisywane jako osobne pliki, przechowywane w folderze szablonów templates, wewnątrz pakietu app. 


###### 1. 
W katalogu app tworzę katalog **templates**, w którym będą przechowywane szablony

<hr>

###### 2. 
W **templates** robię **index.html**

<hr>

###### 3.
W **routes.py** renderuję szablon **index.html** za pomocą funkcji **render_template()**

<hr>

###### 4. 
Dodaję szablon bazowy **base.html** który dziedziczę w **index.html**

## 3. WEB FORMS

###### 1. 
Instaluję rozszerzenie obsługi formularzy internetowych **Flask-WTF**
```
pip install flask-wtf
```

<hr>

###### 2. 
Tworzę nowy moduł **config.py** do zarządzania konfiguracją aplikacji

<hr>

###### 3. 
Gdy mam plik konfiguracyjny, muszę powiedzieć Flaskowi, by go przeczytał i zastosował. 
Robię to za pomocą metody **app.config.from_object()** w **__init.py__**

<hr>

###### 4. 
Tworzę nowy moduł **app/forms.py** do przechowywania moich klas formularzy internetowych.
Klasa formularza po prostu definiuje pola formularza jako zmienne klasy.

<hr>

###### 5. 
Dodaję formularz do szablonu HTML. Tworzę **app/templates/login.html**

<hr>

###### 6. 
Teraz zanim zobaczę ten formularz w przeglądarce, muszę dodać funkcję widoku, która renderuje szablon w **app/routes.py**.

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

<hr>

###### 7. 
Dodaję link do strony logowania w **app/templates/base.html** oraz instrukcję with dla wiadomości flash implementującą
 funkcję **get_flashed_messages()**
 
 <hr>

###### 8. 
W szablonie logowania **app/templates/login.html** dodaję walidatory. W rzeczywistości weryfikatory w **forms.py** 
 generują już opisowe komunikaty o błędach, więc brakuje tylko dodatkowej logiki w szablonie, aby je renderować.
 
 <hr>

###### 9. 
Używam funkcji **Url_for( )** do przekierowań w **app/templates/base.html**
> Formularz logowania jest kompletny. Warto jeszcze tylko zmienić sposób umieszczania linków w szablonach i przekierowaniach.
> Aby mieć lepszą kontrolę nad tymi łączami, Flask dostarcza funkcję **url_for( )**, która generuje adresy URL za pomocą
> wewnętrznego mapowania adresów URL do przeglądania funkcji. 


## 4. DATABASES

###### 1. 
Instaluję **Flask-SQLAlchemy** które zapewnia przyjazne opakowanie Flask do popularnego pakietu **SQLAlchemy**, 
który jest Object Relational Mapper (ORM). 
```
pip install flask-sqlalchemy
```

Drugim rozszerzeniem, które instaluję jest **Flask-Migrate**. To rozszerzenie jest opakowaniem Flask dla Alembic
 (framework migracji baz danych dla SQLAlchemy). 
 ```
pip install flask-migrate
```

<hr>

###### 2. 
Konfiguruję **Flask-SQLAlchemy** do pracy z SQLLite. W pliku konfiguracyjnym **config.py** dodaję nowe elementy.


<hr>

###### 3. 
DB będzie reprezentowana w aplikacji przez instancję bazy danych. Silnik migracji bazy danych również będzie 
miał instancję. Są to obiekty, które należy utworzyć w pliku **app/__ init__.py**


<hr>

###### 4. 
Tworzę modele db
> Dane przechowywane w bazie danych, będą reprezentowane przez kolekcję klas, zwykle zwanych modelami baz danych.  
> Warstwa ORM w obrębie SQLAlchemy wykona tłumaczenia wymagane do odwzorowania obiektów utworzonych z tych klas 
> na wiersze w odpowiednich tabelach bazy danych.

Teraz, gdy wiem, czego chcę dla tabeli użytkowników, mogę przetłumaczyć to na kod w nowym module **app/models.py**

<hr>

###### 5. 
Tworzę repozytorium migracji dla mikroblogu, uruchamiając:
```
flask db init
```
> Po uruchomieniu tego polecenia znajdę nowy katalog migracji, z kilkoma plikami i podkatalogiem wersji w środku. 
>Wszystkie te pliki powinny być od teraz traktowane jako część projektu, powinny być dodawane do kontroli źródła.

<hr>

###### 6. 
Tworzenie pierwszą migrację bazy danych, która będzie zawierała tabelę użytkowników mapującą model bazy danych **User**.
> Istnieją dwa sposoby utworzenia migracji bazy danych: ręcznie lub automatycznie.   
> Aby automatycznie wygenerować migrację, Alembic porównuje schemat bazy danych zdefiniowany przez modele db z aktualnym 
> schematem bazy używanym obecnie w bazie danych. Następnie wypełnia skrypt migracji zmianami niezbędnymi w celu dostosowania
> schematu bazy danych do modeli aplikacji. W tym przypadku, ponieważ nie ma poprzedniej bazy danych, migracja automatyczna 
> doda cały model User do skryptu migracji.

```
flask db migrate -m "users table"
```

Komenda **flask db migrate** nie wprowadza żadnych zmian w bazie danych, a jedynie generuje skrypt migracji. 
Aby zastosować zmiany do bazy danych, należy użyć komendy 
```
flask db upgrade
```
> Ponieważ ta aplikacja używa SQLite, polecenie upgrade wykryje, że baza danych nie istnieje i utworzy ją (zauważysz, 
> że plik o nazwie app.db zostanie dodany po zakończeniu tego polecenia. Podczas pracy z serwerami baz danych, takimi jak
> MySQL i PostgreSQL, przed uruchomieniem polecenia upgrade( ) należy utworzyć bazę danych na serwerze.


<hr>

###### 7. 
Dodaję klasę Post w **app/models.py**

> Klasa User ma też 1 nowe pole **posts**, które jest inicjowane za pomocą db.relationship. To nie jest rzeczywiste 
> pole bazy danych, ale widok wysokiego poziomu relacji między użytkownikami i ich postami. W przypadku relacji jeden do 
> wielu, pole db.relationship jest zwykle zdefiniowane po stronie "jeden" i jest używane jako wygodny sposób uzyskania dostępu do "wielu". 
> Argument **backref** definiuje nazwę pola, które zostanie dodane do obiektów klasy "many", która wskazuje na "jeden" obiekt. 
> Spowoduje to dodanie wyrażenia post.author, które zwróci użytkownikowi dany wpis. argument **lazy** określa, 
> w jaki sposób zostanie wydane zapytanie o bazę danych relacji.

<hr>

###### 8.

Generuję nową migrację bazy danych dla Post
```
flask db migrate -m "posts table"
```
Migracja musi być wygenerowana do bazy danych
```
flask db upgrade
```

<hr>

###### 9.
Ponieważ aplikacja nie ma jeszcze żadnej logiki bazy danych, pobawmy się z bazą danych w interpreterze Pythona
```
flask shell
from app import db
from app.models import User, Post

u = User(username='waldek', email='waldek@example.com')
db.session.add(u)
db.session.commit()
```
> Zmiany w bazie danych są wykonywane w kontekście sesji, do której można uzyskać dostęp komendą **db.session**. 
> W sesji można gromadzić wiele zmian i po zarejestrowaniu wszystkich zmian można wydać pojedynczy **db.session.commit( )**, 
> który zapisuje wszystkie zmiany.  

> Jeśli w dowolnym momencie podczas pracy z sesją wystąpił błąd, wywołanie metody **db.session.rollback( )** spowoduje 
> przerwanie sesji i usunięcie wszelkich zapisanych w niej zmian. Ważną rzeczą do zapamiętania jest to, że zmiany są 
>zapisywane w bazie danych tylko po wywołaniu metody **db.session.commit( )**. 
> Sesje gwarantują, że baza danych nigdy nie pozostanie w niespójnym stanie.

Dodajmy kolejnego użytkownika:
```
u = User(username='susan', email='susan@example.com')
db.session.add(u)
db.session.commit()
```

Baza danych może odpowiedzieć na zapytanie (query) zwracające wszystkich użytkowników:
```
users = User.query.all()
users
```
Pobieram pierwszego usera i przypisuję mu nowy wpis na blogu:
```
one = User.query.get(1)
one 
p = Post(body='my first post!', author=one)
db.session.add(p)
db.session.commit()

posts = one.posts.all()
posts
```

Dokumentacja Flask-SQLAlchemy jest najlepszym miejscem do zapoznania się z wieloma opcjami dostępnymi do 
wysyłania zapytań do bazy danych. Aby ukończyć tę sekcję, usuń testowych użytkowników i posty utworzone powyżej, 
aby baza danych była czysta i gotowa do następnego rozdziału:
```
users = User.query.all()

for one in users:
...    db.session.delete(one)
...

posts = Post.query.all()
for p in posts:
...     db.session.delete(p)
...
db.session.commit()
```

<hr>

###### 10.
Konfiguruję powłokę shell za pomocą funkcji w **mikroblog.py**
> Polecenie **flask shell** uruchomi interpreter Pythona w kontekście aplikacji. Polecenie to uruchamia powłokę Python i
> wstępnie importuje instancję aplikacji **app**. Zaletą powłoki **flask shell** nie jest to, że app jest wstępnie 
> importowana, tylko, że można skonfigurować "kontekst powłoki", który jest listą innych symboli do importu wstępnego.

## 5. USERS LOGINS

###### 1.
Ok, Połączę formularz logowania z bazą danych.
> Jednym z pakietów, który implementuje hashowanie hasłem jest **Werkzeug**, które być może widzieliśmy w wynikach pip 
> podczas instalowania Flask, ponieważ jest to jedna z głównych zależności. Werkzeug jest już zainstalowany w twoim środowisku wirtualnym. 

Cała logika haszowania hasła może być zaimplementowana w **app/models.py** jako dwie nowe metody w modelu User:  
**set_password(self, password)** i **check_password(self, password)**  
Dzięki zastosowaniu tych dwóch metod obiekt klasy User może teraz bezpiecznie weryfikować hasła bez konieczności przechowywania oryginalnych haseł.  

<hr>

###### 2.
Rozszerzenie Flask o nazwie **Flask-Login** zarządza stanem zalogowania użytkownika, dzięki czemu na przykład użytkownicy 
mogą logować się do aplikacji, a następnie nawigować do różnych stron, gdy aplikacja "pamięta", że użytkownik jest zalogowany. 
Zapewnia także funkcję "zapamiętaj mnie", pozwalającą użytkownikom pozostać zalogowanym nawet po zamknięciu okna przeglądarki.
```
pip install flask-login
```

<hr>

###### 3.

**Flask-Login** musi zostać utworzony i zainicjowany zaraz po wystąpieniu aplikacji w **app/__ init__.py**.

<hr>

###### 4.

Flask-Login działa z modelem użytkownika aplikacji User i oczekuje, że zostaną w nim zaimplementowane określone właściwości i metody.

Cztery wymagane elementy są wymienione poniżej:  
**is_authenticated**: właściwość o wartości True, jeśli użytkownik ma prawidłowe poświadczenia lub False w przeciwnym razie.  
**is_active**: właściwość, która ma wartość True, jeśli konto użytkownika jest aktywne lub False w przeciwnym razie.  
**is_anonymous**: właściwość False dla zwykłych użytkowników i True dla specjalnego, anonimowego użytkownika.  
**get_id ()**: metoda, która zwraca unikalny identyfikator dla użytkownika jako string.  

Mogę łatwo wdrożyć te cztery elementy, ale ponieważ implementacje są dość ogólne, Flask-Login udostępnia klasę mixin o nazwie **UserMixin**, 
która zawiera ogólne implementacje, które są odpowiednie dla większości klas modeli użytkowników. 
Dodaję więc klasę **UserMixin** w **app/models.py**

<hr>

###### 5.
Rozszerzenie **Flask-Login** oczekuje, że aplikacja skonfiguruje funkcję ładującą użytkownika, którą można wywołać w celu 
załadowania użytkownika z danym identyfikatorem. Dlatego dodaję funkcję **load_user(id)** w module **app/models.py**

> Program ładujący użytkownika jest rejestrowany przez Flask-Login za pomocą dekoratora **@login.user_loader**. 
>Identyfikator, który Flask-Login przekazuje do funkcji jako argument, będzie ciągiem znaków, więc bazy danych, 
>które używają liczbowych identyfikatorów, muszą przekonwertować ciąg na liczbę całkowitą, jak widać powyżej.

<hr>

###### 6.
Teraz, gdy aplikacja ma dostęp do bazy danych użytkowników i wie, jak generować i weryfikować hashe hasła mogę 
zaimplementować logikę funkcji logowania użytkownika w **app/routes.py**

<hr>

###### 7.
Muszę zaoferować użytkownikom opcję wylogowania się z aplikacji. Można to zrobić za pomocą funkcji **logout_user( )** w **app/routes.py**.

Mogę spowodować, że link **Login** na pasku nawigacyjnym automatycznie przełączy się na link **logout** po zalogowaniu użytkownika. 
Można to zrobić warunkowo w szablonie **base.html** przy pomocy if oraz właściwości **is_anonymous**.
> **is_anonymous** jest jednym z atrybutów, które Flask-Login dodaje do obiektów użytkowników za pośrednictwem klasy UserMixin. 
> Wyrażenie **current_user.is_anonymous** będzie miało wartość True tylko wtedy, gdy użytkownik nie jest zalogowany.

<hr>

###### 8.
Wymaganie zalogowania.  
> Flask-Login posiada bardzo przydatną funkcję, która zmusza użytkowników do zalogowania się, zanim będą mogli obejrzeć określone strony aplikacji.
> Jeśli użytkownik, który nie jest zalogowany, spróbuje wyświetlić chronioną stronę, Flask-Login automatycznie przekieruje użytkownika 
> do formularza logowania i przekieruje z powrotem na stronę, którą użytkownik chciał zobaczyć po zakończeniu procesu logowania.

W **app/__ init__.py** określam jaka funkcja widoku obsługuje logowanie.

Flask-Login chroni funkcję widoku przed anonimowymi użytkownikami za pomocą dekoratora o nazwie **@login_required**, 
implementuję go pod dekoratorem **@app.route('/')** w pliku **app/routes.py**

<hr>

###### 9.

Implementuję przekierowanie z udanego logowania na stronę, do której użytkownik chciał uzyskać dostęp.
> Gdy użytkownik, który nie jest zalogowany, uzyskuje dostęp do funkcji widoku chronionej za pomocą @login_required , 
> dekorator przekieruje go do strony logowania, ale w tym przekierowaniu będzie zawierać dodatkowe informacje, 
> aby aplikacja mogła następnie powrócić do pierwszej strony.

Dlatego w funkcji logowania w **app/routes.py** dodaję to przekierowanie. Wtedy użytkownik po poprawnym zalogowaniu 
przejdzie do strony którą atakował zanim przekierowało go na /login

<hr>

###### 10.
WYŚWIETLENIE ZALOGOWANEGO UŻYTKOWNIKA W SZABLONACH.

Aplikacja ma teraz prawdziwych użytkowników, więc mogę teraz usunąć fałszywego użytkownika i rozpocząć pracę z prawdziwymi użytkownikami. 
Zamiast fałszywego użytkownika mogę użyć current_user w szablonie **app/templates/index.html** i usunąć zmienną user z **app/routes.py**  

Dodaję też jednego usera
```
u = User(username='susan', email='susan@example.com')
u.set_password('susan')
db.session.add(u)
db.session.commit()
```

<hr>

###### 11.

REJESTRACJA UŻYTKOWNIKA - tworzę formularz rejestracyjny.

Najpierw robię klasę formularza w **app/forms.py**

> Dodałem również dwie metody do tej klasy o nazwie **validate_username( )** i **validate_email( )**.  
> Gdy dodasz dowolne metody, które pasują do wzorca **validate_ <nazwa_pola>**, WTForms bierze je jako niestandardowe 
> weryfikatory i wywołuje je oprócz walidatorów giełdowych. W tym przypadku chcę się upewnić, że nazwa użytkownika i 
> adres e-mail wprowadzone przez użytkownika nie znajdują się już w bazie danych, więc te dwie metody powodują zapytania 
> do bazy danych, oczekując, że nie będzie żadnych wyników. W przypadku wyniku występuje błąd sprawdzania poprawności 
> poprzez podniesienie błędu ValidationError. Komunikatem zawartym jako argument w wyjątku będzie komunikat wyświetlany 
> obok pola, aby użytkownik mógł go zobaczyć.


<hr>

###### 12.

Robię szablon HTML do rejestrowania w pliku **app/templates/register.html**

<hr>

###### 13.

Dodaję link do rejestracji w szablonie logowania **app/templates/login.html**

<hr>

###### 14.

Na koniec muszę napisać funkcję widoku, która będzie obsługiwać rejestracje użytkowników w **app/route.py**

<hr>

###### 15.
Instaluję email_validator dla pola walidavji Email dodanego w **forms.py**
```
pip install email_validator
```


## 6. PROFILE PAGE & AVATARS

###### 1
Aby utworzyć stronę profilu użytkownika, napiszĘ najpierw nową funkcję widoku **app/routes.py**, która mapuje na adres URL na **/user/<nazwa użytkownika>**

<hr>

###### 2.

Tworzę szablon **app/templates/user.html**

<hr>

###### 3.

Dodaję link do Profilu użytkownika w **app/templates/base.html**

<hr>

###### 4.

Korzystam z **Gravatar** aby dodać awatara użytkownikowi

Ponieważ awatary są powiązane z użytkownikami, sensowne jest dodanie logiki, która generuje adresy URL awatarów do modelu użytkownika w **app/models.py**

<hr>

###### 5.

Następnym krokiem jest wstawienie obrazów awatara do szablonu profilu użytkownika **app/templates/user.html**

<hr>

###### 6. 

**PODTEMPLATKI JINJA2**
> Zaprojektowałem stronę **user.html**, aby wyświetlała posty napisane przez użytkownika wraz z ich awatarami. 
> Teraz chcę, aby strona **index.html** wyświetlała również posty o podobnym układzie. Mógłbym po prostu skopiować / wkleić część szablonu, 
> która dotyczy renderowania postu, ale to naprawdę nie jest idealne, ponieważ później, jeśli zdecyduję się wprowadzić zmiany w tym układzie, 
> będę musiał pamiętać o zaktualizowaniu obu szablonów.

Zamiast tego utworzę pod-szablon, który renderuje tylko jeden post, a następnie odwołam się do niego zarówno z szablonów **user.html**, jak i **index.html**.
Na początek mogę utworzyć pod-szablon, używając tylko znaczników HTML dla jednego posta. 
Nazwę ten szablon **app/templates/_post.html**. Przedrostek **_** to tylko konwencja nazewnictwa, która pomaga mi rozpoznać, które pliki szablonów są pod-szablonami.

Aby wywołać ten pod-szablon w **user.html**, używam instrukcji dołączania (**include**) Jinja2

Strona **index.html** aplikacji nie jest jeszcze tak rozbudowana, więc nie zamierzam jeszcze dodawać tej funkcji.

<hr>

###### 6. 

Rozszerzam profil użytkownika o dodawanie informacji "o mnie" i śledzenie, kiedy ostatni raz użytkownik wszedł na stronę.

Rozszerzam w **app/models.py** tabelę użytkowników **Users** w bazie danych o dwa nowe pola, po czym migruję:
```
flask db migrate -m "new fields in user model"
flask db upgrade
```

W następnym kroku dodam te dwa nowe pola do szablonu profilu użytkownika **app/templates/user.html**

<hr>

###### 7. 

REJESTROWANIE OSTATNIEJ WIZYTY UŻYTKOWNIKA
Dodaję funkcję **before_request()** do **app/routes.py**

> Dekorator @before_request firmy Flask rejestruje dekorowaną funkcję, która ma zostać wykonana tuż przed funkcją widoku. 
> Jest to niezwykle przydatne, ponieważ teraz mogę wstawić kod, który chcę wykonać przed jakąkolwiek funkcją widoku w aplikacji, 
> i mogę mieć go w jednym miejscu. Implementacja po prostu sprawdza, czy użytkownik bieżący jest zalogowany, i w 
> takim przypadku ustawia pole last_seen na bieżącą godzinę.

> Ostatnim krokiem jest zatwierdzenie sesji bazy danych, aby powyższa zmiana została zapisana w bazie danych. 
> Jeśli zastanawiasz się, dlaczego przed zatwierdzeniem **db.session.commit ()** nie ma funkcji **db.session.add ()**, weź pod uwagę,
> że odwołując się do current_user, Flask-Login wywoła funkcję zwrotną modułu ładującego użytkownika, która uruchomi zapytanie
> do bazy danych, które wprowadzi docelowego użytkownika sesji bazy danych. Możesz więc ponownie dodać użytkownika w tej funkcji,
> ale nie jest to konieczne, ponieważ już tam jest.

<hr>

###### 8. 

EDYTOR PROFILU
> Muszę też dać użytkownikom formularz, w którym mogą wprowadzić informacje o sobie. Formularz pozwoli użytkownikom na zmianę 
>nazwy użytkownika, a także napisanie o sobie czegoś, co zostanie zapisane w nowym polu **about_me**. 

Dodaję formularz edycji profilu użytkownika w **app/forms.py**

<hr>

###### 9. 

Tworzę szablon renderujący ten formularz **app/templates/edit_profile.html**

<hr>

###### 10. 

I na koniec funkcja widoku w **app/routes.py**, która łączy wszystko razem 

<hr>

###### 11. 

Aby ułatwić użytkownikom dostęp do strony edytora profilu, mogę dodać link na stronie profilu **app/templates/user.html**

