'''
1. Create one new PET - POST
2. Check if it is in available pets - GET
3. update the pet to sold state - POST/PUT
4. Check if the pet moved to sold state
5. delete the pet - DELETE
6. verify if it is deleted - GET
https://petstore.swagger.io/
'''

import requests
import json

PET_API = 'https://petstore.swagger.io/v2/pet'
data = {
  "id": 3212111,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Alex",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}


headers = {'accept': 'application/json',
           'Content-Type': 'application/json'}

# 1. Create a new pet
res = requests.post(PET_API, data=json.dumps(data), headers=headers)
assert res.status_code == 200, "Pet did not get created successfully"

# 2. Check if it is in available pets - GET
params = {'status': 'available'}
res = requests.get(PET_API + '/findByStatus', headers=headers, params=params)
assert res.status_code == 200, "No pets in available status"
pets = res.json()
for pet in pets:
    if pet['id'] == 3212111:
        assert pet['name'] == "Alex", "Name is not proper"
        assert pet['status'] == "available"
        break
else:
    assert True, "Alex Pet is not in available list"

# 3. update the pet to sold state - POST/PUT
data['status'] = 'sold'
res = requests.put(PET_API, data=json.dumps(data), headers=headers)
assert res.status_code == 200, "Pet is not sold"

# 4. Check if the pet moved to sold state
params = {'status': 'sold'}
res = requests.get(PET_API + '/findByStatus', headers=headers, params=params)
assert res.status_code == 200, "No pets in available status"
pets = res.json()
for pet in pets:
    if pet['id'] == 3212111:
        assert pet['name'] == "Alex", "Name is not proper"
        assert pet['status'] == "sold", "Status is not sold"
        break
else:
    assert True, "Alex Pet is not in sold list"

# 5. delete the pet - DELETE
res = requests.delete(PET_API + '/%d'%data['id'], headers=headers)
assert res.status_code == 200, "Pet is not deleted"

# 6. verify if it is deleted - GET
res = requests.delete(PET_API + '/%d'%data['id'], headers=headers)
assert res.status_code == 404, "Pet is still there"


