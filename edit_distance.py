def edit_distance(str1, str2, m , n):

    # If first string is empty, the only option is to
    # insert all characters of second string into first
    if m==0:
         return n

    # If second string is empty, the only option is to
    # remove all characters of first string
    if n==0:
        return m

    # If last characters of two strings are same, nothing
    # much to do. Ignore last characters and get count for
    # remaining strings.
    if str1[m-1]==str2[n-1]:
        return edit_distance(str1,str2,m-1,n-1)

    # If last characters are not same, consider all three
    # operations on last character of first string, recursively
    # compute minimum cost for all three operations and take
    # minimum of three values.
    return 1 + min(edit_distance(str1, str2, m, n-1),    # Insert
                   edit_distance(str1, str2, m-1, n),    # Remove
                   edit_distance(str1, str2, m-1, n-1)    # Replace
                   )

# Driver program to test the above function
def call_edit_distance(str1, str2):
    print("Edit distance: " + str(edit_distance(str1, str2, len(str1), len(str2))))

# This code is contributed by Bhavya Jain