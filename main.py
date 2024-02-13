def main():
    book = "books/frankenstein.txt"
    text = get_book(book)
    counted = count(text)
    all_characters = character(text)
    full_report = char_sorted_list(text)

    print(f"--- Begin report of {book} ---")
    print(f"{counted} words found in the document")
    print("")
    print(full_report)
    print("")
    print("--- End report ---")
    

def get_book(book):
    with open(book) as f:
         return f.read()
         
def count(text):
    words = text.split()
    return len(words)

def character(text):
    lowered_string = text.lower()
    new_dict = {}
    for letter in lowered_string:
        if letter in new_dict:
           new_dict[letter] +=1
        else:
            new_dict[letter] = 1
    return new_dict

def sort_on(dict):
    return dict["num"]

def char_sorted_list(text):
    report_dic = character(text)
    report_list = []
    for key, value in report_dic.items():
        if key.isalpha():
           temp_dict = {}
           temp_dict["name"] = key
           temp_dict["num"] = value
           report_list.append(temp_dict)
    
    report_list.sort(reverse=True, key=sort_on)
    report_lines = []
    for item in report_list:
        name = item["name"]
        num = item["num"]
        report_line = f"The '{name}' character was found {num} times"
        report_lines.append(report_line)
    return "\n".join(report_lines)
    

main()
