# Regular Expression Project

This project contains a collection of Ruby scripts that demonstrate various regular expression patterns using the Oniguruma library. Each script is designed to match specific patterns and handle different text processing scenarios.

## Project Structure

* `0-simply_match_school.rb` - Matches the word "School"
* `1-repetition_token_0.rb` - Matches specific repetition pattern with "hbt{2,5}n"
* `2-repetition_token_1.rb` - Matches pattern with optional character "hb?tn"
* `3-repetition_token_2.rb` - Matches pattern with one or more repetitions "hbt+n"
* `4-repetition_token_3.rb` - Matches pattern with zero or more repetitions "hbt*n"
* `5-beginning_and_end.rb` - Matches strings starting with 'h', ending with 'n', with any single character in between
* `6-phone_number.rb` - Validates 10-digit phone numbers
* `7-OMG_WHY_ARE_YOU_SHOUTING.rb` - Extracts capital letters from text

## Requirements

* Ruby interpreter
* Ubuntu 20.04 LTS
* All scripts must be executable
* Oniguruma regular expression library (default in Ruby)

## Usage

Each script accepts one argument and processes it using the specified regular expression pattern:

```bash
./script_name.rb "text_to_process"
```

### Examples

1. Matching "School":
```bash
./0-simply_match_school.rb "Best School" # Output: School
```

2. Phone number validation:
```bash
./6-phone_number.rb "4155049898" # Output: 4155049898
./6-phone_number.rb "415-504-9898" # Output: 
```

3. Capital letters extraction:
```bash
./7-OMG_WHY_ARE_YOU_SHOUTING.rb "HELLO World" # Output: HELLO
```

## File Descriptions

* `0-simply_match_school.rb`: Simple pattern matching for the word "School"
* `1-repetition_token_0.rb`: Demonstrates repetition matching with specific count range
* `2-repetition_token_1.rb`: Shows optional character matching
* `3-repetition_token_2.rb`: Implements one or more repetition matching
* `4-repetition_token_3.rb`: Uses zero or more repetition matching
* `5-beginning_and_end.rb`: Pattern matching with start and end constraints
* `6-phone_number.rb`: Exact digit matching for phone numbers
* `7-OMG_WHY_ARE_YOU_SHOUTING.rb`: Character class matching for capital letters