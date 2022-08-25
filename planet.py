"""
1 Mercury |  none                         |  0 No
2 Venus   |  Carbon Dioxide, Nitrogen  |  0 No
3 Earth   |  Nitrogen, Oxygen          |  1 No
4 Jupitor |  Hydrogen, Helium          |  79 Yes
5 Saturn  |  Hydrogen, Helium          |  83 Yes
6 Uranus  |  Hydrogen, Helium, Methane |  27 Yes
"""

planet_name = ["Mercury", "Venus", "Earth", "Jupitor", "Saturn", "Uranus"];
gasses = {
    "Mercury_gas" : "none",
    "Venus_gas1" : "Carbon Dioxide",
    "Venus_gas2" : "Nitrogen",
    "Earth_gas1" : "Nitrogen",
    "Earth_gas2" : "Oxygen",
    "Jupitor_gas1" : "Hydrogen",
    "Jupitor_gas2" : "Helium",
    "Saturn_gas1" : "Hydrogen",
    "Saturn_gas2" : "Helium",
    "Uranus_gas1" : "Hydrogen",
    "Uranus_gas2" : "Helium",
    "Uranus_gas3" : "Methane"
}
moons = {
    "Mercury" : 0,
    "Venus" : 0,
    "Earth" : 1,
    "Jupitor" : 79,
    "Saturn" : 83,
    "Uranus" : 27
}
rings = {
    "Mercury" : "NO",
    "Venus" : "NO",
    "Earth" : "NO",
    "Jupitor" : "YES",
    "Saturn" : "YES",
    "Uranus" : "YES"
}
class Planet:
    def __init__(self,planet_name,gasses,moons,rings):
        self.planet_name = planet_name
        self.gasses = gasses
        self.moons = moons
        self.rings = rings
    def get_count_of_moons(self):
        count = 0
        for i in self.moons:
            if moons[i] >=1 and rings[i] == "YES":
                count += moons[i]
        print(count)
    def get_the_gas_on_max_planets(self):
        list_b = []
        for i in self.gasses:
            list_b.append(gasses[i])
        
        counter = 0
        gas = []
        for i in list_b:
            curr_frequency = list_b.count(i)
            if(curr_frequency> counter):
                counter = curr_frequency
                gas = i
        print(gas)
        
object_1 = Planet(planet_name,gasses,moons,rings)
object_1.get_count_of_moons()
object_1.get_the_gas_on_max_planets()
