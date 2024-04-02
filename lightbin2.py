import http.client
import json
import csv
import argparse

def get_bin_info(bin_number, verbose=False):
    if verbose:
        print("Fetching information for BIN number:", bin_number)
    conn = http.client.HTTPSConnection("neutrinoapi-bin-lookup.p.rapidapi.com")

    payload = f"bin-number={bin_number}&customer-ip=60.234.81.148"

    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'X-RapidAPI-Key': "87f0b316e0msh4395b1db710fb7ep19b3ddjsnc06bdf0b304b",
        'X-RapidAPI-Host': "neutrinoapi-bin-lookup.p.rapidapi.com"
    }

    conn.request("POST", "/bin-lookup", payload, headers)

    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")

def format_bin_info(bin_info):
    bin_info_dict = json.loads(bin_info)
    return bin_info_dict

def main():
    parser = argparse.ArgumentParser(description='LightBIN - A BIN lookup tool')
    parser.add_argument('-b', '--bin', type=str, required=True, help='Single BIN number to get information')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose mode')
    parser.add_argument('-o', '--output', choices=['json', 'csv'], help='Output format (JSON or CSV)')
    args = parser.parse_args()

    bin_info = get_bin_info(args.bin, args.verbose)
    formatted_info = format_bin_info(bin_info)

    if args.output == 'json':
        print(json.dumps(formatted_info, indent=4))
        with open(f'{args.bin}.json', 'w') as json_file:
            json.dump(formatted_info, json_file, indent=4)
    elif args.output == 'csv':
        with open(f'{args.bin}.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Attribute', 'Value'])
            for key, value in formatted_info.items():
                writer.writerow([key, value])
        print(f"Information saved in {args.bin}.csv")
    else:
        print(f"BIN Number: {args.bin}")
        for key, value in formatted_info.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    main()
