import json

#the data below is dict because it started with {}
data = '''
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

info = json.loads(data) #this is dict
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])
