import phonenumbers
from phonenumbers import timezone, geocoder, carrier

number = input("Enter your phone number: ")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
simDetails = carrier.name_for_number(phone, 'en')
register = geocoder.description_for_number(phone, 'en') 
print(phone)
print(time)
print(simDetails)
print(register)




 
  
