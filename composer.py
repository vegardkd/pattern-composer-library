import sys
import urllib.request
import urllib.parse
import os
from datetime import datetime

def send_request(file_path):
    # Convert relative path to absolute path
    absolute_file_path = os.path.abspath(file_path)

    # Read content from the file
    with open(absolute_file_path, 'r') as file:
        code = file.read()

    # URL encode the content
    encoded_code = urllib.parse.quote(code)

    # Prepare the request URL
    request_url = f"https://composer-api.vercel.app/test-run?code={encoded_code}"

    # Send the request
    try:
        with urllib.request.urlopen(request_url) as response:
            if response.status == 200:
                # Saving the response content to a file
                date = datetime.now().strftime('%m-%d-%Y-%H.%M.%S')
                name = absolute_file_path.split(os.sep)[-1].replace('.py', '')
                output_file_name = f'{name}-{date}.mid'
                with open(f'./output/{output_file_name}', 'wb') as output_file:
                    output_file.write(response.read())
                print(f'{output_file_name} written to /ouput')
            else:
                print(f"Failed: {str(response.read())}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python composer.py <path_to_python_file>")
    else:
        send_request(sys.argv[1])
