from math import sqrt;

users = {
	"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 			2.5, "Vampire Weekend": 2.0},
	
	"Bill": {"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
	
	"Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0,

	"Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},

	"Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
	
	"Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},

	"Jordyn": {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},

	"Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},

	"Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
}

def manhattan(rating1, rating2):
	"""Computes the Manhattan distance. Both rating1 and rating2 are
dictionaries of the form
{'The Strokes': 3.0, 'Slightly Stoopid': 2.5 ..."""
	distance=0;
	for key in rating1:
		if key in rating2:
			distance += abs(rating1[key] - rating2[key]);
	return distance;

def computeNearestNeighbor(username, users):
	"""creates a sorted list of users based on their distance to username"""
	distances=[];
	for user in users:
		if user != username:
			distance = manhattan(users[username], users[user]);
			distances.append((distance, user));
			
	# sort deppending on the first key
	distances.sort();
	return distances;

def minkowski(rating1, rating2, r):
	"""Computes the Minkowski distance.
	Both rating1 and rating2 are dictionaries of the form
	{'The Strokes': 3.0, 'Slightly Stoopid': 2.5}
	"""
	distance = 0
	commonRatings = False
	for key in rating1:
		if key in rating2:
			distance += pow(abs(rating1[key] - rating2[key]), r)
			commonRatings = True
		
	if commonRatings:
		#print distance**(1/r)
		return pow(distance, 1/r)
	else:
		return 0 #Indicates no ratings in common

def pearson(rating1, rating2):
	sum_xy = 0
	sum_x = 0
	sum_y = 0
	sum_x2 = 0
	sum_y2 = 0
	n = 0
	for key in rating1:
		if key in rating2:
			n += 1
			x = rating1[key]
			y = rating2[key]
			sum_xy += x * y
			sum_x += x
			sum_y += y
			sum_x2 += x**2
			sum_y2 += y**2
	# if no ratings in common return 0
	if n == 0:
		return 0
	# now compute denominator
	denominator = sqrt(sum_x2 - (sum_x**2) / n) * sqrt(sum_y2 - (sum_y**2) / n)
	if denominator == 0:
		return 0
	else:
		return (sum_xy - (sum_x * sum_y) / n) / denominator;
		
def recommend(username, users):
	"""Give list of recommendations"""
	# first find nearest neighbor
	nearest = computeNearestNeighbor(username, users)[0][1];
	recommendations = [];
	# now find bands neighbor rated that user didn't
	neighborRatings = users[nearest];
	userRatings = users[username];
	for artist in neighborRatings:
		if not artist in userRatings:
			recommendations.append((artist, neighborRatings[artist]))
	# using the fn sorted for variety - sort is more efficient
	return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse = True)

for key in users:
	print key, "--> ", users[key];
print "\t\t", "*"*30;

for user1 in users:
	for user2 in users:
		if user1 != user2:
			print "Manhattan Distance between ["+user1+"] and [" + user2 +"] is: " + str(manhattan(users[user1], users[user2]));

print "\t\t"+"*"*30;
for user in users:
	print "The distances of ["+user+"] is: " + str(computeNearestNeighbor(user, users));
print "\t\t"+"*"*30;

for user in users:
	print "The User is: ", user, ", we recommend: ", recommend(user, users);
print "\t\t"+"*"*30;

print pearson(users['Angelica'], users['Bill']),"\n";
print pearson(users['Angelica'], users['Hailey']), "\n";
print pearson(users['Angelica'], users['Jordyn']), "\n";
