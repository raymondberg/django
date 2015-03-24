__author__ = 'rberg'
from partymaker.models import Neighborhood, Animal, AnimalRating
import random

class PartyMakerGenerator:
    neighborhoods = ["Albany Park","Andersonville","Avondale","Beverly","Boystown","Bridgeport",
    "Bronzeville","Chinatown","Edgewater","Gold Coast","Humboldt Park","Hyde Park","Irving Park",
    "Jefferson Park","Kenwood","Lakeview","Lincoln Park","Lincoln Square","Little Italy & University Village",
    "Little Village","Logan Square","Loop","Magnificent Mile","North Center","North Park","Old Town",
    "Pilsen","Portage Park","Pullman","River North","Rogers Park","Roscoe Village","South Loop","South Shore",
    "Streeterville","Uptown","West Loop","West Ridge","West Town","Wicker Park / Bucktown","Wrigleyville"]

    first_names = ["Edgardo","Terina","Angelica","Eustolia","Kassandra","Truman","Denise","Kathlene",
    "Linnie","Yolande","Gregg","Winnifred","Kirsten","Emelda","Fritz","Hector","Lue","Ed","Valene",
    "Inge","Bart","Kyla","Matt","Ben"]

    last_names = ["Sandavol","Westgate","Harward","Wojcik","Devino","Macbeth","Murton","Barahona",
      "Cranfill","Spiegel","Lembke","Hamler","Mullican","Lepore","Rockhill","Hammack",
      "Rosborough","Dearborn","Trentham","Heuser","Mayhugh","Folkerts","Greggs","Soriano"]

    @staticmethod
    def generateNeighborhoods():
        for neighborhood in PartyMakerGenerator.neighborhoods:
            Neighborhood(name=neighborhood).save()

    @staticmethod
    def generateAnimals(amount=256,withNeighborhoods=True):
        for i in range(0,amount):
            fname = PartyMakerGenerator.first_names[random.randrange(0,len(PartyMakerGenerator.first_names))]
            lname = PartyMakerGenerator.last_names[random.randrange(0,len(PartyMakerGenerator.last_names))]
            number = "%d-%d-%d" % \
                (random.randrange(100,999),random.randrange(100,999),random.randrange(1000,9999)) #stupid number generator
            email = "%s.%s@example.com" % (fname.lower(), lname.lower())
            Animal(first_name=fname, last_name=lname, phone=number, email=email).save()

    @staticmethod
    def assignAnimalsNeighborhoods():
        neighborhoods = Neighborhood.objects.all()
        for animal in Animal.objects.all():
            animal.neighborhood = neighborhoods[random.randrange(0,len(neighborhoods))]
            animal.save()

    @staticmethod
    def rateAnimals():
        animals = Animal.objects.all()
        for i in range(0,len(animals)):
            print "Processing ratings for %d / %d" % (i, len(animals))
            center = random.randrange(0,9)
            for j in range(0,len(animals)):
                if i == j or random.randint(0,10) != 1:
                    continue
                deviation = random.randrange(-2,2)
                actual = min(max(0, center + deviation), 9)
                animals[i].rate(animals[j], actual)