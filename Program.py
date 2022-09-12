from Players import Players
from LinkedList import LinkedList

class Program:
    p1 = Players('Auston Matthews',24,205)
    p2 = Players('Mitch Marner',25,172)
    p3 = Players('Michael Bunting',26,186)
    
    team = LinkedList()
    team.add_first(p1)
    team.add_first(p2)
    team.add_first(p3)

    team.print_all()