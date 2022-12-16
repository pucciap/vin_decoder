# sample vin #'s chevy equinox
# 2GNAXHEVXL
# 2GNAXUEV8L
# 3GNAXUEV5K

# sample vins camaro
# 1G1FF1R73L
# 1G1FC1RS2L
# 1G1FE1R73L
# 1G1FK1R67K

# sample vins bolt
# 1G1FY6S09L
# 1G1FY6S03L
# 1G1FY6S07L
# 1G1FY6S00K
# 1G1FY6S05K

# sample vins chevy impala
# 1G11Z5S3XL
# 1G11Z5S31L
# 2G11Z5S30L
# 1G11Z5S34L

# sample vins chevy malibu
# 1G1ZD5ST7J
# 1G1ZB5ST5J
# 1G1ZD5ST7J
# 1G1ZD5ST8L
# 1G1ZD5ST4L
# 1G1ZD5ST8L

# sample vins chevy colorado
# 1GCGSCEN9L1191222
# 1GCGSCEN4L1188664
# 1GCGTCEN9K1179647


# user inputs vin number to get Year, Make , Model, Trim , Drivetrain, Engine

vin_number = list(input("Vin #: "))

# Dictionaries For Vin Decoder

# Dictionary for Country of Origin / Digit # 1

country_of_origin = {
    "1": "USA",
}

# Dictionary for manufacturer / Digit # 2

manufacturer = {
    "G": "General Motors Corp. 1995-2023",
}

# Dictionary for engine  / Digit # 8

engine_dict = {
    "V": "1.5L I4 DI DOHC T/C", "X": "2.0L I4 DI DOHC T/C", "6": "6.2L V8 DI OHV S/C""", "7": "6.2L V8 DI OHV",
    "S": "3.6L V6 DI DOHC", "0": "65kw", "3": "3.6L V6 SIDI DOHC VVT Flex", "T": "1.5L I4 DI DOHC T/C",
    "U": "1.8L I4 SIDI DOHC Hybrid", "1": "2.8L I4 DI DOHC TDsl", "A": "2.5L I4 DI DOHC, Flex", "N": "3.6L V6 DI DOHC",
}

engine_key = engine_dict.keys()
engine_value = engine_dict.values()


def get_engine_from_vin(vin_number):
    return engine_dict[vin_number[7]]


# Dictionary for model year  / Digit #10

model_year_dict = {
    "A": "2010", "B": "2011", "C": "2012", "D": "2013", "E": "2014", "F": "2015", "G": "2016", "H": "2017", "J": "2018",
    "K": "2019", "L": "2020", "M": "2021", "N": "2022", "P": "2023", "R": "2024"
}

model_year_key = model_year_dict.keys()
model_year_value = model_year_dict.values()


def get_model_year_from_vin(vin_number):
    return model_year_dict[vin_number[9]]


# Dictionary for Vehicle Make /  Digit #3

vehicle_make_dict = {
    "N": "Chevrolet", "1": "Chevrolet", "C": "Chevrolet", "B": "Chevrolet",
}

vehicle_make_key = vehicle_make_dict.keys()
vehicle_make_value = vehicle_make_dict.values()


def get_vehicle_make_from_vin(vin_number):
    return vehicle_make_dict[vin_number[2]]


# Dictionary for Trim Levels

