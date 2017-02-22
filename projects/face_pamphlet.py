'''
This is the starter code for the 
face-pamphlet assignment
TODO: replace this (and all) header comment(s)
with your own!
'''

# Assignment idea from Stanford CS106A
# assume all friendships go both ways
# e.g. if A is a friend of B, then B is
# a friend of A

__author__ = '' # put your name here

class SocialNetwork:

    def __init__(self): # feel free to modify this as necessary
        self.friends = {} # friend (string) -> set of friends (set of strings)

    def add_connection(self, person1, person2): 
        '''
        person1 and person2 are now friends with each other
        '''
        pass

    def remove_connection(self, person1, person2):
        '''
        person1 and person2 are no longer friends with each other
        (throw errors as appropriate)
        '''
        pass

    def degrees_of_separation(self, person1, person2): # challenge!
        '''
        What's the smallest number of friends that separate
        these two?
        '''
        pass

    def is_reachable(self, person1, person2):
        '''
        Return bool: is there a path of friends
        between person1 and person2
        '''
        pass

    def is_friend(self, person1, person2):
        '''
        Returns bool: is person1 a friend of person2?
        '''
        pass

    def get_mutual_friends(self, person1, person2):
        '''
        Return a set of the mutual friends of person1
        and person2
        '''
        pass

    def get_num_friends(self, person1):
        '''
        Return the number of friends of person1
        '''
        pass

    def read_friends_from_file(self, path):
        '''
        Input format:
        <person1 name> <friend1> <friend2> ...
        <person2 name> <friend1> <friend2> ...
        ...

        Initialize the newtork from a file
        '''
        with open(path, 'r') as f: # opens file in read mode (first token is friend, all others )
            pass

    def write_friends_to_file(self, path):
        '''
        Write the social network to a file
        in the format described in 
        read_friends_from_file
        '''
        pass

def main():
    '''
    TODO: test your network out over here!
    '''
    pass

if __name__ == '__main__':
    main()








