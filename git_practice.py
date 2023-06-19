cities={
    'beijing':{
        'pop':'****',
        'country':'cn',
        'fact':'captain',
    },
    'shanghai':{
        'pop':'*****',
        'country':'cn',
        'fact':'modern',
    },
    'tianjin':{
        'pop':'***',
        'country':'cn',
        'fact':'many of my friends there'
    },
}
for city,cityinfo in cities.items():
    print(f"As for the city {city.title()},the pop is {cityinfo['pop'].title()},"
          f"the country is {cityinfo['country'].title()},the fact is that it is {cityinfo['fact'].title()}")