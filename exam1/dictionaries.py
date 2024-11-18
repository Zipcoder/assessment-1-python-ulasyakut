
def delete_keys_from_dict(datadict, keylist):
    """
    Delete a list of keys from a dictionary
    """
    d = datadict.copy()
    for i in keylist:
        d.pop(i)

    return d

def check_dict_for_key(datadict, key):
    """
    Check if a value exists in a dictionary
    (NO FOR loops!)
    """
    pass

def get_key_of_min_value(ddd):
    """
    Get the key of the minimum value from a dictionary
    """
    value = min(ddd.values())
    for key,val in ddd.items():
        if val == value:
            return key

def get_key_of_max_value(ddd):
    """
    Get the key of the maximum value from a dictionary
    """
    value = max(ddd.values())
    for key,val in ddd.items():
        if val == value:
            return key

def letterfreq(word):
    '''
    # Write a function that returns a dictionary of letter frequencies from a word
    '''
    

    pass