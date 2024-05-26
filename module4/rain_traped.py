def calculate_trapped_water(terrainLevels):
    left = 0
    right = len(terrainLevels) - 1
    left_max = right_max = total_water = 0
    while left <= right:
        if terrainLevels[left] <= terrainLevels[right]:
            left_max = max(left_max, terrainLevels[left])
            water_level = left_max - terrainLevels[left]
            total_water += water_level
            left += 1
        else:
            right_max = max(right_max, terrainLevels[right])
            water_level = right_max - terrainLevels[right]
            total_water += water_level
            right -= 1

    return total_water
num=[5,3,0,2,0,4]

print(calculate_trapped_water(num))