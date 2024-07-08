# C'est le projet de l'emploi du temps

Installations:

```bash
$ git clone https://github.com/AdoumMahadi/Emploi_Project.git
$ cd Emploi_Project
```

Créé un environnement virtuel:

```bash
$ python3 -m venv .venv
```

Déplace toi dans le dossier de ton environnement virtuel et active ton environnement virtuel:

```bash
$ cd .venv && source bin/activate
```

Install les dépendances pour ce projet avec cette commande:

```bash
$ pip install -r requirements.txt
```

Avant de lancer le serveur il faut faire les migrations:
- NB: Assure toi que tu es dan sle dossier qui contient le fichier ```manage.py```
```bash
(.venv)users@lenovo:~/Matar_project/Matar$ python manage.my makemigrations
```
Aussi

```bash
(.venv)users@lenovo:~/Matar_project/Matar$ python manage.my migrate
```

Lance le serveur de django avec cette commande:

```bash
(.venv)users@lenovo:~/Matar_project/Matar$ python manage.py runserver 8000
```

Pour se logger au panel d'administration à l'url http://127.0.0.1:8000/admin/ , il faut créer un superuser
Voici la commande:

```bash
(.venv)users@lenovo:~/Matar_project/Matar$ python manage.py creatsuperuser
```