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

###### 8 

Generuję nową migrację bazy danych dla Post
```
flask db migrate -m "posts table"
```
Migracja musi być wygenerowana do bazy danych
```
flask db upgrade
```

<hr>

###### 9
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

###### 10
Konfiguruję powłokę shell za pomocą funkcji w **mikroblog.py**
> Polecenie **flask shell** uruchomi interpreter Pythona w kontekście aplikacji. Polecenie to uruchamia powłokę Python i
> wstępnie importuje instancję aplikacji **app**. Zaletą powłoki **flask shell** nie jest to, że app jest wstępnie 
> importowana, tylko, że można skonfigurować "kontekst powłoki", który jest listą innych symboli do importu wstępnego.

