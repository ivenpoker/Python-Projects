# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Convert pressure in kilopascals to pounds per square inch,   #
#                        a millimeter of mercury (mmHg) and atmosphere pressure.      #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : August 19, 2019                                              #
#                                                                                     #
#######################################################################################

if __name__ == "__main__":
    kpa = float(input("Enter pressure in kilo pascals: "))
    psi = kpa / 6.89475729
    mmhg = kpa * 760 / 101.325
    atm = kpa / 101.325

    print("The pressure in pounds per square inch: %.2f psi." % psi)
    print("The pressure in millimeter of mercury: %.2f mmHg" % mmhg)
    print("Atmosphere pressure: %.2f atm." % atm)