def example():
    things = ['a', 'b', 'c', 'd']
    print things[1]
    things[1] = 'z'
    print things[1]
    print things
    stuff = {'name': 'Zed', 'age': 39, 'height': 6 * 12 + 2}
    print stuff['name']
    print stuff['age']
    print stuff['height']
    stuff['city'] = 'San Francisco'
    print stuff['city']
    stuff[1] = "Wow"
    stuff[2] = "Neato"
    print stuff[1]
    print stuff[2]
    print stuff
    del stuff['city']
    del stuff[1]
    del stuff[2]
    print stuff
example()

def dict_example():
# creates a mapping of states to abbreviations
    states = {
        'Oregon': 'OR',
        'Florida': 'FL',
        'California': 'CA',
        'New York': 'NY',
        'Michigan': 'MI'
    }

# creates a basic set of states and some cities in them
    cities = {
        'CA': 'San Francisco',
        'MI': 'Detroit',
        'FL': 'Jacksonville',
    }

# add more cities
    cities['NY'] = 'New York'
    cities['OR'] = 'Portland'

# print out some cities
    print '-' * 10
    print "NY State has: ", cities['NY']
    print "OR State has: ", cities['OR']

# print out some states
    print '-' * 10
    print "Michigan's abbreviation is: ", states['Michigan']
    print "Florida's abbreviation is: ", states['Florida']

# print every state abbreviation
    print "-" * 10
    for state, abbrev in states.items():
        print "%s is abbreviated as %s" % (state, abbrev)

# print every city in state
    print '-' * 10
    for abbrev, city in cities.items():
        print "%s has the city %s" % (abbrev, city)

# now do both at the same time
    print '-' * 10
    for state, abbrev in states.items():
        print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

    print '-' * 10
    # safely get an abbreviation by state that might not be there
    state = states.get('Texas')

    if not state:
        print "Sorry, no Texas."
# get a city with a default value
    city = cities.get('TX', 'Does Not Exist')
    print "The city for the state 'TX' is: %s" % city
dict_example()
