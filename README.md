# HNG_PROJECT
Building an api by calling GENDERIZE API

## CORE FEATURES
  - Request for a name and then calls the GENDERIZE API 
  - Display name and other features of the name called
  - Also display exact time the data was queryed 

## CALLING GENDERIZE API when a name is parsed
```
response = requests.get(GENDERIZE_API_URL, params={"name": name}, timeout=5)
``
These block of code request for a name that is queryed, then calls the genderize api 
...

### Writing some basic fuctions
The written code block below helps to in te error handling if the name does not meet the necessary requirement
```
 if not name:
        return error_response('Bad Request', 400)
    
    if not isinstance(name, str):
        return error_response('Unprocessable Entity', 422)
```

