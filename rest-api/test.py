import requests

# Making a get request
response = requests.get('https://ubt24-node01.jtest.pivotal.io', verify ='./incus-ui.crt')

# print request object
print(response)

