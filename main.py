import http.client
from termcolor import colored

API_KEY = "87f0b316e0msh4395b1db710fb7ep19b3ddjsnc06bdf0b304b"
API_HOST = "bin-info-checker-api.p.rapidapi.com"

def get_bin_info(bin_number):
    conn = http.client.HTTPSConnection(API_HOST)

    headers = {
        'X-RapidAPI-Key': API_KEY,
        'X-RapidAPI-Host': API_HOST
    }

    conn.request("GET", f"/info?bin={bin_number}", headers=headers)

    res = conn.getresponse()
    data = res.read().decode("utf-8")

    return data

def format_bin_info(bin_info):
    bin_data = bin_info[1:-1].split(',')
    formatted_info = []
    for entry in bin_data:
        if ':' in entry:
            key, value = entry.split(':', 1)
            formatted_info.append([key.strip('"'), value.strip('"')])
        else:
            formatted_info.append([entry.strip('"'), ""])
    return formatted_info

def main():
    bin_number = input("Enter the BIN number to get information: ")
    bin_info = get_bin_info(bin_number)
    formatted_info = format_bin_info(bin_info)

    print(colored("+----------------+", 'grey'))
    for info in formatted_info:
        print(colored(f"| {info[0]:<15}| {info[1]:<15}|", 'cyan'))
    print(colored("+----------------+", 'grey'))

if __name__ == "__main__":
    main()
