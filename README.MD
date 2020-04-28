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
