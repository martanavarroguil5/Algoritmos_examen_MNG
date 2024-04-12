from enum import Enum

class HotelRoomType(Enum):

    INDIVIDUAL = 0
    DOBLE = 1
    SUITE = 2

    



def main():
    #TESTING
    print("=================================================================.")
    print("Test Case 1: Check Class HotelRoomType.")
    print("=================================================================.")

    if isinstance(HotelRoomType.INDIVIDUAL, HotelRoomType):
        print("Test PASS. The enum for Individual has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(HotelRoomType.DOBLE, HotelRoomType):
        print("Test PASS. The enum for Doble has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(HotelRoomType.SUITE, HotelRoomType):
        print("Test PASS. The enum for Suite has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


if __name__ == "__main__":
    main()
