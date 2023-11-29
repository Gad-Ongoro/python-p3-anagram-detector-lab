# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, anagram_list):
        count = 1
        result_list = []

        while count > 0:
            for word in anagram_list:
                anagram_letters = [char for char in word]
                if sorted(anagram_letters) == sorted(self.word):
                    result_list.append(word)
            count -= 1
            
        return(result_list)                
    pass

listen = Anagram("enlist")
print(listen.match([ "silent", "listen", "hippopotamus"]))