import codecs;
from math import sqrt;

users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},

"Bill":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},

"Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},

"Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},

"Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},

"Jordyn": {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},

"Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},

"Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
}

class recommender:
	def __init__(self, data, k=1, metric='pearson', n=5):
		""" initialize recommender currently, if data is dictionary the recommender is initialized to it.
				For all other data types of data, no initialization occurs k is the k value for k nearest neighbor metric is which distance formula to 					use n is the maximum number of recommendations to make"""
		self.k=k;
		self.n=n;
				
		self.username2id={};
		self.userid2name={};
		self.productid2name={};
				
		self.metric=metric;
		if self.metric == 'pearson':
			self.fn=self.pearson
					
		if type(data).__name__ == 'dict':
			self.data=data;
	
	def convertProductID2name(self, id):
		"Given product id number return product name"
		if id in self.productid2name:
			return self.productid2name[id]
		else:
			#print("The id of Product Not Found, %s"%(id));
			return str(id);
	
	def userRatings(self, id, n):
		"""Return n top ratings for user with id"""
		print("Ratings for " + self.userid2name[id]);
		ratings=self.data[id];
		print("The Length of ratings is: %d"%(len(ratings)));
		ratings=list(ratings.items())
		ratings=[(self.convertProductID2name(k), v) for(k, v) in ratings];
		
		#finally sort and return 
		ratings.sort(key=lambda artistTuple: artistTuple[1], reverse=True);
		ratings=ratings[:n];
		#print("The Final Ratings is: ", ratings);
		for rating in ratings:
			print("%s\t%i"%(rating[0], rating[1]));
	
	def loadBookDB(self, path=''):
		"""loads the BX book dataset. Path is where the BX files are located"""
		self.data={};
		i=0;
		#
		# First load book ratings into self.data
		#
		with codecs.open(path+"BX-Book-Ratings.csv", 'r', 'latin-1', errors="replace") as f:
			for line in f:
				#line=line.encode('utf-8').strip();
				i+=1;
				print("Line of BX-Book-Ratings.csv is: %s"%line);
				user='';
				book='';
				rating=0.0;
				# separate line into fields
				fields=line.split(';');
				user=fields[0].strip('"');
				book=fields[1].strip('"');
				#print ("Rating before conversation: ", fields[2].strip().strip('"'))
				if not isinstance(fields[2].strip().strip('"'), basestring):
					#print ("The Type of Rating is: ", type(fields[2].strip().strip('"')).__name__);
					rating=float(fields[2].strip().strip('"'));
				else:
					pass;
					#print ("Rating Not Float Value: ", fields[2].strip().strip('"'))

				#print("User: %s, Book: %s, Ratings: %s"%(user, book, rating));
				if user in self.data:
					currentRatings=self.data[user];
				else:
					currentRatings={};
				currentRatings[book]=rating;
				#print("The Current Ratings are for user: ",user, currentRatings);
				self.data[user]=currentRatings;
				#print("The Data for User:%s, is: %s"%(user, self.data[user]));
			f.close();
	#
	# Now load user info into both self.userid2name and
	# self.username2id
	#
		f = codecs.open(path + "BX-Users.csv", 'r', 'utf8')
		for line in f:
			i+=1
			# separate line into fields
			fields=line.split(';')
			userid=fields[0].strip('"')
			location=fields[1].strip('"');
			if len(fields)>3:
				age=fields[2].strip().strip('"');
			else:
				age='NULL';
		
			if age != 'NULL':
				value = location + ' (age: ' + age + ')'
			
			else:
				value=location;
			#print ("The Value for userid: %s is: %s"%(userid, value));
			self.userid2name[userid]=value;
			self.username2id[location]=userid;
		f.close();
		#print ("The value of i is: %d"%(i));
	
	def pearson(self, rating1, rating2):
		sum_xy	=0;
		sum_x 	=0;
		sum_y 	=0;
		sum_x2 	=0;
		sum_y2 	=0;
		n=0;
		
		for key in rating1:
			if key in rating2:
				n+=1;
				x=rating1[key];
				y=rating2[key];
				sum_xy+=x*y;
				sum_x +=x;
				sum_y	+=y;
				sum_x2+=x**2;
				sum_y2+=y**2;
				
		if n == 0:
			return 0;
		
		# now compute denominator
		denominator=(sqrt(sum_x2 - sum_x**2/n) * sqrt(sum_y2 - sum_y**2/n));
		
		if denominator == 0:
			return 0;
		else:
			return (sum_xy - (sum_x * sum_y)/n)/denominator;
			
	def computeNearestNeighbor(self, username):
		"""Creates a sorted list of users based on their distance to username"""
		distances=[];
		for instance in self.data:
			if instance != username:
				distance=self.fn(self.data[username], self.data[instance]);
				distances.append((instance, distance));
		# sort based on disance -- closest first
		distances.sort(key=lambda artistTuple: artistTuple[1], reverse=True);
		return distances;
	
	def recommend(self, user):
		"""Given list of recommendations"""
		recommendations={};
		# first get list of users ordered by nearness
		nearest=self.computeNearestNeighbor(user);
		#
		# now get the ratings for the user
		#
		userRatings=self.data[user];
		#
		# determine the total distance
		#
		totalDistance=0.0;
		for i in range(self.k):
			#nearest[i][1] is the pearson value for i-th value
			totalDistance+=nearest[i][1]*1.0;
		# now iterate through the k nearest neighbors
		# accumulating their ratings
		for i in range(self.k):
			# compute slice of pie
			weight=nearest[i][1]/totalDistance;
			#get the name of the person
			name=nearest[i][0];
			#get The ratings for this person
			neighborRatings=self.data[name];
			# get the name of the person
			# now find bands neighbor rated that user didn't
			for artist in neighborRatings:
				if not artist in userRatings:
					if artist not in recommendations:
						recommendations[artist]=(neighborRatings[artist]*weight);
					else:
						recommendations[artist]=(recommedations[artist] + neighborRatings[artist] * weight);
		# now make list from dictionary
		recommendations=list(recommendations.items());
		recommendations=[(self.convertProductID2name(k), v) for(k,v) in recommendations];
		
		# finally sort and return
		recommendations.sort(key=lambda artistTuple: artistTuple[1], reverse=True);
		
		# Return The first n items
		return recommendations[:self.n]
		
r=recommender(users);
print r.recommend('Jordyn');
print r.recommend('Hailey');
r.loadBookDB('./');
print ("Loaded Book DB Successfully");
print "The recommendation for 171118 is: ", r.recommend('171118');
print "The User Ratings 171118 for 5 is: ", r.userRatings('171118', 5);
