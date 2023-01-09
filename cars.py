# import requests
# cars = []
# API_KEY = "HXKClddPQZiIbQ8G6IKLIg==2Hgb5E6Svht4MyqS"

# for model in models:
#   api_url = 'https://api.api-ninjas.com/v1/cars?model={}'.format(model)
#   response = requests.get(api_url, headers={'X-Api-Key': API_KEY}).json()
#   if len(response) > 0:
#     cars.append(response[0])

# car_list = [
#   {
#     'model' : 'model name',
#     'make' : 'make name',
#     'year' : 'year made (INTEGER)',
#     'price' : 'price (INTEGER)',
#     'color' : 'color',
#     'mileage' : '',
#     'body_type' :,
#     'fuel_type' : 'electric or gas ',
#     'image' : 'record the image'
#   }
# ]

honda = [{
  'model': "Odyssey",
  'make': 'Honda',
  'year': 2016,
  'price': 19999,
  'color': 'white',
  'mileage': 122000,
  'body_type': 'Mini Van',
  'fuel_type': 'Gas',
  'image': 'static/cars/odyssey.png'
}, {
  'model': "Civic",
  'make': 'Honda',
  'year': 2019,
  'price': 22999,
  'color': 'red',
  'mileage': 86000,
  'body_type': "Sedan",
  'fuel_type': 'Gas',
  'image': 'static/cars/civic.png'
}, {
  'model': "Accord",
  'make': 'Honda',
  'year': 2019,
  'price': 26999,
  'color': 'silver',
  'mileage': 39000,
  'body_type': "Sedan",
  'fuel_type': 'Gas',
  'image': 'static/cars/accord.png'
}, {
  'model': "CR-V",
  'make': 'Honda',
  'year': 2011,
  'price': 17999,
  'color': 'blue',
  'mileage': 72000,
  'body_type': "SUV",
  'fuel_type': 'Gas',
  'image': 'static/cars/crv.png'
}, {
  'model': "Insight",
  'make': 'Honda',
  'year': 2022,
  'price': 29999,
  'color': 'black',
  'mileage': 14000,
  'body_type': "Sedan",
  'fuel_type': 'Gas',
  'image': 'static/cars/insight.png'
}, {
  'model': "Pilot",
  'make': 'Honda',
  'year': 2013,
  'price': 19999,
  'color': 'white',
  'mileage': 122000,
  'body_type': "SUV",
  'fuel_type': 'Gas',
  'image': 'static/cars/pilot.png'
}, {
  'model': "Passport",
  'make': 'Honda',
  'year': 2020,
  'price': 39999,
  'color': 'red',
  'mileage': 6000,
  'body_type': "SUV",
  'fuel_type': 'Gas',
  'image': 'static/cars/passport.png'
}, {
  'model': "HR-V",
  'make': 'Honda',
  'year': 2022,
  'price': 28999,
  'color': 'white',
  'mileage': 7000,
  'body_type': "SUV",
  'fuel_type': 'Gas',
  'image': 'static/cars/hrv.png'
}]

nissan = [{
  'model': 'Altima',
  'make': 'Nissan',
  'year': 2021,
  'price': 23999,
  'color': 'Black',
  'mileage': 38000,
  'body_type': 'Sedan',
  'fuel_type': 'Gas',
  'image': 'static/cars/altima.png'
}, {
  'model': 'Quest',
  'make': 'Nissan',
  'year': 2014,
  'price': 16999,
  'color': 'White',
  'mileage': 69000,
  'body_type': "Minivan",
  'fuel_type': 'Gas',
  'image': 'static/cars/quest.png'
}, {
  'model': 'Rogue',
  'make': 'Nissan',
  'year': 2018,
  'price': 21999,
  'color': 'Silver',
  'mileage': 75000,
  'body_type': 'SUV',
  'fuel_type': 'Gas',
  'image': 'static/cars/rogue.png'
}, {
  'model': 'Armada',
  'make': 'Nissan',
  'year': 2019,
  'price': 35999,
  'color': 'Blue',
  'mileage': 35998,
  'body_type': 'SUV',
  'fuel_type': 'Gas',
  'image': 'static/cars/armada.png'
}, {
  'model': 'Juke',
  'make': 'Nissan',
  'year': 2017,
  'price': 17999,
  'color': 'Red',
  'mileage': 54000,
  'body_type': "SUV",
  'fuel_type': 'Gas',
  'image': 'static/cars/juke.png'
}, {
  'model': 'Leaf',
  'make': 'Nissan',
  'year': 2020,
  'price': 27999,
  'color': 'Black',
  'mileage': 15000,
  'body_type': 'Compact',
  'fuel_type': 'Electric',
  'image': 'static/cars/leaf.png'
}, {
  'model': 'Murano',
  'make': 'Nissan',
  'year': 2018,
  'price': 24999,
  'color': 'Gray',
  'mileage': 58000,
  'body_type': "SUV",
  'fuel_type': 'Gas',
  'image': 'static/cars/murano.png'
}]

