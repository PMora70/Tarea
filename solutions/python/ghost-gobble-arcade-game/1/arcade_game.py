def eat_ghost(power_pellet_active, touching_ghost):
    
    if power_pellet_active == True and touching_ghost == True:
        return True
    else: 
        return False


def score(touching_power_pellet, touching_dot):
    
    if touching_power_pellet == True or touching_dot == True:
        return True
    else:
        return False
 

def lose(power_pellet_active, touching_ghost):
    if power_pellet_active == False and touching_ghost == True:
        return True
    else: 
        return False
  

def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    if power_pellet_active == True and touching_ghost == True and has_eaten_all_dots == True:
        return True
        
    elif power_pellet_active == True and touching_ghost == True and has_eaten_all_dots == False:
        return False
        
    elif power_pellet_active == False and touching_ghost == True and has_eaten_all_dots == True:
        return False
    else:
        return True