def get_rounds(number):
    rounds = [number, number + 1, number + 2]
    return rounds

    
def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2
    
    
def list_contains_round(rounds, number):
    if number in rounds:
        return True
    return False

    
def card_average(hand):
    return sum(hand) / len(hand)

    
def approx_average_is_average(hand):
    first_and_last_average = (hand[0] + hand[-1]) / 2
    median_average = hand[len(hand) // 2]
    average = sum(hand) / len(hand)
    if average == first_and_last_average or average == median_average:
        return True
    return False
    

def average_even_is_average_odd(hand):

    odd_numbers = hand[0: :2]
    even_numbers = hand[1: :2]
    
    odd_average = sum(odd_numbers) / len(odd_numbers)
    even_average = sum(even_numbers) / len(even_numbers)

    if odd_average == even_average:
        return True
    return False
    
    
def maybe_double_last(hand):
    if hand[-1] == 11:
        hand[-1] = hand[-1] * 2
    return hand

    
