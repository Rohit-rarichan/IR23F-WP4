import API
import file_io
import visualization


def main():
    # Get user input
    api_url = get_user_input()

    # Fetch data from API
    data = API.fetch_data_from_api(api_url)

    # Write data to file
    file_io.write_data_to_file(data, 'data.json')

    # Generate visualization
    visualization.generate_visualization(data)


def get_user_input():
    api_url = input("Enter API URL: ")
    return api_url

if __name__ == "__main__":
    main()
