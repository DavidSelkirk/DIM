# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from MapEntity import *
import TileMap

def index(request):
        # select the appropriate template to use
        template = loader.get_template('terror/index.html')
        # create and define the context. We don't have any context at the moment
        # but later on we will be putting data in the context which the template engine
        # will use when it renders the template into a page.
        context = RequestContext(request, {})
        # render the template using the provided context and return as http response.
        return HttpResponse(template.render(context))

def game(request):
        # select the appropriate template to use
        template = loader.get_template('terror/game.html')
        # create and define the context. We don't have any context at the moment
        # but later on we will be putting data in the context which the template engine
        # will use when it renders the template into a page.
	#create the TileMap
	tilemap = TileMap.TileMap("/users/level3/1003646s/work/DIM3/DIM/terror_in_project/terror/Map.txt")
	player = Player(1)
	zombie = Zombie(1, 1, 3)
	tilemap.populateMap(player, zombie)
	tiles = tilemap.tiles
        context = RequestContext(request, {'tiles' : tiles})
        # render the template using the provided context and return as http response.
        return HttpResponse(template.render(context))
