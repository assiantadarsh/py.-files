Text = str(input("enter anything here :"))
count = 0
vowels =" aeiouAEIOU"#includes both lowercase and uppercase 
for char in Text:           #Lopp through each character in the string
    if char in vowels:
        count +=1
print("number of vowels:",count)