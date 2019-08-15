data = '''
{
  "Name": "Alan",
  "Details": {
    "Age": "20",
    "Sex": "Male"
  },
  "Degree": {
    "hide": "Yes"
  }
}'''

import json

result = json.loads(data)
print(result)   # The type of result is dictionary so we did not need to use other method to decode it.
print(result["Name"])
print(result["Degree"]["hide"])



data = '''
[
  {
    "Name": "Alan",
    "Age": "25"
  },
  {
    "Name": "Jeon",
    "Age": "24"
  }
]'''

import json

result = json.loads(data)
print(len(result))
print(result)

for item in result:
    print("Name is: " + item['Name'])
    print("Age is: " + item['Age'])
