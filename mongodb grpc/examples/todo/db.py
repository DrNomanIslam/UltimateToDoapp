import pymongo

class DB:
    
    
    def __init__(self):
        client = pymongo.MongoClient("mongodb://localhost")
        self.db = client.todo


    def addToDo(self,id,description, title,done):               
        data = {"id": id, "description": description, "title": title, "done": done}
        self.db.Tasks.insert_one(data)


    def update_task(self,id,description, title,done):               
        data = {"id": id, "description": description, "title": title, "done": done}
        self.db.Tasks.update_one({'id':id}, {"$set": data}, upsert=False)


    def remove_task(self,id):               
        self.db.Tasks.delete_one({'id':id})


    def get_all(self):
        data=[]
        for d in self.db.Tasks.find():
            data.append(d)
        return data

    def get_task(self,id):
        return self.db.Tasks.find_one({"id":id})
