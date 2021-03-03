import pandas as pd
df = pd.read_csv('QnA/books.csv') # Library database read as csv
# create a hashmap key:[genre] value:array of [books]
# this divides the books based on genre 
booksmap = {}
for genre in df['Genre'].unique():
    booksmap[genre] = df[df['Genre'] == genre].sort_values('Title').reset_index() #  Sort the Title of the books in the file by alphabetical

# Compare two string equals are not 
def comparetext(str1, str2):   
    i = 0
    while i < len(str1) - 1 and str1[i] == str2[i]: 
        i += 1
    if str1[i] > str2[i]: 
        return -1 
    return str1[i] < str2[i]

# Modified Binary Search for book titles
def searchbook(arr, string, first, last):   
    if first > last:
        return -1 
    # Move mid to the middle 
    mid = (last + first) // 2 
    # If mid is empty , find closet non-empty string 
    if len(arr[mid]) == 0:       
        # If mid is empty, search in both sides of mid 
        # and find the closest non-empty string, and 
        # set mid accordingly. 
        left, right = mid - 1, mid + 1
        while True:           
            if left < first and right > last: 
                return -1                 
            if right <= last and len(arr[right]) != 0: 
                mid = right 
                break              
            if left >= first and len(arr[left]) != 0: 
                mid = left 
                break              
            right += 1
            left -= 1 
    # If str is found at mid 
    if comparetext(string, arr[mid]) == 0: 
        return mid  
    # If str is greater than mid 
    if comparetext(string, arr[mid]) < 0: 
        return searchbook(arr, string, mid+1, last)  
    # If str is smaller than mid 
    return searchbook(arr, string, first, mid-1)     


def binary2dSearch(mat, x):
    # Serach 2d matrix for given book title x
    for i in range(len(mat)):
        j_low = 0
        j_high = len(mat[i])-1
 
        # End the loop if it exceeds the size of array
        while (j_low <= j_high):
            
            # Mid point
            j_mid = (j_low + j_high) // 2
    
            # Element found at mid point
            if (mat[i][j_mid] == x):
                return i, j_mid
    
            # split fisrt half
            elif (mat[i][j_mid] > x):
                j_high = j_mid - 1
    
            # split second half
            else:
                j_low = j_mid + 1
        
    # Element not found
    return False, -1


while(True):
    print("\n-------------------------Welcome to Library Search-----------------------------\n")
    options = input("Press 1 to search by genre\nPress 2 to search all the books\n\n: ")
    if options == "1":
        print("Available Genre:\n")
        print(df['Genre'].unique())   
        genre = input("Enter Genre: ")
        n = len(booksmap[genre]['Title'])
        print(booksmap[genre])
        searchlist = booksmap[genre]['Title'].values.tolist()
        title = input("Enter Title: ")
        i = searchbook(searchlist, title, 0, n-1)
        print("Index: ",i)    
        if(i>0):
            print("\n---------------------\n")
            print(booksmap[genre].iloc[i])
            print("\n---------------------\n")
        else:
            print("Book not found!")
    elif options == "2":
        all_books = []
        for each_genre in booksmap:
            all_books.append(booksmap[each_genre]['Title'].values.tolist())
        
        print(all_books)
        title = input("Enter Title: ")
        m, n = binary2dSearch(all_books, title)
        if m:
            genre = list(booksmap.keys())[m]
            print("\n---------------------\n")
            print(booksmap[genre].iloc[n])
            print("\n---------------------\n")
    else:
        print("Invalid option selected\n\n")

