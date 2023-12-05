from typing import List

file = open('input.txt')
data = file.read().split('\n\n')
file.close()

class Map:
    def __init__(self, sources: List[int], destinations: List[int], ranges: List[int]):
        self.source = sources
        self.destination = destinations
        self.range = ranges

    def get_mapping(self, value: int) -> int:
        for i in range(len(self.source)):
            if self.source[i] <= value <= self.source[i] + self.range[i]:
                offset = value - self.source[i]
                return self.destination[i] + offset
        return value


def create_map(lines: List[str]) -> Map:
    sources = []
    destinations = []
    ranges = []
    for line in lines.split(':')[1].strip().split('\n'):
        values = list(map(int, line.strip().split()))
        sources.append(values[1])
        destinations.append(values[0])
        ranges.append(values[2])
    return Map(sources, destinations, ranges)

seeds = list(map(int, data[0].split(': ')[1].strip().split()))
seed_to_soil = create_map(data[1])
soil_to_fertilizer = create_map(data[2])
fertilizer_to_water = create_map(data[3])
water_to_light = create_map(data[4])
light_to_temperature = create_map(data[5])
temperature_to_humidity = create_map(data[6])
humidity_to_location = create_map(data[7])

order = [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location]

locations = []
for seed in seeds:
    for method in order:
        seed = method.get_mapping(seed)
    locations.append(seed)

print(min(locations))
