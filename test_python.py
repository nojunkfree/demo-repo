import yaml

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
        
stringname=yaml.dump(thisdict)
f = open("output.yml", "w")
f.write(stringname)
f.close()

print("Hello World")
