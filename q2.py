class Quark:
    def __init__(self, color, flavor):
        validcolors=["red", "blue", "green"]
        validflavors=['up', 'down', 'strange', 'charm', 'top', 'bottom']
        if color in validcolors and flavor in validflavors:
            self.color= color
            self.flavor= flavor
            self.barryonnumber=0.3333333333333333
        
    def interact(self, newquark):
        tempcol= self.color
        self.color= newquark.color
        newquark.color= tempcol

q1=Quark("green", "up")
q2=Quark("blue", "strange")

print("q1 color before interaction is",q1.color)
print("q2 color before interaction is",q2.color)

q1.interact(q2)

print("q1 color after interaction is",q1.color)
print("q2 color after interaction is",q2.color)
