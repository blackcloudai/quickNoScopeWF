import sys

def contains_query_words(field_value, query_words):
    return any(word in field_value for word in query_words)

# Field name to index and label mapping
field_mappings = {
    'A': {'index': 0, 'label': 'timestamp'},
    'B': {'index': 1, 'label': 'eventName'},
    'C': {'index': 2, 'label': 'foobar'},
    'D': {'index': 3, 'label': 'metadata'}  # Add other fields as necessary
}

# Input file path
input_file = 'your_log_file.log'

# Process the log file
with open(input_file, 'r') as infile:
    # Default behavior: print all fields with labels
    if len(sys.argv) == 1:
        for line in infile:
            fields = line.strip().split()
            for key, value in field_mappings.items():
                if value['index'] < len(fields):
                    print(f"{value['label']}({key}): {fields[value['index']]}")
            print()  # Print a newline between entries

    # Specific field or metadata with query
    else:
        field_key = sys.argv[1]
        query_words = sys.argv[2:] if len(sys.argv) > 2 else None

        if field_key in field_mappings:
            for line in infile:
                fields = line.strip().split()
                if field_mappings[field_key]['index'] < len(fields):
                    field_value = fields[field_mappings[field_key]['index']]

                    # Print field value or apply query if it's metadata
                    if field_key != 'D' or not query_words or contains_query_words(field_value, query_words):
                        print(field_value)
