import json
data = "    {\"pk\": 1,    \"value\": \"Toss Team\",    \"is_active\": true,    \"parent\": null  },  {    \"pk\": 2,    \"value\: \"송금\",    \"is_active\": true,    \"parent\": 1  },  {    \"pk\": 3,    \"value\": \"착오송금\",    \"is_active\": true,    \"parent\": 2  }"

def get_summary(data, target_value):
    data = json.loads(data)
    print(data)
    data.sort(key=lambda x:x.parent)
    print(data)

get_summary(data, 0)