#CJ Patel
#Task21 - loop_lists.py
#------------------------------------------------------------#
#list of 5 favourite movies
favMovies = ['Hunt for the Wilderpeople', 'The Hobbit', 'LOTR', 'Deadpool', 'Harry Potter']

#print index and elements of list using enumerate method
for index,element in enumerate(favMovies):
	print("Movie " + str(index+1) + ": " + element)