toyota = [{
  'model': 'Camry',
  'make' : 'Toyota',
  'year' : 2011,
  'price' : 14599,
  'color' : 'Red',
  'mileage' : 114000,
  'body_type' : 'Sedan',
  'fuel_type': 'Gas',
  'image': 'static/cars/camry.png'
},{
  'model': 'Corolla',
  'make' : 'Toyota',
  'year' : 2021,
  'price' : 22998,
  'color' : 'Black',
  'mileage' : 23000,
  'body_type' : 'Sedan',
  'fuel_type': 'Gas',
  'image': 'static/cars/corolla.png'
},{
  'model': 'RAV4',
  'make' : 'Toyota',
  'year' : 2022,
  'price': 48998,
  'color' : 'Black',
  'mileage' : 14000,
  'body_type' : 'SUV',
  'fuel_type': 'Hybrid',
  'image': 'static/cars/rav4.png'
},{
  'model': 'Highlander',
  'make' : 'Toyota',
  'year' : 2017,
  'price': 35998,
  'color' : 'Gray',
  'mileage' : 23000,
  'body_type' : 'SUV',
  'fuel_type': 'Gas',
  'image': 'static/cars/highlander.png'
},{
  'model': 'Prius',
  'make' : 'Toyota',
  'year' : 2021,
  'price': 28998,
  'color' : 'Gray',
  'mileage' : 38000,
  'body_type' : 'Sedan',
  'fuel_type': 'Hybrid',
  'image': 'static/cars/prius.png'
},{
  'model': 'Sequoia',
  'make' : 'Toyota',
  'year' : 2014,
  'price': 35998,
  'color' : 'Silver',
  'mileage' : 64000,
  'body_type' : 'SUV',
  'fuel_type': 'Gas',
  'image': 'static/cars/sequoia.png'
},{
  'model': 'Tundra',
  'make' : 'Toyota',
  'year' : 2020,
  'price': 43998,
  'color' : 'Silver',
  'mileage' : 44000,
  'body_type' : 'Truck',
  'fuel_type': 'Gas',
  'image': 'static/cars/tundra.png'
}]

acura = [{
  'model': 'ILX',
  'make': 'Acura',
  'year': 2022,
  'price': 30998,
  'color': 'White',
  'mileage': 7000,
  'body_type': 'Sedan',
  'fuel_type': 'Gas',
  'image': 'static/cars/ILX.png'
},{
  'model': 'Integra',
  'make': 'Acura',
  'year': 2023,
  'price': 37998,
  'color': 'Blue',
  'mileage': 3000,
  'body_type': 'Sedan',
  'fuel_type': 'Gas',
  'image': 'static/cars/integra.png'
},{
  'model': 'MDX',
  'make': 'Acura',
  'year': 2017,
  'price': 33998,
  'color': 'Black',
  'mileage': 40000,
  'body_type': 'SUV',
  'fuel_type': 'Gas',
  'image': 'static/cars/MDX.png'
},{
  'model': 'RDX',
  'make': 'Acura',
  'year': 2018,
  'price': 29998,
  'color': 'White',
  'mileage': 32000,
  'body_type': 'SUV',
  'fuel_type': 'Gas',
  'image': 'static/cars/RDX.png'
},{
  'model': 'TLX',
  'make': 'Acura',
  'year': 2015,
  'price': 23998,
  'color': 'Red',
  'mileage': 24000,
  'body_type': 'Sedan',
  'fuel_type': 'Gas',
  'image': 'static/cars/TLX.png'
},{
  'model': 'TSX',
  'make': 'Acura',
  'year': 2012,
  'price': 16998,
  'color': 'Gray',
  'mileage': 98000,
  'body_type': 'Sedan',
  'fuel_type': 'Gas',
  'image': 'static/cars/TSX.png'
},{
  'model': 'RLX',
  'make': 'Acura',
  'year': 2015,
  'price': 20998,
  'color': 'White',
  'mileage': 73000,
  'body_type': 'Sedan',
  'fuel_type': 'Gas',
  'image': 'static/cars/RLX.png'
}]


