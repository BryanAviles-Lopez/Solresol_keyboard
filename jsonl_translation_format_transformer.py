# I'll use the transform_jsonl function to process the provided file and generate the desired output
import json

input_file_path = "C:\\Users\\bryan\\Dropbox\\PC\\Downloads\\gptexamples.jsonl"
output_file_path = "C:\\Users\\bryan\\Dropbox\\PC\\Downloads\\gptexamples_transformed_v2.jsonl"

def transform_jsonl(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            data = json.loads(line)
            
            # Extract the relevant information from the existing JSON
            src_language = data['prompt'].split(':')[0]
            tgt_language = data['prompt'].split('\n')[2].split(':')[0]
            src_sentence = data['prompt'].split('\n')[1]
            tgt_sentence = data['completion'].strip().split('\n')[0]
            
            # Create the new JSON format
            new_data = {
                "instruction": f"Translate this {src_language} text into {tgt_language}:",
                "input": src_sentence,
                "output": tgt_sentence
            }
            
            # Write the new JSON format to the output file
            outfile.write(json.dumps(new_data, ensure_ascii=False) + '\n')

# Transform the provided file
transform_jsonl(input_file_path, output_file_path)

output_file_path
