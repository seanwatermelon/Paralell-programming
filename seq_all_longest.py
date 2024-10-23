def all_longest(each_longest):
    """
    Find the longest subsequences across multiple sequences.

    This function combines the outputs from ``longest_contiguous``
    to a single dictionary. For each letter in each of the input
    dictionaries, the output will contain that letter as a key and
    the largest of all associated values as its value.

    Args:
        each_longest (list): A list of longest subsequence counts.

    Returns:
        dict: The largest values for each letter from the inputs.

    Examples:
        >>> all_longest([{"a": 4}, {"b": 6}])
        {'a': 4, 'b': 6}
        >>> all_longest([{"a": 4}, {"b": 6, "a": 2}])
        {'a': 4, 'b': 6}
        >>> all_longest([{"a": 4}, {"b": 10, "a": 2}])
        {'a': 4, 'b': 10}
        >>> all_longest([{"a": 4}, {"b": 6, "a": 2}, {"b": 10}])
        {'a': 4, 'b': 10}
    """
    
    merged_dict = {}
    
    for seq in each_longest:
        
        for key, value in seq.items():
            
            if key in merged_dict:
                
                merged_dict[key] = max(merged_dict[key], value)
                
            else:
                merged_dict[key] = value
                
    return merged_dict
