'''
Check if doors are open 100 passes
Start with 100 doors and they are all closed.
Every time you pass by you open the door if it closed then you open it, it if is open then you close it.
The first time you pass by every door. The second time you only visit every 2nd door (#2, #4, #6, ...).
The third time, every 3rd door (#3, #6, #9, ...), etc., until you only visit the 100th door.
Return only the doors that are open.
'''


def open_doors() -> list[int]:
	# False = Closed
	# True = Open
	total_doors = []
	for door in range(100):
		total_doors.append(False)

	check = 1
	for passes in range(1, 100):
		for door in range(0, 100, check):
			total_doors[door] = not total_doors[door]
		check += 1
	
	opened_doors = []
	for door in range(100):
		if total_doors[door]:
			opened_doors.append(door)
	
	return opened_doors

print(open_doors())
	