chevrolet = [{
  'model': 'Equinox',
  'make': 'Chevrolet',
  'year': 2014,
  'price': 15998,
  'color': 'Black',
  'mileage': 96000,
  'body_type': 'SUV',
  'fuel_type': 'Gas',
  'image': 'static/cars/equinox.png'
},{
  'model': 'Silverado',
  'make': 'Chevrolet',
  'year': 2020,
  'price': 51998,
  'color': 'White',
  'mileage': 18000,
  'body_type': 'Truck',
  'fuel_type': 'Gas',
  'image': 'static/cars/silverado.png'
},{
  'model': 'Blazer',
  'make': 'Chevrolet',
  'year': 2020,
  'price': 27998,
  'color': 'Red',
  'mileage': 30000,
  'body_type': 'SUV',
  'fuel_type': 'Gas',
  'image': 'static/cars/blazer.png'
},{
  'model': 'Malibu',
  'year': 2018,
  'price': 19998,
  'color': 'Silver',
  'mileage': 63000,
  'body_type': 'Sedan',
  'fuel_type': 'Gas',
  'image': 'static/cars/malibu.png'
},{
  'model': 'Tahoe',
  'make': 'Chevrolet',
  'year': 2019,
  'price': 47998,
  'color': 'White',
  'mileage': 55000,
  'body_type': 'Truck',
  'fuel_type': 'Gas',
  'image': 'static/cars/tahoe.png'
},{
  'model': 'Suburban',
  'make': 'Chevrolet',
  'year': 2011,
  'price': 20998,
  'color': 'Black',
  'mileage': 124000,
  'body_type': 'SUV',
  'fuel_type': 'Gas',
  'image': 'static/cars/suburban.png'
},{
  'model': 'Camaro',
  'make': 'Chevrolet',
  'year': 2017,
  'price': 36998,
  'color': 'Gray',
  'mileage': 46000,
  'body_type': 'Sedan',
  'fuel_type': 'Gas',
  'image': 'static/cars/camaro.png'
}]

ford = [{
  'model': 'Edge',
  'make': 'Ford',
  'year': 2016,
  'price': 18999,
  'color': 'Blue',
  'mileage': 98000,
  'body_type': 'SUV',
  'fuel_type': 'Gas',
  'image': 'static/cars/edge.jpeg'
}, {
  'model': 'Escape',
  'make': 'Ford',
  'year': 2017,
  'price': 18999,
  'color': 'Red',
  'mileage': 51000,
  'body_type': 'SUV',
  'fuel_type': 'Gas',
  'image': 'static/cars/escape.jpeg'
}, {
  'model': 'Fiesta',
  'make': 'Ford',
  'year': 2017,
  'price': 13599,
  'color': 'Black',
  'mileage': 72000,
  'body_type': 'Supermini',
  'fuel_type': 'Gas',
  'image': 'static/cars/fiesta.jpeg'
}, {
  'model': 'Flex',
  'make': 'Ford',
  'year': 2019,
  'price': 26999,
  'color': 'Gray',
  'mileage': 22000,
  'body_type': 'SUV',
  'fuel_type': 'Gas',
  'image': 'static/cars/flex.jpeg'
}, {
  'model': 'Ranger',
  'make': 'Ford',
  'year': 2021,
  'price': 35999,
  'color': 'Gray',
  'mileage': 40000,
  'body_type': 'Truck',
  'fuel_type': 'Gas',
  'image': 'static/cars/ranger.jpeg'
}, {
  'model': 'Taurus',
  'make': 'Ford',
  'year': 2015,
  'price': 18999,
  'color': 'Red',
  'mileage': 69000,
  'body_type': 'Sedan',
  'fuel_type': 'Gas',
  'image': 'static/cars/taurus.jpeg'
}, {
  'model': 'Mustang',
  'make': 'Ford',
  'year': 2019,
  'price': 25999,
  'color': 'Black',
  'mileage': 59000,
  'body_type': 'Coupe',
  'fuel_type': 'Gas',
  'image': 'static/cars/mustang.jpeg'
}]

tesla = [{
  'model': 'Model 3',
  'make': 'Tesla',
  'year': 2019,
  'price': 42999,
  'color': 'blue',
  'mileage': 15000,
  'body_type': 'Sedan',
  'fuel_type': 'Electric',
  'image': 'static/cars/model3.png'
}, {
  'model': 'Model Y',
  'make': 'Tesla',
  'year': 2021,
  'price': 59999,
  'color': 'black',
  'mileage': 21000,
  'body_type': 'Sedan',
  'fuel_type': 'Electric',
  'image': 'static/cars/modely.png'
}, {
  'model': 'Model X',
  'make': 'Tesla',
  'year': 2018,
  'price': 80999,
  'color': 'red',
  'mileage': 15000,
  'body_type': 'SUV',
  'fuel_type': 'Electric',
  'image': 'static/cars/modelx.jpeg'
}, {
  'model': 'Model S',
  'make': 'Tesla',
  'year': 2018,
  'price': 65999,
  'color': 'black',
  'mileage': 47000,
  'body_type': 'Sedan',
  'fuel_type': 'Electric',
  'image': 'static/cars/models.png'
}]
cars = honda
for i in ford:
  cars.append(i)
for i in nissan:
  cars.append(i)
for i in tesla:
  cars.append(i)
for i in chevrolet:
  cars.append(i)
for i in acura:
  cars.append(i)
for i in toyota:
  cars.append(i)
# cars.append(honda)
# cars.append(ford)
# cars.append(nissan)
# cars.append(tesla)