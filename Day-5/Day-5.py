#%%
with open('./input.txt') as file:
    data = file.read().splitlines()


# %%
seeds = data[0].split(' ')[1:]
seeds = [int(i) for i in seeds]

class Map():
    def __init__(self):
        self.source_name = None
        self.destination_name = None
        self.mapping = []
    def map_value(self,value):
        for row in self.mapping:
            source = row["source"]
            destination = row["destination"]
            map_range = row["map_range"]
            if value in range(source,source+map_range+1):
                diff = value - source
                return destination + diff
        else:
            return value
        
mapCategories = []
mapCategory = None
for ind,row in enumerate(data[1:]):
    if row == "":
        continue
    if ind == len(data[1:])-1:
        mapCategories.append(mapCategory)
    if "map" in row:
        if mapCategory != None: mapCategories.append(mapCategory)
        mapCategory = Map()
        source_dest = row.split(" ")[0].split("-to-")
        mapCategory.source_name = source_dest[0]
        mapCategory.destination_name = source_dest[1]
    else:
        mapCategory.mapping.append({"source": int(row.split(" ")[1]),
                                 "destination": int(row.split(" ")[0]), 
                                 "map_range": int(row.split(" ")[2])})

# %%
seed_location = []
for seed in seeds:
    for mapCategory in mapCategories:
        seed = mapCategory.map_value(seed)
    seed_location.append(seed)
min(seed_location)
# %%
seed_ranges = [seeds[x:x+2] for x in range(0,len(seeds),2)]
seed_range_locations = []
seed_locations = []
for seed_range in seed_ranges:
    for i in range(seed_range[1],seed_range[0]+1):
        for mapCategory in mapCategories:
            location = mapCategory.map_value(i)
        seed_location.append(location)
    seed_range_locations.append(seed_location)
# %%
