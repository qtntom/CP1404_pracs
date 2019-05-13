from prac_08.silver_service_taxi import SilverServiceTaxi

silver_cab = SilverServiceTaxi(name='Gold service', fuel=1000, fanciness=2)
silver_cab.start_fare()
silver_cab.drive(18)
print(silver_cab)
print('current fare: ${}'.format(silver_cab.get_fare()))

