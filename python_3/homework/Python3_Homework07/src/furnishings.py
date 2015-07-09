'''

Created on June 13 2015

@author: cbabilotte
'''

class Furnishing:
    count = 0
    def __init__(self, room):
        self.room = room
        self.type = self.__class__.__name__
        self.__class__.count += 1
        
class Sofa(Furnishing):
    ''' a Sofa object '''
    pass
    
class Bookshelf(Furnishing):
    ''' a Bookshelf object '''
    pass
    
class Bed(Furnishing):
    ''' a Bed object '''
    pass
    
class Table(Furnishing):
    ''' a Table object '''
    pass
    
def map_the_home(furniture_lst):
    """
    Convert a furniture object list to a built-in dict 
    type where the rooms are the individual keys 
    and the associated value is the list of furniture 
    for that room
    """
    home_dict = {}
    for furniture in furniture_lst:
        room = furniture.room
        if room in home_dict:
            home_dict[room].append(furniture)
        else:
            home_dict[room] = [furniture]
    return home_dict

def counter(furniture_lst):
    """
    Prints the types of furniture and 
    how many there are of each type. 
    """
    home_dict = dict()
    for furniture in furniture_lst:
        home_dict[furniture.type] = furniture.count
    return'\n'.join('{}s: {}'.format(key, value) for key, value in sorted(home_dict.items()))
    
if __name__ == "__main__":
    home = []
    home.append(Bed('Bedroom'))
    home.append(Sofa('Living Room'))
    print(map_the_home(home))
    print(counter(home))

    
    
    
    
    