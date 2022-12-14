# sample vin #'s chevy equinox
# 2GNAXHEVXL
# 2GNAXUEV8L
# 3GNAXUEV5K

# sample vins camaro
# 1G1FF1R73L
# 1G1FC1RS2L0140222
# 1G1FE1R73L0107705
# 1G1FK1R67K0129334

# sample vins bolt
# 1G1FY6S09L4105175
# 1G1FY6S03L4144621
# 1G1FY6S07L4136912
# 1G1FY6S00K4126849
# 1G1FY6S05K4132081

# sample vins chevy impala
# 1G11Z5S3XLU101499
# 1G11Z5S31LU112035
# 2G11Z5S30L9101282
# 1G11Z5S34LU112224

# sample vins chevy malibu
# 1G1ZD5ST7JF125861
# 1G1ZB5ST5JF293987
# 1G1ZD5ST7JF125861
# 1G1ZD5ST8LF101412
# 1G1ZD5ST4LF110124
# 1G1ZD5ST8LF089763

# user inputs vin number to get Year, Make , Model, Trim , Drivetrain, Engine

vin_number = list(input("Vin #: "))

# Dictionaries For Vin Decoder

# Dictionary for Country of Origin, vin decoder 1st digit

country_of_origin = {
    "1": "USA",
}

# Dictionary for manufacturer, vin decoder 2nd digit

manufacturer = {
    "G": "General Motors Corp. 1995-2023",
}

# Dictionary for engine digit 8

engine_dict = {
    "V": "1.5L I4 DI DOHC T/C", "X": "2.0L I4 DI DOHC T/C", "6": "6.2L V8 DI OHV S/C""", "7": "6.2L V8 DI OHV",
    "S": "3.6L V6 DI DOHC", "0": "65kw", "3": "3.6L V6 SIDI DOHC VVT Flex", "T": "1.5L I4 DI DOHC T/C",
    "U": "1.8L I4 SIDI DOHC Hybrid",
}

engine_key = engine_dict.keys()
engine_value = engine_dict.values()


def get_engine_from_vin(vin_number):
    return engine_dict[vin_number[7]]


# Dictionary for model year , vin decoder digit #10

model_year_dict = {
    "A": "2010", "B": "2011", "C": "2012", "D": "2013", "E": "2014", "F": "2015", "G": "2016", "H": "2017", "J": "2018",
    "K": "2019", "L": "2020", "M": "2021", "N": "2022", "P": "2023", "R": "2024"
}

model_year_key = model_year_dict.keys()
model_year_value = model_year_dict.values()


def get_model_year_from_vin(vin_number):
    return model_year_dict[vin_number[9]]


# Dictionary for Vehicle Make

vehicle_make_dict = {
    "N": "Chevrolet", "1": "Chevrolet",
}

vehicle_make_key = vehicle_make_dict.keys()
vehicle_make_value = vehicle_make_dict.values()


def get_vehicle_make_from_vin(vin_number):
    return vehicle_make_dict[vin_number[2]]


# Dictionary for Chevrolet Trims

trim_level_dict = {
    "X5": "Equinox 1LS 1.5L AWD", "XF": "Equinox 1LS 1.5L FWD", "XG": "Equinox L FWD", "XH": "Equinox L FWD",
    "XJ": "Equinox 1LT 1.5L FWD", "XK": "Equinox 1LT 1.5L FWD", "XL": "Equinox 2LT 2.0L FWD", "XN": "Equinox 2LT 2.0L FWD",
    "XP": "Equinox 2LT 2.0L FWD", "XS": "Equinox LS AWD", "XT": "Equinox 1LT 1.5L AWD", "XU": "Equinox 1LT 1.5L AWD",
    "XV": "Equinox 2LT 2.0L AWD", "XX": "Equinox 1LT 1.5L AWD", "XY": "Equinox 1.5 Premier FWD", "F9": "Non-US, Non-Canada",
    "FA": "Camaro 1LS or 1LT 6sp", "FB": "Camaro 1LT Auto", "FC": "Camaro 2LT 6sp", "FD": "Camaro 2LT Auto",
    "FE": "Camaro 1SS 6sp", "FF": "Camaro 1SS Auto", "FG": "Camaro 2SS 6sp", "FH": "Camaro 2SS Auto", "FJ": "Camaro ZL1 6sp",
    "FK": "Camaro ZL1 Auto", "F7": "Bolt Non-US, Non-Canada", "FW": "Bolt LT", "FX": "Bolt Premier",
    "FY": "Bolt LT w/Fast Charge", "FZ": "Bolt Premier w/Fast Charge", "10": "Impala Premier", "13": "Impala Non-US, Non-Canada",
    "1X": "Impala LS 2FL", "1Y": "Impala LS", "1Z": "Impala 1LT", "ZA": "Malibu L", "ZB": "Malibu LS", "ZC": "Malib LS Fleet",
    "ZD": "Malibu LT", "ZE": "Malibu Premier", "ZF": "Malibu Hybrid", "ZG": "Malibu RS", "B8": "Blazer Export", "BA": "L Blazer FWD",
    "BB": "1LT Blazer FWD", "BC": "2LT Blazer FWD", "BD": "3LT Blazer FWD", "BE": "RS Blazer FWD", "BF": "Premier Blazer FWD",
    "BH": "2LT Blazer AWD", "BJ": "3LT Blazer AWD", "BK": "RS Blazer AWD", "BL": "Premier Blazer AWD",
}

trim_level_key = trim_level_dict.keys()
trim_level_value = trim_level_dict.values()


# function for chevy camaro trims and malibu


def get_digit_four_five_trim_level_from_vin(vin_number):
    for trim_level_key, trim_level_value in trim_level_dict.items():
        if trim_level_key == vin_number[3] + vin_number[4]:
            return trim_level_value


# function for chevy equinox trims and bolt

def get_digit_five_six_trim_level_from_vin(vin_number):
    for trim_level_key, trim_level_value in trim_level_dict.items():
        if trim_level_key == vin_number[4] + vin_number[5]:
            return trim_level_value


# assigning a variable for the user view vehicle year
year = get_model_year_from_vin(vin_number)

# assigning a variable for the user view vehicle make
make = get_vehicle_make_from_vin(vin_number)

# assigning a variable for user view vehicle trim level
trim = get_digit_five_six_trim_level_from_vin(vin_number) or get_digit_four_five_trim_level_from_vin(vin_number)

# assigning a variable for user view vehicle engine
engine = get_engine_from_vin(vin_number)

# assigning a variable for final user view Vehicle Year, Make, Model, Trim
final_user_view = f"{year} {make} {trim} {engine}"

print(final_user_view)

