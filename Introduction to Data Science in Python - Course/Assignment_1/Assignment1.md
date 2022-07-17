
# Assignment 1
For this assignment you are welcomed to use other regex resources such a regex "cheat sheets" you find on the web.



Before start working on the problems, here is a small example to help you understand how to write your own answers. In short, the solution should be written within the function body given, and the final result should be returned. Then the autograder will try to call the function and validate your returned result accordingly.


```python
def example_word_count():
    # This example question requires counting words in the example_string below.
    example_string = "Amy is 5 years old"

    result = example_string.split(" ")
    return len(result)

```

## Part A

Find a list of all of the names in the following string using regex.


```python
import re

def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old.
    Ruth and Peter, their parents, have 3 kids."""

    a = re.findall('[A-Z]\w+',simple_string)
    return a

names()
```
```
    ['Amy', 'Mary', 'Ruth', 'Peter']
```


## Part B

The dataset file in [assets/grades.txt](assets/grades.txt) contains a line separated list of people with their grade in
a class. Create a regex to generate a list of just those students who received a B in the course.


```python
import re

def grades():
    with open ("assets/grades.txt", "r") as file:
        grades = file.read()

    people = re.findall('[\w]*\ [\w]*(?=:\ B)', grades)

    return people

grades()

```
```
    ['Bell Kassulke',
     'Simon Loidl',
     'Elias Jovanovic',
     'Hakim Botros',
     'Emilie Lorentsen',
     'Jake Wood',
     'Fatemeh Akhtar',
     'Kim Weston',
     'Yasmin Dar',
     'Viswamitra Upandhye',
     'Killian Kaufman',
     'Elwood Page',
     'Elodie Booker',
     'Adnan Chen',
     'Hank Spinka',
     'Hannah Bayer']
```


## Part C

Consider the standard web log file in [assets/logdata.txt](assets/logdata.txt). This file records the access a user makes when visiting a web page (like this one!). Each line of the log has the following items:
* a host (e.g., '146.204.224.152')
* a user_name (e.g., 'feest6811' **note: sometimes the user name is missing! In this case, use '-' as the value for the username.**)
* the time a request was made (e.g., '21/Jun/2019:15:45:24 -0700')
* the post request type (e.g., 'POST /incentivize HTTP/1.1' **note: not everything is a POST!**)

Your task is to convert this into a list of dictionaries, where each dictionary looks like the following:
```
example_dict = {"host":"146.204.224.152",
                "user_name":"feest6811",
                "time":"21/Jun/2019:15:45:24 -0700",
                "request":"POST /incentivize HTTP/1.1"}
```


```python
import re

def logs():
    with open("assets/logdata.txt", "r") as file:
        logdata = file.read()

    pattern = '''
    (?P<host>\d+(?:\.\d+){3})
    \s+\S+\s+
    (?P<user_name>\S+)\s+\[
    (?P<time>[^\]\[]*)\]\s\"
    (?P<request>.*)\"\s+
    '''

    result = list()
    for item in re.finditer(pattern, logdata, re.VERBOSE):
        result.append(item.groupdict())

    return result

logs()

```
```
    [{'host': '146.204.224.152',
      'user_name': 'feest6811',
      'time': '21/Jun/2019:15:45:24 -0700',
      'request': 'POST /incentivize HTTP/1.1'},
     {'host': '197.109.77.178',
      'user_name': 'kertzmann3129',
      'time': '21/Jun/2019:15:45:25 -0700',
      'request': 'DELETE /virtual/solutions/target/web+services HTTP/2.0'},
     {'host': '156.127.178.177',
      'user_name': 'okuneva5222',
      'time': '21/Jun/2019:15:45:27 -0700',
      'request': 'DELETE /interactive/transparent/niches/revolutionize HTTP/1.1'},
     {'host': '100.32.205.59',
      'user_name': 'ortiz8891',
      'time': '21/Jun/2019:15:45:28 -0700',
      'request': 'PATCH /architectures HTTP/1.0'},
     {'host': '168.95.156.240',
      'user_name': 'stark2413',
      'time': '21/Jun/2019:15:45:31 -0700',
      'request': 'GET /engage HTTP/2.0'},
     {'host': '71.172.239.195',
      'user_name': 'dooley1853',
      'time': '21/Jun/2019:15:45:32 -0700',
      'request': 'PUT /cutting-edge HTTP/2.0'},
      ....
```

```python
assert len(logs()) == 979

one_item={'host': '146.204.224.152',
  'user_name': 'feest6811',
  'time': '21/Jun/2019:15:45:24 -0700',
  'request': 'POST /incentivize HTTP/1.1'}
assert one_item in logs(), "Sorry, this item should be in the log results, check your formating"

```
