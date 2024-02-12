from dataclasses import dataclass
from geopy.geocoders import Nominatim
from geopy.distance import geodesic


@dataclass
class Coordinates:
    lat: float
    lng: float

    def coordinates(self):
        return self.lat, self.lng


def get_coordinates(address: str):
    geolocator = Nominatim(user_agent='distance_calculator')
    location = geolocator.geocode(address)

    if location:
        return Coordinates(location.latitude, location.longitude)


def calculate_distance_km(home: Coordinates, target: Coordinates):
    if home and target:
        distance: float = geodesic(home.coordinates(), target.coordinates()).kilometers
        return distance


def get_distance_km(home_address: str, target_address: str):
    home_coordinates: Coordinates = get_coordinates(home_address)
    target_coordinates: Coordinates = get_coordinates(target_address)

    if distance := calculate_distance_km(home_coordinates, target_coordinates):
        print(f'{home_address} -> {target_address}')
        print(f'{distance:.2f} kilometers')
        return distance
    else:
        print('Failed to calculate the distance.')


def main():
    home_address: str = 'Delhi'
    target_address: str = input('Enter an address: ')
    print(f'Home address: {home_address}')

    print('Calculating...')
    get_distance_km(home_address,target_address)


if __name__ == '__main__':
    main()
