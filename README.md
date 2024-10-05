# Elastic Stack
__🚧 Dépôt en cours de construction 🚧__  
***
🇫🇷 _Workshops sur l'utilisation de Elasticsearch, Kibana et Logstash._  
_Dans le cadre de la formation de développeur IA, nous avons réalisé une veille sur Elastic Stack.  
Celle-ci s'accompagne de deux workshops faits sous Windows 11.  _

## Workshop 1 : Elasticsearch / Kibana
### DockerDesktop
_Sous Docker, il est beaucoup plus simple d'installer les éléments de Elastic Stack à l'aide d'un script __docker-compose.yml__. Dans une optique pédagogique, je préfère vous indiquer et donc utiliser les instructions fournies par Docker dans une CLI._

1. Télécharger et installer DockerDesktop via [le site de Docker](https://www.docker.com/products/docker-desktop/)
> [!IMPORTANT]  
> _Dans notre cas - sous Windows - Docker ne pouvait démarrer qu'en tant qu'Administrateur._  

2. Sous la console Windows ou celle directement intégrée à DockerDesktop, __créer un réseau avec Docker__ _(ici nommé "elastic-net")_ : 
```ruby
docker network create elastic-net
```
3. Récupérer l'__image Elasticsearch__ _(version 8.15.2 par exemple)_ :
```ruby
docker pull docker.elastic.co/elasticsearch/elasticsearch:8.15.2
```
4. Créer un __conteneur Elasticsearch__ _(ici nommé "es01")_ sur le réseau _elastic-net_ à l'aide de l'image précédemment fournie :
```ruby
docker run --name es01 --net elastic -p 9200:9200 -it -m 1GB docker.elastic.co/elasticsearch/elasticsearch:8.15.2
```
5. Le CLI vous fournit un mot de passe pour l'utilisateur nommé __elastic__ ainsi qu'un token pour l'utilisation de Kibana.
> [!TIP]
> Tentez de vous connecter à [http://localhost:9200](http://localhost:9200) en tant que l'utilisateur __elastic__ avec le mot de passe fourni.  
> Si vous y parvenez, c'est que le service d'Elastisearch est bien présent sur votre réseau local sous le port 9200.

### Requêtes
Requêtes effectuées via code python _main.py_

## Workshop 2 : Utilisation d'un dataset

🇬🇧 _Workshops on the use of Elasticsearch, Kibana and Logstash_
