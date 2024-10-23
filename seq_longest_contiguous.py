def longest_contiguous(seq):
    """
    Count the length of the longest contiguous subsequences.

    This function finds each contiguous subsequence in ``seq``,
    e.g. ``aaaa`` or ``bb`` and counts its length and returns the
    letter with the longest contiguous subsequence and its length.

    It returns a dictionary with the key being the letter and the
    value being the length of the longest subsequence. If two letters
    have longest subsequences of the same length, both are included
    separately in the dictionary.

    Each unique letter in ``seq`` is counted separately so the
    sequence "aabbcc" will find the longest subsequences of each of
    "a", "b" and "c".

    If ``seq`` is empty then an empty dicitonary is returned.

    Args:
        seq (Bio.Seq.Seq): A sequence of characters.

    Returns:
        dict: The count of the longest subsequences, keyed by letter.

    Examples:
        >>> longest_contiguous("aacbbb")
        {'b': 3}
        >>> longest_contiguous("aabbbaabbc")
        {'b': 3}
        >>> longest_contiguous("aaabbbaabb")
        {'a': 3, 'b': 3}
    """
    
    result_dict = {}
    
    max_len = 0
    
    current_char = None
    
    current_len = 0
    
    for char in seq:
        
        if char == current_char:
            current_len += 1
            
        else:
            current_char = char
            current_len = 1
        
        if current_len > max_len:
            max_len = current_len
            result_dict = {current_char: max_len}
            
        elif current_len == max_len:
            result_dict[current_char] = max_len

    return result_dict