trim_level_dict = {
    "X5": "Equinox 1LS 1.5L AWD", "XF": "Equinox 1LS 1.5L FWD", "XG": "Equinox L FWD", "XH": "Equinox L FWD",
    "XJ": "Equinox 1LT 1.5L FWD", "XK": "Equinox 1LT 1.5L FWD", "XL": "Equinox 2LT 2.0L FWD",
    "XN": "Equinox 2LT 2.0L FWD",
    "XP": "Equinox 2LT 2.0L FWD", "XS": "Equinox LS AWD", "XT": "Equinox 1LT 1.5L AWD", "XU": "Equinox 1LT 1.5L AWD",
    "XV": "Equinox 2LT 2.0L AWD", "XX": "Equinox 1LT 1.5L AWD", "XY": "Equinox 1.5 Premier FWD",
    "F9": "Non-US, Non-Canada",
    "FA": "Camaro 1LS or 1LT 6sp", "FB": "Camaro 1LT Auto", "FC": "Camaro 2LT 6sp", "FD": "Camaro 2LT Auto",
    "FE": "Camaro 1SS 6sp", "FF": "Camaro 1SS Auto", "FG": "Camaro 2SS 6sp", "FH": "Camaro 2SS Auto",
    "FJ": "Camaro ZL1 6sp",
    "FK": "Camaro ZL1 Auto", "F7": "Bolt Non-US, Non-Canada", "FW": "Bolt LT", "FX": "Bolt Premier",
    "FY": "Bolt LT w/Fast Charge", "FZ": "Bolt Premier w/Fast Charge", "10": "Impala Premier",
    "13": "Impala Non-US, Non-Canada",
    "1X": "Impala LS 2FL", "1Y": "Impala LS", "1Z": "Impala 1LT", "ZA": "Malibu L", "ZB": "Malibu LS",
    "ZC": "Malib LS Fleet",
    "ZD": "Malibu LT", "ZE": "Malibu Premier", "ZF": "Malibu Hybrid", "ZG": "Malibu RS", "B8": "Blazer Export",
    "BA": "L Blazer FWD",
    "BB": "1LT Blazer FWD", "BC": "2LT Blazer FWD", "BD": "3LT Blazer FWD", "BE": "RS Blazer FWD",
    "BF": "Premier Blazer FWD",
    "BH": "2LT Blazer AWD", "BJ": "3LT Blazer AWD", "BK": "RS Blazer AWD", "BL": "Premier Blazer AWD",
    "SA": "Colorado Base 2WD",
    "SB": "Colorado W/T 2WD,", "SC": "Colorado LT 2WD", "SD": "Colorado Z71 2WD", "TB": "Colorado W/T 4WD",
    "TC": "Colorado LT 4WD",
    "TD": "Colorado Z71 4WD", "TE": "Colorado ZR2 4WD",
}

trim_level_key = trim_level_dict.keys()
trim_level_value = trim_level_dict.values()


# function for trim level


def get_digit_four_five_trim_level_from_vin(vin_number):
    for trim_level_key, trim_level_value in trim_level_dict.items():
        if trim_level_key == vin_number[3] + vin_number[4]:
            return trim_level_value


# function for chevy equinox trims and bolt

def get_digit_five_six_trim_level_from_vin(vin_number):
    for trim_level_key, trim_level_value in trim_level_dict.items():
        if trim_level_key == vin_number[4] + vin_number[5]:
            return trim_level_value


# Dictionary for Body Type / Digit # 4

body_type_dict = {
    "G": "Crew Cab", "H": "Extended Cab", "P": "Crew Cab",
    "R": "Extended Cab", "1": "2D Coupe", "3": "2D Convertible", "5": "4D Sedan"
}

body_type_key = body_type_dict.keys()
body_type_value = body_type_dict.values()


def get_vehicle_body_type_digit_three():
    for body_type_key, body_type_value in body_type_dict.items():
        if body_type_key == vin_number[3]:
            return body_type_value

def get_vehicle_body_type_digit_six(vin_number):
    for body_type_key, body_type_value in body_type_dict.items():
        if body_type_key == vin_number[5]:
            return body_type_value


# assigning a variable for the user view vehicle year
year = get_model_year_from_vin(vin_number)

# assigning a variable for the user view vehicle make
make = get_vehicle_make_from_vin(vin_number)

# assigning a variable for user view vehicle trim level
trim = get_digit_five_six_trim_level_from_vin(vin_number) or get_digit_four_five_trim_level_from_vin(vin_number)

# assigning a variable for user view body types
body_type = get_vehicle_body_type_digit_three() or get_vehicle_body_type_digit_six(vin_number)
# assigning a variable for user view vehicle engine
engine = get_engine_from_vin(vin_number)

# assigning a variable for final user view Vehicle Year, Make, Model, Trim   #{body_type}
final_user_view = f"{year} {make} {trim} {body_type} {engine}"

print(final_user_view)
