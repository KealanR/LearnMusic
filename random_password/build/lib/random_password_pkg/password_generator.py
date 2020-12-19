import random
import string
class PasswordGenerator:
    
    #returns random string of lowercase letters
    def very_weak_password(self, length):
    
        pool = string.ascii_lowercase
        random_password = ""
        
        for i in range(length):
            random_password = random_password + random.choice(pool)
            
        return random_password
    
    #returns random string of lowercase + uppercase letters
    def weak_password(self, length):
    
        pool = string.ascii_lowercase+string.ascii_uppercase
        
        random_password = ""
        
        for i in range(length):
            random_password = random_password + random.choice(pool)
            
        return random_password
    
    #returns random string of lowercase + uppercase letters + numbers
    def mid_password(self, length):
    
        pool = string.ascii_lowercase+string.ascii_uppercase+string.digits
        
        random_password = ""
        
        for i in range(length):
            random_password = random_password + random.choice(pool)
            
        return random_password
    #returns random string of lowercase + uppercase letters + numbers + punctuation
    def strong_password(self,length):
    
        pool = string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation
        
        random_password = ""
        
        for i in range(length):
            random_password = random_password + random.choice(pool)
            
        return random_password
