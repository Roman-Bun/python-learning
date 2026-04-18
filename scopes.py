total_score = 0

def add_points(amount):
    global total_score
    total_score = total_score + amount
    print(f"Points added! Current score: {total_score}")

add_points(10)