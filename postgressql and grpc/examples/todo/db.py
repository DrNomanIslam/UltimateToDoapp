import psycopg2
hostname = 'localhost'
username = 'postgres'
password = 'kishwar1'
database = 'todo'

class DB:
    
    
    def __init__(self):
        pass        


    def addToDo(self,id,description, title,done):               
        self.myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
        query="insert into Tasks(id,title,description,done) values('"+id+"','"+title+"','"+description+"','"+ done +"');"
        cur = self.myConnection.cursor()
        cur.execute(query)
        self.myConnection.commit()
        self.myConnection.close()

    def update_task(self,id,description, title,done):               
        self.myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
        query="update Tasks set id='"+id+"',title='"+title+"', description='"+description+"',done='"+done+"' where id='"+id+"';"
        cur = self.myConnection.cursor()
        cur.execute(query)
        self.myConnection.commit()
        self.myConnection.close()
        
    def remove_task(self,id):               
        self.myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
        query="delete from Tasks where id='"+id+"';"
        cur = self.myConnection.cursor()
        cur.execute(query)
        self.myConnection.commit()
        self.myConnection.close()

    def get_all(self):
        self.myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
        query="select * from Tasks;"
        cur = self.myConnection.cursor()
        cur.execute(query)
        l=[]
        for id, title, description, done in cur.fetchall() :
            d={}
            d["id"]=id
            d["title"]=title
            d["description"]=description
            d["done"]=done
            l.append(d);
        self.myConnection.close()
        return l

    def get_task(self,id):
        self.myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
        query="select * from Tasks where id='"+id+"';"
        cur = self.myConnection.cursor()
        cur.execute(query)
        d={}
        for id, title, description, done in cur.fetchall() :

            d["id"]=id
            d["title"]=title
            d["description"]=description
            d["done"]=done
        self.myConnection.close()
        return d