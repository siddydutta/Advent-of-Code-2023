from typing import List
from tqdm import tqdm
data = '''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4'''
data = data.split('\n\n')

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

seed_ranges = list(map(int, data[0].split(': ')[1].strip().split()))
seeds = list()
for i in tqdm(range(0, len(seed_ranges), 2)):
    for j in range(seed_ranges[i+1]):
        seeds.append(seed_ranges[i]+j)

seed_to_soil = create_map(data[1])
soil_to_fertilizer = create_map(data[2])
fertilizer_to_water = create_map(data[3])
water_to_light = create_map(data[4])
light_to_temperature = create_map(data[5])
temperature_to_humidity = create_map(data[6])
humidity_to_location = create_map(data[7])

order = [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location]

locations = []
for seed in tqdm(seeds):
    for method in tqdm(order):
        seed = method.get_mapping(seed)
    locations.append(seed)

print(min(locations))
