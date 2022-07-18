import pymongo
client = pymongo.MongoClient("mongodb+srv://Prem:Mongo1234@cluster0.pomoe.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d ={
    "name":"prem",
    "email" :"premnichat@gmail.com",
    "surname" : "nichat"
}
