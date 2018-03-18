def hotel_cost(nights):
    if nights > 0:
        return 140 * int(nights)

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    else:
        return None

def rental_car_cost(days):
    if days < 3:
        return 40 * days
    elif days > 6:
        return 40 * days - 50
    else:
        return 40 * days - 20

def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

print trip_cost("Los Angeles", 5, 600)
