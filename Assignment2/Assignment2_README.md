### Function Design Recipe
Your functions will fall into three categories: functions for data formatting, functions for data queries, and functions for data modification. The functions for data queries and modification will all work with data formatted as described above.

Functions to write for A2
Function name:
(Parameter types) -> Return type	Full Description (paraphrase to get a proper docstring description)
get_bridge:
(list[list], int) -> list	
The first parameter represents the bridge data, and the second parameter represents the id of a bridge. The function should return the data of the bridge with the given id. If there is no bridge with the given id, the function should return the empty list.

For example, when called with the example THREE_BRIDGES as the first argument and 1 as the second argument, the function should return:

[1, 'Highway 24 Underpass at Highway 403', '403', 43.167233, -80.275567, '1965', '2014', '2009', 4,
 [12.0, 19.0, 21.0, 12.0], 65, '04/13/2012', [72.3, 69.5, 70.0, 70.3, 70.5, 70.7, 72.9]]
	  
get_average_bci:
(list[list], int) -> float	
The first parameter represents the bridge data, and the second parameter represents the id of a bridge. The function should return the average BCI of the bridge with the given id. If there is no bridge with the given id, the function should return zero. If there are no BCIs for the bridge with the given id, the function should return zero.

For example, when called with the example THREE_BRIDGES as the first argument and 1 as the second argument, the function should return approximately 70.8857.

get_total_length_on_hwy:
(list[list], str) -> float	
The first parameter represents the bridge data, and the second parameter represents the highway. The function should return the total length of bridges on that highway. If there are no bridges on the highway, the function should return zero.

For example, when called with the example THREE_BRIDGES as the first argument and '403' as the second argument, the function should return 126.0.

get_distance_between:
(list, list) -> float	
The two parameters represent two bridges. The function should return the distance in kilometres, rounded to the nearest metre (i.e., 3 decimal places), between them.

For example, if the first argument is the bridge from THREE_BRIDGES with id 1, i.e., the bridge [1, 'Highway 24 Underpass at Highway 403', '403', 43.167233, -80.275567, '1965', '2014', '2009', 4, [12.0, 19.0, 21.0, 12.0], 65.0, '04/13/2012', [72.3, 69.5, 70.0, 70.3, 70.5, 70.7, 72.9]], and the second argument is the bridge from THREE_BRIDGES with id 2, i.e. the bridge [2, 'WEST STREET UNDERPASS', '403', 43.164531, -80.251582, '1963', '2014', '2007', 4, [12.2, 18.0, 18.0, 12.2], 61.0, '04/13/2012', [71.5, 68.1, 69.0, 69.4, 69.4, 70.3, 73.3]], then the function should return 1.968.

Hint: use a provided helper function calculate_distance to calculate the distance.

get_closest_bridge:
(list[list], int) -> int	
The first parameter represents the bridge data, and the second parameter represents the id of a bridge. The function should return the id of a bridge that has the shortest distance to the bridge with the given id. (The function should not return the bridge with the given id itself, i.e., we do not consider a bridge to be closest to itself!) You may assume that the bridge with the given id is present in the bridge data, and that there are at least two bridge in the bridge data.

For example, when called with the example THREE_BRIDGES as the first argument and 2 as the second argument, the function should return 1.

Hint: use the function get_distance_between.

get_bridges_in_radius:
(list[list], float, float, float) -> list[int]	
The first parameter represents the bridge data, the second and third parameters represent the location (latitude and longitude), and the fourth parameter represents a radius/distance. The function should return a list of ids of all bridges that are within the given distance of the given location.

For example, when called with the example THREE_BRIDGES, 43.10, -80.15, and 50 as arguments, the function should return the list [1, 2].

get_bridges_with_bci_below:
(list[list], list[int], float) -> list[int]	
The first parameter represents the bridge data, the second parameter represents a list of bridge ids, and the third parameter represents a BCI. The function should return a list of ids of all bridges whose ids are in the given list of ids and whose BCI is less than or equal to the given BCI.

For example, when called with the example THREE_BRIDGES, the list of ids [1, 2], and the BCI limit 72, the function should return the list [2].

get_bridges_containing:
(list[list], str) -> list[int]	
The first parameter represents the bridge data, and the second parameter represents a search string. The function should return a list of ids of all bridges whose names contain the search string. The search should be case-insensitive.

For example, when called with the example THREE_BRIDGES and the search string 'underpass', the function should return the list [1, 2]. Note that when called with the example THREE_BRIDGES and the search string 'pass', the function should also return the list [1, 2], i.e. the function looks for part of the name, not necessarily the entire name.

inspect_bridges:
(list[list], list[int], str, float) -> None	
The first parameter represents the bridge data, the second parameter represents a list of bridge IDs, the third parameter represents a date, and the fourth parameter represents a BCI. The function should update the bridges with the given IDs with the new given date and the new given BCI score for a new inspection. If there is no corresponding bridge for one or more of the given bridge ids in the given data, the function has no effect for that bridge id.

