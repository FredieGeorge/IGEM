import requests

# Microsoft Graph API endpoint for messages in a channel
url = "https://graph.microsoft.com/v1.0/teams/{teamId}/channels/{channelId}/messages"

# Replace {teamId} and {channelId} with your specific team and channel IDs
team_id = "your_team_id"
channel_id = "your_channel_id"

# Set your access token obtained through authentication
access_token = "your_access_token"

headers = {
    "Authorization": f"Bearer {access_token}",
}

# Optional parameters for filtering or pagination
params = {
    # You can add filters like $filter=createdDateTime ge 2023-01-01T00:00:00Z
    # More options are available in the Microsoft Graph API documentation.
}

try:
    response = requests.get(url.format(teamId=team_id, channelId=channel_id), headers=headers, params=params)
    
    if response.status_code == 200:
        messages = response.json()
        with open("saved_messages.txt", "w") as file:
            for message in messages['value']:
                file.write(f"Message ID: {message['id']}\n")
                file.write(f"Author: {message['from']['user']['displayName']}\n")
                file.write(f"Message: {message['body']['content']}\n\n")
        print("Messages saved to 'saved_messages.txt'")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

except Exception as e:
    print(f"An error occurred: {e}")