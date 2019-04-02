
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  5 11:38:58 2014

@author: zzhang
"""
import pickle

class Index:
    def __init__(self, name):
        self.name = name
        self.msgs = [];
        self.index = {}
        self.total_msgs = 0
        self.total_words = 0
        
    def get_total_words(self):
        return self.total_words
        
    def get_msg_size(self):
        return self.total_msgs
        
    def get_msg(self,n):
        return self.msgs[n]
        
    # implement
    def add_msg(self, m):
        self.msgs.append(m)
        self.total_msgs +=1
        
        
    def add_msg_and_index(self, m):
        self.add_msg(m)
        line_at = self.total_msgs - 1
        self.indexing(m, line_at)

    # implement
    def indexing(self, m, l):
        
        word_list = m.split()
        for word in word_list:
            if word not in self.index.keys():
                
                self.index[word] = [l]
                
            else:
                
                self.index[word].append(l)
                
                
                

                    
    def search(self, term):
        msgs = []
        
        
        for line in self.index[term]:
            
            msgs.append((line,self.msgs[line]))
        
        return msgs
    
    



class PIndex(Index):
    
    
    def __init__(self, name):
        super().__init__(name)
        roman_int_f = open('roman.txt.pk', 'rb')
        self.int2roman = pickle.load(roman_int_f)
        roman_int_f.close()
        self.load_poems()
        
        # implement: 1) open the file for read, then call
        # the base class's add_msg_and_index
    def load_poems(self):
        
        lines= open(self.name,'r').readlines()
        
        for i in lines:
            i=i.strip('\n')
            self.add_msg_and_index(i)
            
        return self.index        
        

    
        # implement: p is an integer, get_poem(1) returns a list,
        # each item is one line of the 1st sonnet
    def get_poem(self, p):
        poem = []
        
        start_romnum = self.int2roman[p] + '.'
        end_romnum = self.int2roman[p+1] + '.'
        
        list1= self.search(start_romnum)
        list2=self.search(end_romnum)
        
        for i in range(list1[0][0],list2[0][0]):
            
            poem.append(self.msgs[i])
        
        return  poem

if __name__ == "__main__":
    sonnets = PIndex("AllSonnets.txt")

    # the next two lines are just for testing
    
    s_love = sonnets.search("love")
    
    p3= sonnets.get_poem(50)
    print(s_love)
    print(p3)
    
    
    
    
