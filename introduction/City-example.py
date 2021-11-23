from app import db, Countries, Cities

db.drop_all()
db.create_all() # Creates all table classes defined

countries = [
    "United Kingdom",
    "France",
    "South Korea",
    "Ireland",
    "Japan",
    "Nigeria"
]

for country in countries:
    new_country = Countries(name = country)
    db.session.add(new_country)
    db.session.commit()
    
cities = [
    ("London", "United Kingdom"),
    ("Manchester", "United Kingdom"),
    ("Tokyo", "Japan"),
    ("Dublin", "Ireland")
]

for city in cities:
    new_city = Cities(name = city[0], country = Countries.query.filter_by(name=city[1]).first())
    db.session.add(new_city)
    db.session.commit()

all_countries = Countries.query.all()

for country in all_countries:
    print(f"Country name: {country.name}")
    print(f"Cities in {country.name}:")
    for city in country.cities:
        print(f"- {city.name}")
    print()