"""
A Flight Class. Model for aircraft flights
"""


class Flight:
    """
    A flight with a particular passenger aircraft
    """

    def __init__(self, flight_num, aircraft):  # called by constructor
        # implementation details begin with '_'
        self._flight_num = flight_num

        if len(flight_num) != 5:
            raise ValueError("Invalid flight number length {}".format(flight_num))
        if not flight_num[:2].isalpha():
            raise ValueError("No airline code {}".format(flight_num))
        if not flight_num[:2].isupper():
            raise ValueError("Improper airline code {}".format(flight_num))

        if not flight_num[2:].isnumeric():
            raise ValueError("Improper flight code {}".format(flight_num))

        self._flight_num = flight_num  # underscore is notation for "private" member

        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan() # this is a dictionary
        self._seating = [None] + \
                        [{letter: None for letter in seats} for _ in rows]

    def flight_num(self):
        """
        Flight Number
        :return: flight number
        """
        return self._flight_num[2:]

    def airline(self):
        return self._flight_num[:2]

    def allocate_seat(self, seat, passenger):
        """
        Allocate a seat to a passenger
        :param seat:  A seat designator as as '12C', '21F'
        :param passenger:  The passenger name
        :return:
        """
        rows, seat_letter = self._aircraft.seating_plan()
        letter = seat[-1] # in our examples above 'C' for '12C' or 'F' for '21F'
        if letter not in seat_letter:
            raise ValueError("Invalid seat letter{}".format(letter))
        row_text = seat[:-1] # take everything but the last letter
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row{}".format(row_text))
        if row not in rows:
            raise ValueError("Invalid row number{}".format(row))
        #Valid seat number at this point. Check for occupancy
        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} already occupied".format(seat))
        # Assign the seat
        self._seating[row][letter] = passenger

    def num_available_seats(self):
        return sum(sum( 1 for s in row.values() if s is None) # the "1" increments
            for row in self._seating
            if row is not None)

    def make_bording_class(self, card_printer):
         for passenger, seat in sorted(self._passenger_seats()):
             card_printer(passenger, seat, self._flight_num(),
                          self._aircraft.model())

    def _passenger_seats(self):
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, "{}{}".format(row,letter))

class Aircraft:
    """
    Characterize features of the aircraft
    """

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def num_rows(self):
        return self._num_rows

    def num_seats_per_row(self):
        return self._num_seats_per_row

    def seating_plan(self):  # ABCDEFGHJK  (no row zero)
        return (range(1, self._num_rows + 1),
                "ABCDEFGHJK"[:self._num_seats_per_row])


def my_code():
    """
    Test function
    :return: 
    """
    pass


if __name__ == '__main__':
    my_code()
    exit(0)
