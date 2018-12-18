#Data Source :http://www.grouplens.org/node/73 
import pandas as pd  # first time it loades cache it will take some time to Run it 
import os.path # To check if Src data files are there or not 
def perpare_user():
	
	# Get the coulumn whatever needed for Analysis and report  
	unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
	users = pd.read_table('ml-1m/usersmin.dat', sep='::', header=None,names=unames,engine = 'python')
	return users
def perpare_movies():
	
	# Get the coulumn whatever needed for Analysis and report  
	unames = ['movie_id', 'title', 'genres'] # genres has several types 
	users = pd.read_table('ml-1m/moviesmin.dat', sep='::', header=None,names=unames,engine = 'python')
	return users

def perpare_ratings():
	
	# Get the coulumn whatever needed for Analysis and report  
	unames = ['user_id', 'movie_id', 'rating', 'timestamp']# mapping between user and movies with its own fields
	users = pd.read_table('ml-1m/ratingsmin.dat', sep='::', header=None,names=unames,engine = 'python')
	return users
if __name__=="__main__":
	if os.path.isfile('ml-1m/users.dat'):
		print("user is there ")
		users=perpare_user()
	
	if os.path.isfile('ml-1m/ratings.dat'):
		print("ratings is there ")
		ratings=perpare_ratings()


	if os.path.isfile('ml-1m/movies.dat'):
		print("movies is there ")
		movies=perpare_movies()
	raw_input("Enter Anything ")
	print(type(users),len(users))


	#merge operation should have common filed name so users to ratings to movies 
	data = pd.merge(pd.merge(ratings, users), movies)
	
	raw_input("Enter Anything ")
	print("Merged Items  **************************************************")
	print(data[:5])

	raw_input("Enter Anything ")
	#Value: Amount to be shown as groupby aggregation (This is Summed,Avged,Varienced) No values from frmw perspective we jsut take count 
	#coulumn : All types in columns are counted on value given .
	#Index: List of Items to identify the Value  	
	mean_ratings = data.pivot_table(values='rating',index=['title','genres'], columns='gender', aggfunc='mean')
	print("PIVOT TABLE  **************************************************")
	print("Ex: Showing Mean ratings of Movies(Title and genre) given by each gender i.e F and M ")
	print(mean_ratings[:5])

	
	raw_input("Enter Anything ")
	#Groupby : Groupby on possible groups including columns (gender)
	# get the agg function on this group and seperate the column 
	#unstack : remove the group which you wanna show as columns 
	print("GROUP BY   **************************************************")
	print("EX: Groupby Movies(Title and genre) by gender i.e F and M showing Average ratings ")
	mean_ratings = data.groupby(['title','genres','gender'])['rating'].mean().unstack('gender')
	print(mean_ratings[:5])

	raw_input("Enter Anything ")
	#lets groupby only a feild  and get the size of the memebers in teh group  
	mean_ratingsgrpby = data.groupby('title').size()
	active_titles = mean_ratingsgrpby.index[mean_ratingsgrpby < 3]
	print("INDEXING*******************************************************")
	print("List of only titles as indexes ")
	print(active_titles[:5])
	# Use this indexes to  get all the corresposnding ro w fields data from the meanreating 
	Lesser_ratings = mean_ratingsgrpby.ix[active_titles]
	print("EX: Creating a data frame where rating < 3 ie Select * from data groupby titles  where ratings < 3  ")
	print(Lesser_ratings[:5])

	#Sort the data by a field F ratings in Ascending order 	
	top_female_ratings = mean_ratings.sort_values(by='F', ascending=False)
	raw_input("Enter Anything ")
	print("SORTING********************************************************")
	print("Top 3 female ratings ")
	print(top_female_ratings[:3])

	#Subtract two cloumns and set as a new column in mean rating data 
	mean_ratings['diff']=  mean_ratings['M'] - mean_ratings['F'] 
	top_diff_ratings = mean_ratings.sort_values(by='diff', ascending=False)
	raw_input("Enter Anything ")
	print("DIFFERENCE********************************************************")
	print("Top 3 differnce ratings ")
	print(top_diff_ratings[:3])
	
	#Subtract two cloumns and set as a new column in mean rating data 
	mean_ratings['diff']=  mean_ratings['M'] - mean_ratings['F'] 
	top_diff_ratings = mean_ratings.sort_values(by='diff', ascending=False)
	raw_input("Enter Anything ")
	print("DIFFERENCE********************************************************")
	print("Top 3 differnce ratings ")
	print(top_diff_ratings[:3])

	rating_std_by_title = data.groupby('title')['rating'].std()	
	
