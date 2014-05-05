import random 

names = [
#{{{
"Homo amans",
"Homo reciprocans",
"Homo oeconomicus",
"Homo ecologicus",
"Homo combinans",
"Homo degeneratus",
"Homo domesticus",
"Homo faber",
"Homo ferox",
"Homo generosus",
"Homo adorans",
"Homo ludens",
"Homo duplex",
"Homo sociologicus",
"Homo loquens",
"Homo loquax",
"Homo necans",
"Homo demens",
"Homo ridens",
"Homo sentimentalis",
"Homo politicus",
"Homo inermis",
"Homo creator",
"Homo pictor",
"Homo aestheticus",
"Homo grammaticus",
"Homo imitans",
"Homo discens",
"Homo educanus",
"Homo investigans",
"Homo excentricus",
"Homo metaphysicus",
"Homo religiosus",
"Homo viator",
"Homo patiens",
"Homo laborans",
"Animal laborans",
"Animal symbolicum",
"Animal rationabile",
"Homo socius",
"Homo poetica",
"Homo neophilus and Homo neophobus",
"Pan narrans",
"Pan sapiens or Homo troglodytes",
"Homo mendax",
"Homo Interneticus",
"Homo technologicus",
"Homo sanguinis",
"Homo mechanicus",
"Homo peregrinum"
]
#}}}

class node:
    """A simple example node"""
    height = None
    name = None
    status = None # True = infected. False / None = un-infected.
    relationship_status = False 
    relationship_with = None

    def __init__(self):
        self.height = random.randint(57, 272)
        self.name = names[random.randint(0, 15)]

    def __repr__(self):
        return str("Hi, my name is " + self.name + " and I am " + str(self.height) + "cm tall, and I am %s" %self.get_status())

    def get_name(self):
        return self.name

    def get_status(self):
        if self.status:
            return "Positive"
        else:
            return "Negative"
