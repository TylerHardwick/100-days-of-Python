import requests
from datetime import datetime
import os

USERNAME = "tjh"
TOKEN = os.environ.get("Pixela_token")
GRAPH = "codegraph"

pixela_endpoint = "https://pixe.la/v1/users"
pixela_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsofService": "yes",
    "notMinor": "yes"
}
# # Creating a user account:
# pixela_user_response = requests.post(url=pixela_endpoint, json=pixela_parameters)
# print(pixela_user_response.text)

pixela_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixela_graph_parameters = {
    "id": GRAPH,
    "name": "Code Study Graph",
    "unit": "minutes",
    "type": "int",
    "color": "ajisai",
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# # Creating a graph:
# graph_response = requests.post(url=pixela_graph_endpoint, json=pixela_graph_parameters, headers=headers)
# print(graph_response.text)

today = datetime.now()
ymd_today = today.strftime("%Y%m%d")

pixela_g_update_endpoint = f"{pixela_graph_endpoint}/{GRAPH}"
pixela_g_update_parameters = {
    "date": ymd_today,
    "quantity": "60"
}
# Adding to graph:
g_update_response = requests.post(url=pixela_g_update_endpoint, json=pixela_g_update_parameters, headers=headers)
print(g_update_response.text)

pixela_edit_endpoint = f"{pixela_g_update_endpoint}/{ymd_today}"
pixela_edit_parameters = {
    "quantity": input("How many minutes did you spend coding today?")
}

# # Update pixel in graph:
# pixela_edit_response = requests.put(url=pixela_edit_endpoint, json=pixela_edit_parameters, headers=headers)
# print(pixela_edit_response.text)

# # Delete a pixel in graph:
# pixela_delete_response = requests.delete(url=pixela_edit_endpoint, headers=headers)
# print(pixela_delete_response.text)
