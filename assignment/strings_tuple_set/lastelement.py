import ast

# Input: 1 2.5 hello True [1,2,3] {"key": "value"}
user_input = input("Enter values separated by spaces: ")

# Split input into separate values
input_values = user_input.split()

# Process each value to determine its type and convert accordingly
processed_values = []
for value in input_values:
    try:
        # Try to convert to integer
        processed_values.append(int(value))
    except ValueError:
        try:
            # Try to convert to float
            processed_values.append(float(value))
        except ValueError:
            # Try to convert to boolean
            if value.lower() == 'true':
                processed_values.append(True)
            elif value.lower() == 'false':
                processed_values.append(False)
            else:
                try:
                    # Try to convert to list or dict using ast.literal_eval
                    processed_values.append(ast.literal_eval(value))
                except (ValueError, SyntaxError):
                    # If all conversions fail, keep it as a string
                    processed_values.append(value)

print(processed_values)
