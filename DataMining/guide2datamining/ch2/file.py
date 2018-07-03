import csv;
reader=csv.reader(open("./BX-Book-Ratings.csv", 'r'));
for row in reader:
	print "Row is: ", row[0].split(';');
	#print "Type of row is: ", type(row).__name__;
	#print "length of row is: ", len(row);
