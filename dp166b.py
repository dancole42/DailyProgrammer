from math import pi
#from nihilio import creatio

ourUniverse = True
if ourUniverse: G = 6.67e-11

class CosmicBody(object):    
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __repr__(self):
          return "%s" % (self.name)

class World(CosmicBody):
    def __init__(self, name, radius, density):

      def rdmass(radius, density):
        """Returns a mass in kg from a radius in
        meters and a density in kg per cubic meter."""
        volume = (4.0 / 3) * pi * radius ** 3
        return volume * density

      self.radius = radius  # meters
      self.density = density    # kg / m ** 3
      CosmicBody.__init__(self, name, rdmass(radius, density))
      self.hasIntelligentLife = False    

class Astronaut(CosmicBody):
    def __init__(self, name = "Neil", mass = 75):
      CosmicBody.__init__(self, name, mass)

class Unit(object):
    def __init__(self, name, toNewtons):
        self.name = name
        self.toNewtons = toNewtons

    def __repr__(self):
        return "%s" % (self.name)

    def convert(self, newtons):
        """Converts to Unit from newtons"""
        return newtons / self.toNewtons

def reddit_cleanup(reddit_input):
    """Turns a comma-delimited text input into a dictionary
    where the key is a string and the values are lists of integers."""
    fieldRecord = rowName = ''
    fieldNumber = id = 0
    row = []
    reddit_clean = {}
    reddit_input = reddit_input.replace(' ', '')
    for i in reddit_input:
        fieldRecord += i
        if i == ',':
            fieldRecord = fieldRecord.rstrip(',')
            if fieldNumber == 0:
                rowName = fieldRecord
                reddit_clean[rowName] = ''
                id += 1
            else:
                row.insert(1, int(fieldRecord))
                reddit_clean[rowName] = row
            fieldRecord = ''
            fieldNumber += 1
        if '\n' in fieldRecord:
            fieldRecord = fieldRecord.rstrip('\n')
            row.insert(0, id)
            row.insert(1, int(fieldRecord))
            reddit_clean[rowName] = row
            fieldRecord = rowName = ''
            row = []
            fieldNumber = 0
    return reddit_clean

def worldBuilder(starstuff):
    """Turns a dictionary of raw material into sorted Planet objects."""
    worlds = []
    for i in starstuff:
        worlds.append((starstuff[i][0],World(i, starstuff[i][1], \
        starstuff[i][2])))
    worlds.sort()
    return worlds

def force(m1, m2, r):
    """Calculates force of attraction between two objects (m1, m2)
    at distance r."""
    force = G * ((m1 * m2) / r ** 2)
    return force

def getForce(World, Astronaut):
    """Calculates force of attraction between a planet and an astronaut."""
    return force(World.mass, Astronaut.mass, World.radius)

def forceReport(world, unit):
    """Prints the force of attraction between a planet and an astronaut."""
    weight = unit.convert(getForce(world[1], explorer))
    print "%s: %s" % (world[1], weight)

def underline(text):
    """Prints an underlined string."""
    print text
    text = text.split()
    for i in text:
        print '-' * len(i),
    print ''

def makeUnits():
    units = []
    lbs, newtons = Unit("pounds", 4.44822162825), Unit("newtons", 1) # Create units
    units.append(lbs)
    units.append(newtons)
    return units

"""To create an apple pie from scratch, one must first invent
the universe. -Carl Sagan"""

reddit_starstuff = reddit_cleanup("""Mercury, 2439700, 5427
Venus, 6051900, 5243
Earth, 6367445, 5515
Mars, 3386000, 3934
Jupiter, 69173000, 1326
Saturn, 57316000, 687
Uranus, 25266000, 1270
Neptune, 24553000, 1638
Pluto, 1173000, 2050
""")

solarsystem = worldBuilder(reddit_starstuff)    # Make the worlds.
explorer = Astronaut('dancole42', 75)   # Make me an astronaut to stand on the
                                        # worlds.
units = makeUnits() # Make some units of measurement.                        

# Print an astronaut's weight report.
for i in units:
    underline("Personal Weight Report for Astronaut %s (%s)" % (explorer.name, i))
    for world in solarsystem:
        forceReport(world, i)
    print ''