import os
import time

# Configuration
downloads_folder = 'C:/Users/YourUsername/Downloads'  # Replace with your actual Downloads folder path
max_file_age_days = 30  # Adjust the threshold as needed (e.g., 30 days)


def clean_downloads_folder(folder_path, max_age_days):
    current_time = time.time()

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Check if it's a file and older than the threshold
        if os.path.isfile(file_path):
            file_age_seconds = current_time - os.path.getctime(file_path)
            file_age_days = file_age_seconds / (60 * 60 * 24)  # Convert seconds to days

            if file_age_days >= max_age_days:
                try:
                    os.remove(file_path)
                    print(f"Deleted: {filename}")
                except Exception as e:
                    print(f"Failed to delete {filename}: {str(e)}")


if __name__ == '__main__':
    clean_downloads_folder(downloads_folder, max_file_age_days)
