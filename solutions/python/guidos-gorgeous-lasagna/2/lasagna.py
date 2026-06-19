EXPECTED_BAKE_TIME = 40
"""We define EXPECTED_BAKE_TIME as a constant """


def bake_time_remaining(time_cooking):
    """We return the bake time remaining by substracting the expected bake time minus the     time cooking"""
    return EXPECTED_BAKE_TIME - time_cooking

bake_time_remaining(30)

   



def preparation_time_in_minutes(number_of_layers):
    """Here we multiply the number or layers by 2 because that is the time you need to        prepare each layer"""
    time = number_of_layers * 2
    return time

preparation_time_in_minutes(5)





def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Here we get the elapsed time by adding the time of cooking the layers plus the         elapsed bake time"""
    
    return number_of_layers * 2 + elapsed_bake_time

elapsed_time_in_minutes(2, 20)


    



