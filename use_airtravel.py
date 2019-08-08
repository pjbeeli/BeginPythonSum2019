"""
Use flight class
"""
from airtravel import Flight, Aircraft
from pprint import pprint as pp

def is_valid_flight(flight_num):
    """
    Check for the syntax  (# syntax LL### ie, alphabetic, alpha, numeric, num, num)
    :param str:
    :return:
    """
    # if ( (len(flight_num) == 5) and flight_num.isalpha(flight_num[0,1])):
    #     if (flight_num[0,1] == flight_num[0,1].Capitalize() ):
    #         if (isnumeric(flight_num[2:5])):
    #             return True
    # return False

def make_flight():
    flight = Flight("SN066", Aircraft("G-EUP", "Airbus A319", num_rows=22, num_seats_per_row=6))

    flight.allocate_seat('11C', "Guido Van Rossum")
    flight.allocate_seat('11F', "Jack Sprat")
    flight.allocate_seat('02A', "Jack Sprat Jr.")

    pp(flight._seating)
    return flight

def console_card_printer(passenger, seat, flight_number, aircraft):
    output = "| Name:  {0}", " Flight: {1}", " Seat: {2}" \
            " Aircraft: {3} |".format(passenger, flight_number, seat, aircraft)
    banner = "+" + "-" * (len(output) -2) + "+"
    border = "|" + " " * (len(output) -2) + "|"
    lines = [banner, border, output, border, banner]
    card = '\n'.join(lines)
    print(card)
    print()

def my_code():
    """
    Test function
    :return: 
    """

    flight_1 = make_flight()
    flight_1 = Flight("SN066", Aircraft("G-EUP", "Airbus A319", num_rows=22, num_seats_per_row=6))

    pp(flight_1._seating)
    # Count the Nones
    #capacity = flight_1._aircraft.seating_plan()
    print("Available seats", flight_1.num_available_seats())
    flight_1.make_bording_class(console_card_printer)
     # don't include the function i.e., the paranthesis.

    return flight_1

if __name__ == '__main__':
    my_code()
    exit(0)
