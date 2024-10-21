# Author: David S. Harmor
# Course : CS 340
# Application: Animal shelter driver
#
# DSH 9-15-2004 - inital
#               - implimented Create and Insert functions
# DSH 10-2-2024 - 
#

from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self,username,password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        #USER = 'aacuser'
        #PASS = 'Yptz693'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32711
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (username,password,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
        
    def create(self, data=None):
       try:        
         # test if we have valid information
         if isinstance(data, (list, dict, tuple,MongoClient())):
             if data is not None:
                 result = self.database.animals.insert_many(data)  # data should be dictionary
    
                 if result.inserted_ids  != 0:  # Test if data was successful
                    return True
                 else:
                    return False # Return False on failure
             else:
               return False
                
       except Exception:            
            raise Exception("Error when creating data")
            
            
    # Complete this create method to implement the R in CRUD

    def read(self, criteria=None):
                                  
        try:
          # test if we have valid information
          if isinstance(criteria, (list, dict, tuple)):                             
               try:
                   if criteria is not None: # Test if there are any entries
                      # If entries read the database for what is required
                      data = self.database.animals.find(criteria,{"_id": False})                                      
                   else:
                      # No reuirments display all entries
                      data = self.database.animals.find({},{"_id": False})
                      
                   return data # Return the dataset
               except Exception:
                      raise Exception("There was an error with reading with the parameters  :" + str(criteria));           
        except Exception:
           raise Exception("Error reading database")
           
              
       # Create method to implement the U in CRUD.
    def update(self, initial, change=None):
        # test if we have valid information
        if isinstance(initial, (list, dict, tuple))  and isinstance(change, (list, dict, tuple)): 
            if (initial is not None) and (change is not None): #Test if there are no entries
                if self.database.animals.count_documents(initial, limit = 1) != 0:
                    update_result = self.database.animals.update_many(initial,{"$set":change})
                    result = update_result.modified_count #Return the number of records modified
                else:
                    result = 0 #No records were modified
                return result
        else:
            raise Exception("Update failed:")\
                

    # Create method to implement the D in CRUD.
    def delete(self, criteria=None):
        # test if we have valid information
        if isinstance(criteria, (list, dict, tuple,)): 
            if criteria is not None:  #Test if there are no entried
                if self.database.animals.count_documents(criteria, limit = 1) != 0:
                    delete_result = self.database.animals.delete_many(criteria)                 
                    result = delete_result.deleted_count #Return the number of records mondified
                else:
                    result = 0 #No records were modified
            return result
        else:
            raise Exception("Error in operateion :"+str(criteria))
    
    
      