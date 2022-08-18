# Adding Words


# You need to write a function that takes multiple words as its argument and returns a concatenated version of those words separated by dashes (-).
# The function should be able to take a varying number of words as the argument.

# Sample Input
# this
# is
# great

# Sample Output
# this-is-great

# Recall, using *args as a function parameter enables you to pass an arbitrary number of arguments to that function.


def concatenate(*args):
    words = []
    for w in args:
        words.append(w)
        
    def list_to_string(l):
        str = ''
        for i in l:
            str += i
            str = '-'.join(l)
        
        return(str)
    
    return list_to_string(words)

print(concatenate("I", "love", "Python", "!"))