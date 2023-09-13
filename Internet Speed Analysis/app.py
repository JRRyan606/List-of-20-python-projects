import requests
import matplotlib.pyplot as plt
import time
import webbrowser
from bs4 import BeautifulSoup


# Function to measure internet speed using fast.com
def get_speed():
    url = "https://fast.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    speed = soup.find("div", {"id": "speed-value"}).text
    return float(speed)  # Speed is in Mbps


# Main function
def main():
    download_speeds = []
    timestamps = []

    # Number of measurements and time interval (in seconds)
    num_measurements = 10
    interval = 5

    for _ in range(num_measurements):
        download_speed = get_speed()
        timestamp = time.strftime('%H:%M:%S')

        download_speeds.append(download_speed)
        timestamps.append(timestamp)

        time.sleep(interval)

    # Plotting the results
    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, download_speeds, marker='o', label='Download Speed (Mbps)')
    plt.title('Internet Speed Analysis')
    plt.xlabel('Time')
    plt.ylabel('Speed (Mbps)')
    plt.legend()
    plt.grid(True)

    # Save the plot as an image file
    image_filename = 'internet_speed_plot.png'
    plt.savefig(image_filename)

    # Open the image file in a web browser
    webbrowser.open('file://' + image_filename, new=2)


if __name__ == "__main__":
    main()
