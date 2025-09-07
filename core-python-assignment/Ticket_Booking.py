def book_seat(total_seats, booked, seat):
    if seat in booked:
        print("Seat", seat, "is already booked.")
    elif seat > total_seats or seat <= 0:
        print("Seat", seat, "is invalid.")
    else:
        booked.append(seat)
    return booked
def cancel_seat(booked, seat):
    if seat in booked:
        booked.remove(seat)
    else:
        print("Seat", seat, "is not booked.")
    return booked
def available_seats(total_seats, booked):
    return [s for s in range(1, total_seats + 1) if s not in booked]
total_seats = 10
booked_seats = [2, 5, 7]
booked_seats = book_seat(total_seats, booked_seats, 3)
booked_seats = cancel_seat(booked_seats, 5)
print("Available seats:", available_seats(total_seats, booked_seats))