For example, if the function is called with the example THREE_BRIDGES, a list of one ID [1], date '09/15/2023', and BCI 71.9, then after the call the bridge data THREE_BRIDGES should contain all the same data, except the first bridge record should become:

[1, 'Highway 24 Underpass at Highway 403', '403', 43.167233, -80.275567, '1965', '2014', '2009', 4,
 [12.0, 19.0, 21.0, 12.0], 65, '09/15/2023', [71.9, 72.3, 69.5, 70.0, 70.3, 70.5, 70.7, 72.9]]
	  
add_rehab:
(list[list], int, str, bool) -> None	
The first parameter represents the bridge data, the second parameter represents a bridge ID, the third parameter represents a date, and the fourth parameter represents whether the rehab is major (argument is True) or minor (argument is False). The function should update the bridge with the given ID with the new rehab year record: year of major rehab, if the last argument is True, and year of minor rehab if the last argument is False. If there is no bridge with the given id in the given bridge data, the function has no effect.

For example, if the function is called with the example THREE_BRIDGES, the ID 1, date '09/15/2023', and False, then after the call the bridge data THREE_BRIDGES should contain all the same data, except the first bridge record should become:

[1, 'Highway 24 Underpass at Highway 403', '403', 43.167233, -80.275567, '1965', '2014', '2023', 4,
 [12.0, 19.0, 21.0, 12.0], 65, '04/13/2012', [72.3, 69.5, 70.0, 70.3, 70.5, 70.7, 72.9]],
	  
format_data:
(list[list[str]]) -> None	
See Formatting the data.

assign_inspectors:
(list[list], list[list[float]], int) -> list[list[int]]	
The first parameter represents the bridge data, the second parameter represents a list of locations of inspectors (pairs of latitude and longitude), and the third parameter represents the maximum number of bridges that should be assigned to any inspector. The function should return a list of bridge IDs to be assigned to each inspector.

See Assigning inspectors for the rules and the algorithm.

For example, when called with the example THREE_BRIDGES, the list of inspector locations [[43.20, -80.35], [45.0368, -81.34]], and the bridge limit of 2, the function should return the list [[1, 2], [3]].

Assigning Inspectors (function assign_inspectors)
Bridge condition indices (BCI) represent the condition of a bridge on a past inspection, and we use the most recent BCI to prioritise certain bridges. There are three levels of priorities, with their upper limits represented by the constants HIGH_PRIORITY_BCI, MEDIUM_PRIORITY_BCI, LOW_PRIORITY_BCI, constrained by HIGH_PRIORITY_BCI < MEDIUM_PRIORITY_BCI < LOW_PRIORITY_BCI.

For example, if HIGH_PRIORITY_BCI is 60, then all bridges with their most recent BCI less than or equal to 60 are considered 'high priority'. Similarly, if MEDIUM_PRIORITY_BCI is 70, then all bridges with a BCI less than or equal to 70 (but > 60) are considered 'medium priority'.

When assigning bridges to inspectors, we want to prioritise nearby high priority bridges within a large radius of the inspector over medium priority bridges that are closer, and both of those are prioritised over low priority bridges in an even smaller radius.

The radii are specified by the constants HIGH_PRIORITY_RADIUS, MEDIUM_PRIORITY_RADIUS, and LOW_PRIORITY_RADIUS.

You are told the maximum number of bridges to assign per inspector. The way we want to assign bridges to inspectors is as follows:

High priority bridges with a distance <= HIGH_PRIORITY_RADIUS from the inspector.
If (1) assigned fewer than the maximum number of bridges, then we go on to assign medium priority bridges with a distance <= MEDIUM_PRIORITY_RADIUS from the inspector.
If (1) and (2) still assigned fewer than the given maximum number of bridges, then we go on to assign low priority bridges with a distance <= LOW_PRIORITY_RADIUS from the inspector.
One inspector at a time, we assign the maximum number of bridges to each inspector (or fewer than the maximum number of bridges, if all bridges have already been assigned). Inspectors should be assigned bridges based on the order they appear in the list (e.g., the first inspector in the list should be assigned up to the maximum number of bridges first, the second inspector should be assigned up to the maximum number of bridges next, and so on).

Bridges are assigned to an inspector using as many bridges that fulfil (1) as possible, followed by (2), and then (3) if there are still fewer than the maximum number of bridges assigned to that inspector. If there are multiple bridges with the same priority and radius, we choose the bridge with the lowest ID (e.g., if there are two low priority bridges with IDs 3 and 4, we would assign the bridge with ID 3 first). Each bridge should be assigned to at most one inspector.

Hint: You may want to use the get_bridges_in_radius and get_bridges_with_bci_below functions to help you with assigning inspectors.
