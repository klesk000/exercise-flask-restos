# Exercice Flask

## Créez une API Flask

Avec juste deux routes pour commencer :

- `/api/`
- `/api/restos/`


### La route `/api/`

Cette route doit représenter "la home" de l'API, c'est à dire donner
les informations intéressantes à propos de l'API, au strict minimum un
lien vers `/api/restos`

```json
{
    "restos": "/api/restos"
}
```

Pour aller plus loin regarder [json-home](https://mnot.github.io/I-D/json-home/).


### La route `/api/restos`

Cette route doit accepter un argument `q` pour chercher, par exemple,
un restaurant par ville :

```
GET /api/restos/?q=Tignes
```

Le document renvoyer doit être un objet json contenant au minimum un
attribut `items` contenant des restaurants sous la forme d'un nœud OSM :

```json
{
    "changeset": 2159133,
    "id": 468716078,
    "lat": 45.4674066,
    "lon": 6.9026969,
    "tags": {
        "amenity": "restaurant",
        "name": "Le Chardonnet"
    },
    "timestamp": "2009-08-15T23:34:57Z",
    "type": "node",
    "uid": 87991,
    "user": "andygates",
    "version": 1
    }
}
```


## Requêter OSM

Pour faire des requêtes sur OSM vous pouvez utiliser
[overpass](https://wiki.openstreetmap.org/wiki/Overpass).

Pour tester vos requêtes, utilisez [overpass
turbo](https://overpass-turbo.eu/), par exemple, pour trouver les
restaurants à Tignes, utilisez cette requête :

=> https://overpass-turbo.eu/s/156z

OSM est un projet libre, les serveurs overpass sont hébergés par la
communauté, et les requêtes parfois gourmandes, nous allons donc
réduire au strict minimum le nombre de requêtes effectuées en les
cachant au maximum, dès le début du projet.

Le langage overpass vous permet de préciser que vous souhaitez une
réponse JSON, ainsi, en utilisant la bibliothèque `requests` de
Python, il est possible de faire une requête smplement via :

```python
response = requests.post(
    "https://lz4.overpass-api.de/api/interpreter",
    f"""[out:json];area[name="{city}"];node["amenity"="restaurant"](area);out meta;""".encode("UTF-8")
)
```

Mais dans un premier temps, je vous ai fait la requête pour Tignes et
l'ai stockée ici : https://mdk.fr/x/tignes.json vous pouvez donc
l'utiliser dans votre code durant la phase de développement (pour
réduire au maximum nos appels aux API overpass).


## Le HTML / JS / CSS

Il y a deux écoles :

- Soit vous le faite dans Flask, avec des templates en Jinja2 dans le
  dossier `templates/` et vos css et js dans le dossier `static/`.
- Soit vous le faite complètement à part, avec vos outils habituels,
  de toute façons le front est entièrement décorrélé du back.
