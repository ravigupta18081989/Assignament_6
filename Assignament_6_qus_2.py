import json

dictionary = { 
        "1" : {
    "state name" : "Rajasthan",
    "capitals" : "Jaipur"
},
"2" : {
    "state name" : "Goa",
    "capitals" : "Panaji"
},

"3" :{
    "state name" : "Karnataka",
    "capitals" : "Bengaluru"
},

"4" :{
    "state name" : "Bihar",
    "capitals" : "Patna"
},

"5" :{
    "state name" : "Tamil nadu",
    "capitals" : "Chennai"
},

"6" :{
    "state name" : "Uttar Pradesh",
    "capitals" : "Lucknow"
},

"7" :{
    "state name" : "West Bengal",
    "capitals" : "Kolkata"
}}


json_object = json.dumps(dictionary,indent=7)
print(json_object)