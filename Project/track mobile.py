
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

print("===== MOBILE NUMBER LOCATION FINDER =====")

mobile = input("Enter Mobile Number with Country Code (+91): ")

try:
    number = phonenumbers.parse(mobile, "IN")

    if phonenumbers.is_valid_number(number):

        print("\n----- MOBILE DETAILS -----")

        print("Mobile Number:", phonenumbers.format_number(
            number,
            phonenumbers.PhoneNumberFormat.INTERNATIONAL
        ))

        print("Country:", geocoder.country_name_for_number(number, "en"))

        print("Region:", geocoder.description_for_number(number, "en"))

        print("Operator:", carrier.name_for_number(number, "en"))

        print("Timezone:", timezone.time_zones_for_number(number))

    else:
        print("Invalid Mobile Number!")

except Exception as e:
    print("Error:", e)
