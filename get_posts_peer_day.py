from read_data import fromJson


def get_posts_peer_day(day:str)->int:
    """
    Return the number of posts for given day

    Args:
        data (dict): a dictionary of posts

    Returns: 
        dict: a dictionary with the number of posts for each month
    """
    return