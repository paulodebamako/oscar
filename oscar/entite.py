#=================================
"Creation des classes"
#=================================


class Agent(object):
        
    def __init__(self, field, status,position):
        self.field = field
        self.status = status
          
    def get_field(self):
        return self.field
          
    def get_status(self):
        return self.status

    def get_position(self):
        return self.position

#------------------------------------------------------


class Animal(Agent):

    def __init__(self, health, nutrition, reproduction, age,sensor,regime,position, field, status):
        Agent.__init__(self, position, status, field)
        self.health = health
        self.nutrition = nutrition
        self.reproduction = reproduction
        self.age = age
        self.sexe = sexe
        self.sensor = sensor
        self.regime = regime

    def get_health(self):
        return self.health

    def get_nutrition(self):
        return self.nutrition
			
    def get_reproduction(self):
        return self.reproduction
			
    def get_age(self):
        return self.age
			
    #def get_sexe(self):
    #	return self.sexe
			
    def get_sensor(self):
        return self.sensor
			
    def get_regime(self):
        return self.regime
			
#------------------------------------------------------

class Mineral(Agent):

    def __init__(self,position, status, field):
        Agent.__init__(self, position, status, field)

#------------------------------------------------------

class Vegetal(Agent):

    def __init__(self, health, nutrition, reproduction, age,sensor,position, status, field):
        Agent.__init__(self, position, status, field)
        self.health = health
        self.nutrition = nutrition
        self.reproduction = reproduction
        self.age = age
        #self.sexe = sexe
        self.sensor = sensor
		
    def get_health(self):
        return self.health
			
    def get_nutrition(self):
        return self.nutrition
			
    def get_reproduction(self):
        return self.reproduction
			
    def get_age(self):
        return self.age
			
    #def get_sexe(self):
    #   return self.sexe
			
    def get_sensor(self):
        return self.sensor

#------------------------------------------------------

class Case(object):
    def __init__(self, valeur_field=None):
        self.valeur_field = valeur_field

    def get_valeur_field(self):
        return self.valeur_field

