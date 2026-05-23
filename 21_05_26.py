import json

dct={
  "center": "IT Academy",
  "branches": [
    {
      "name": "Chilonzor",
      "teachers": [
        { "id": 1, "name": "Ali", "subject": "Python", "experience": 5 },
        { "id": 2, "name": "Vali", "subject": "JavaScript", "experience": 3 }
      ],
      "students": [
        { "id": 101, "name": "Hasan", "course": "Python", "payment": 600000 },
        { "id": 102, "name": "Husan", "course": "JavaScript", "payment": 500000 }
      ]
    },
    {
      "name": "Yunusobod",
      "teachers": [
        { "id": 3, "name": "Aziza", "subject": "Python", "experience": 6 }
      ],
      "students": [
        { "id": 103, "name": "Malika", "course": "Python", "payment": 650000 }
      ]
    }
  ]
}

f=open("IT_Academy.json","w")

json.dump(dct,f,indent=4)

f.close()

f=open("IT_Academy.json")

natija=json.load(f)

#111111111111111111111111111111111111111111

# for i in natija["branches"]:
#     print(i["name"])


#222222222222222222222222222222222222222222


# for i in natija["branches"]:
#     for a in i["teachers"]:
#         if a["subject"]=="Python":
#             print(a)


#333333333333333333333333333333333333333

# for i in  natija["branches"]:
#     ism=i["name"]
#     count=len(i["students"])
#     print(ism+":",count)

#44444444444444444444444444444444444444444444


# max1=max(
#     (
#         (x["payment"],x["name"],i["name"])
#         for i in natija["branches"]
#         for x in i["students"]
#     )
# )
# print(max1)


#5555555555555555555555555555555555


# for i in natija["branches"]:
#     count=0
#     for x in i["students"]:
#         count+=x["payment"]
#     print(i["name"],":",count)


#66666666666666666666666666666666666

# for i in natija["branches"]:
#     for x in i["teachers"]:
#         if x["experience"]>5:
#             print("Teachers:",x["name"])


#77777777777777777777777777777777777777777777777

for i in natija["branches"]:
  n=True
  for x in i["students"]:
    if x["course"] !="Python":
      n=False
  if n:
    print(i["name"])   