from Players import Players
from LinkedList import LinkedList

class Program:
    p1 = Players('Auston Matthews',24,205)
    p2 = Players('Mitch Marner',25,172)
    p3 = Players('Michael Bunting',26,186)
    p4 = Players('Morgan Rielly',28,220)
    p5 = Players('William Nylander',26,202)
    team = LinkedList()
    team.add_first(p1)
    team.delete_last()
    team.add_first(p2)
    team.add_first(p3)
    team.add_last(p4)
    team.add_first(p5)
    team.add_last(p1)

    team.print_all()