import requests
import time

# URL of the website to monitor
url_to_monitor = "https://example.com"


# Function to fetch website data
def fetch_website_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to fetch data from {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred while fetching data: {e}")


# Function to save data to a local file
def save_data_locally(data, filename):
    try:
        with open(filename, "a") as file:
            file.write(data + "\n")
        print(f"Data saved to {filename} successfully.")
    except Exception as e:
        print(f"An error occurred while saving data: {e}")


# Main function
def main():
    local_filename = "website_data.txt"

    while True:
        # Fetch website data
        website_data = fetch_website_data(url_to_monitor)

        if website_data:
            # Save data to a local file
            save_data_locally(website_data, local_filename)

        # Set the monitoring interval (in seconds)
        time.sleep(60)  # Example: 1 minute


if __name__ == "__main__":
    main()
