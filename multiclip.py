import json
import clipboard
import sys

SAVED_DATA = 'clipboard.json'

def save_clip(filepath, data):
    '''
    function to save to clipboard
    Args:
    filepath: filepath to be saved to
    data: data to be saved to clip
    '''
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)
        
def load_clip(filepath):
    '''function to load text in clipboard
    Args:
    filepath: path of file
    Return: data saved in clipboard
    '''
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data
    except:
        return {}
        
if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_clip(SAVED_DATA)
    
    if command == 'save':
        key = input('Enter a key to save with: ')
        data[key] = clipboard.paste()
        save_clip(SAVED_DATA, data)
        print('Data saved')
        
    elif command == 'load':
        key = input('Enter key saved with: ')
        if key in data:
            clipboard.copy(data[key])
            print('Copied to clipboard')
        else:
            print("Key doesn't exist")
    elif command == 'list':
        print(data)
    else:
        print('Unknown Command')
else:
    print('Please enter exactly 1 commands')
