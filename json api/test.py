import json
text = """
{
  "name":"Mandipa Thapa",
  "age":23,
  "graduated_from":"Kathmandu Engineering College",
  "interests":["fashion","makeup","data analysis"]
}
"""
obj = json.loads(text)
print(obj)
print(obj["name"])