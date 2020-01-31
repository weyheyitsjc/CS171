def rev(text):
    sentence = ""
    for i in range(len(text) - 1, -1, -1):
        sentence += text[i]
    return sentence

def reverse_numbers(text):
    answer = ""
    nums = ""
    i = 0
    while i < len(text):
        if text[i].isdigit():
            while (i <= (len(text) - 1)) and (text[i].isdigit()):
                nums += text[i]
                i += 1
            answer += rev(nums)
            nums = ""
        else:
            answer += text[i]
            i += 1
    return answer
    
if __name__ == "__main__":
    print("Welcome to Digit Flipper")
    text = input("Enter Some Text:\n")
    print("Revised String:")
    print(reverse_numbers(text))