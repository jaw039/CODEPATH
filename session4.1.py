def navigate_research_station(station_layout, observations):
    starting_index = 0  
    total = 0          
    
    for char1 in observations:
        for index, char2 in enumerate(station_layout):
            if char1 == char2:
                total += abs(starting_index - index)
                starting_index = index

    
    return total

station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

print(navigate_research_station(station_layout1, observations1))  
print(navigate_research_station(station_layout2, observations2))

