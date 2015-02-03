# quickbot
#
#                     _'_'_ IRfm
#                 ++++++++++++++
#             _/ +              + \_
#       IRfl _/ +                + \_ IRfr
#            / +     LMP   RMP    + \
#              +    __|     |__   +
#              +   |          |   +
#              +   |          |   +
#           _|++++ |  _    _  | ++++|_
#      IRbl _|++++_| T T  T T |_++++|_ IRbr
#            |++++   | |  | |   ++++|
#             ++++    Ol   Or   ++++
#              +                  +
#               ++++++++++++++++++
#
# ir
#IRbl = "P9_38"
IRfl = "P9_40"
IRfm = "P9_38"
IRfr = "P9_36"
#IRbr = "P9_33"
#IRS = (IRbl, IRfl, IRfm, IRfr, IRbr)

# encoder aka odometry
Or = "P9_39"
Ol = "P9_37"

# motors
INl1 = "P8_14"
INl2 = "P8_16"
PWMl = "P9_16"

INr1 = "P8_12"
INr2 = "P8_10"
PWMr = "P9_14"

RMP = (INr1, INr2, PWMr)
LMP = (INl1, INl2, PWMl)

# led
LED = "USR1"
