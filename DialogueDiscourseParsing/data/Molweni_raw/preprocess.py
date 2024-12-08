import json

def remove_newlines_from_json(input_file, output_file):
    # Read the input JSON file
    with open(input_file, 'r') as f:
        data = json.load(f)  # Parse the JSON
    
    # Write the JSON data to the output file in a single line
    with open(output_file, 'w') as f:
        json.dump(data, f)  # Dumps the JSON data in a single line

# Specify the input and output file paths
input_file = 'input.json'  # Replace with your input file path
output_file = 'output.json'  # Replace with your desired output file path

# Remove newlines from JSON
remove_newlines_from_json("/DATA1/ritesh/baselines_discourse_parsing/DialogueDiscourseParsing/data/Molweni_raw/test.json", 
                          "/DATA1/ritesh/baselines_discourse_parsing/DialogueDiscourseParsing/data/Molweni/test.json")

print(f"Processed file saved to {output_file}")
