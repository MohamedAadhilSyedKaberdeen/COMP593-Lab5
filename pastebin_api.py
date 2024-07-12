'''
Library for interacting with the PasteBin API
https://pastebin.com/doc_api
'''
import requests

PASTEBIN_API_POST_URL = 'https://pastebin.com/api/api_post.php'
API_DEV_KEY = 'FsNy6PWptnfKLuHk7WQXu99D0EEzAMAW'

def post_new_paste(title, body_text, expiration='1M', listed=True):
    """Posts a new paste to PasteBin

    Args:
        title (str): Paste title
        body_text (str): Paste body text
        expiration (str): Expiration date of paste (N = never, 10M = 10 minutes, 1H, 1D, 1W, 2W, 1M, 6M, 1Y)
        listed (bool): Whether paste is publicly listed (True) or not (False)
    
    Returns:
        str: URL of new paste, if successful. Otherwise None.
    """
    # Prepare the data to be sent as POST request
    data = {
        'api_dev_key': API_DEV_KEY,
        'api_option': 'paste',
        'api_paste_code': body_text,
        'api_paste_name': title,
        'api_paste_expire_date': expiration,
        'api_paste_private': 1 if not listed else 0
    }

    # Send POST request to PasteBin API
    try:
        response = requests.post(PASTEBIN_API_POST_URL, data=data)
        response.raise_for_status()  # Raise an error for bad response status
        return response.text  # Return the URL of the newly created paste
    except requests.exceptions.RequestException as e:
        print(f'Error occurred: {e}')
        return None

if __name__ == '__main__':
    # Example usage:
    title = 'Test Paste'
    body_text = 'This is a test paste.'
    expiration = '1M'  # 1 month expiration
    listed = False  # Not publicly listed
    paste_url = post_new_paste(title, body_text, expiration, listed)
    if paste_url:
        print(f'Paste created successfully: {paste_url}')
    else:
        print('Failed to create paste.')
