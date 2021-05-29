import requests, json

class RestPython:

    def restPython(self):
        response = requests.get("http://api.open-notify.org/astros.json")
        data = response.json()
        lis = data['people']
        sortedByName = sorted(lis, key=lambda i: i['name'])
        print("Sorted order by names: ",sortedByName)

        for i in sortedByName:
            print(i['name'])


if __name__ == "__main__":
    a = RestPython()
    a.restPython()