import argparse, re, io
import numpy as np


# Compute the Euclidean distance score between user1 and user2 
def euclidean_score(dataset, user1, user2):
    if user1 not in dataset:
        raise TypeError('Cannot find ' + user1 + ' in the dataset')

    if user2 not in dataset:
        raise TypeError('Cannot find ' + user2 + ' in the dataset')

    # Movies rated by both user1 and user2
    common_movies = {} 

    for item in dataset[user1]:
        if item in dataset[user2]:
            common_movies[item] = 1

    # If there are no common movies between the users, 
    # then the score is 0 
    if len(common_movies) == 0:
        return 0

    squared_diff = [] 

    for item in dataset[user1]:
        if item in dataset[user2]:
            squared_diff.append(np.square(dataset[user1][item] - dataset[user2][item]))
        
    return 1 / (1 + np.sqrt(np.sum(squared_diff)))

# Compute the Pearson correlation score between user1 and user2 
def pearson_score(dataset, user1, user2):
    if user1 not in dataset:
        raise TypeError('Cannot find ' + user1 + ' in the dataset')

    if user2 not in dataset:
        raise TypeError('Cannot find ' + user2 + ' in the dataset')

    # Movies rated by both user1 and user2
    common_movies = {}

    for item in dataset[user1]:
        if item in dataset[user2]:
            common_movies[item] = 1

    num_ratings = len(common_movies) 

    # If there are no common movies between user1 and user2, then the score is 0 
    if num_ratings == 0:
        return 0

    # Calculate the sum of ratings of all the common movies 
    user1_sum = np.sum([dataset[user1][item] for item in common_movies])
    user2_sum = np.sum([dataset[user2][item] for item in common_movies])

    # Calculate the sum of squares of ratings of all the common movies 
    user1_squared_sum = np.sum([np.square(dataset[user1][item]) for item in common_movies])
    user2_squared_sum = np.sum([np.square(dataset[user2][item]) for item in common_movies])

    # Calculate the sum of products of the ratings of the common movies
    sum_of_products = np.sum([dataset[user1][item] * dataset[user2][item] for item in common_movies])

    # Calculate the Pearson correlation score
    Sxy = sum_of_products - (user1_sum * user2_sum / num_ratings)
    Sxx = user1_squared_sum - np.square(user1_sum) / num_ratings
    Syy = user2_squared_sum - np.square(user2_sum) / num_ratings
    
    if Sxx * Syy == 0:
        return 0

    return Sxy / np.sqrt(Sxx * Syy)




def build_arg_parser():
    parser = argparse.ArgumentParser(description='Find users who are similar to the input user')
    parser.add_argument('--user', dest='user', required=True,
            help='Input user')
    return parser

# Finds users in the dataset that are similar to the input user 
def find_similar_users(dataset, user, num_users):
    if user not in dataset:
        raise TypeError('Cannot find ' + user + ' in the dataset')

    # Compute Pearson score between input user 
    # and all the users in the dataset
    scores = np.array([[x, pearson_score(dataset, user, 
            x)] for x in dataset if x != user])

    # Sort the scores in decreasing order
    scores_sorted = np.argsort(scores[:, 1])[::-1]

    # Extract the top 'num_users' scores
    top_users = scores_sorted[:num_users] 

    return scores[top_users] 

''' Function sorting data extracted from JSON based on similair_users list'''
def sort_data_similair_users_data(data, similar_users):
    data_from_similair_users = {}
    for item in similar_users:
        #print(item[0]+"-----------")
        for movie, score in data[item[0]].items():
            if(movie not in user_data):
                #print(movie+" "+str(score))
                data_from_similair_users[movie] = score
            #print(data[item[0]])
    return sorted(data_from_similair_users.items(), key=lambda kv: kv[1])

'''Function extracting movie name from data using regex '''
def return_data(start_index, to_index, step, data):
    temp_array = []
    for i in range (start_index, to_index , step):
        match = re.match(r"^.*\'(.*)\'.*$",data[i].__str__())
        #print(match.group(1))
        temp_array.append( match.group(1))
        #print(sorted_data_from_similair_users[i])
    return temp_array

'''Function preprocessing file structure (getting rid of file header)'''
def file_preprocess(csv_file):
    
    temp_data = []
    final_data = []
    line_count = 0
    with open(csv_file, 'r', encoding = "utf-8") as file:
        for line in file:
            temp_data.append(line)
            line_count += 1
    for id in range(1,len(temp_data)):
        final_data.append(temp_data[id])
    #print(final_data)
    return final_data, line_count-1

'''Function converting headerless csv file to dictonary '''
def convert_csv_to_dict(csv_file, line_count):
    data = {}
    temp_array = []
    temp_row = {}
    csv_file.seek(0)
    
    for line_id in range (0,line_count):
        current_line_data = csv_file.readline()
        temp_array.append(re.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)", current_line_data))
        temp_dict = {}
        length = len(temp_array[line_id])
        for item in range(3,length,2):
            if not temp_array[line_id][item] == '':         
                if not item+2 >= length:
                    temp_dict[temp_array[line_id][item-1]] = int(temp_array[line_id][item])
        temp_row[temp_array[line_id][0]] = temp_dict
    data = temp_row
    #print(data)
    
    return data

if __name__=='__main__':
    args = build_arg_parser().parse_args()
    user = args.user
    number_of_users = 3
    csv_file = "Dane_filmowe.csv"
    counter = 0
    
    return_file = io.StringIO()
    #Load data and complete preprocessing
    data_preprocess, line_count = file_preprocess(csv_file) 

    #Write data into in-memory file
    for item in data_preprocess:
        return_file.write(item)
    #Convert in-memory file data to dictonary
    data = convert_csv_to_dict(return_file, line_count)
    
    print('\nUsers similar to ' + user + ':\n')
    similar_users = find_similar_users(data, user, number_of_users) 
    print('User\t\t\tSimilarity score')
    print('-'*41)
    for item in similar_users:
        print(item[0], '\t\t', round(float(item[1]), 2))
    
    #Contains movies that user rated
    user_data = data[user]
    recommended_data = []
    unrecommended_data = []
    data_from_similair_users = {}

    #Create sorted list containing movie data
    sorted_data_from_similair_users = sort_data_similair_users_data(data, similar_users)
    
    start_index = len(sorted_data_from_similair_users)-1
    to_index = len(sorted_data_from_similair_users)-11
    #Create recommended movies data based on sorted list of movie data
    recommended_data = return_data(start_index,to_index, -1, sorted_data_from_similair_users)
    
    start_index = 0
    to_index = 10
    #Create unrecommended movies data based on sorted list of movie data
    unrecommended_data = return_data(start_index,to_index, 1, sorted_data_from_similair_users)
    
    return_file.close()
    
    print("\n")
    print("Recommended Movies Array for "+user+":")
    print(recommended_data)   
    print("Unrecommended Movies Array for "+user+":")
    print(unrecommended_data)   