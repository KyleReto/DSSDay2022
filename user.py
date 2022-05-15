import math

# Convert a given xp value to a level.
def xp_to_level(xp):
    level = round(math.sqrt(xp+1))
    return level

class User:
    def __init__(self, uid):
        self.uid = uid
        self.xp = 0
    
    # uid is the user's unique discord ID (string)
    def get_uid(self):
        return self.uid
    
    # level is a derived property from xp (integer)
    def get_level(self):
        return xp_to_level(self.xp)
