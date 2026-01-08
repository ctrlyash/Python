# Strings:

tea_type = "Ginger Tea"
customer_name = "Priya"

print(f"Order for {customer_name}: {tea_type} please!") # Order for Priya: Ginger Tea please!


tea_description = "Aromatic and Bold"
print(f"First word: {tea_description[0:7]}") # First word: Aromati  
# we can see that c was not printed which means-
# In python value at the last index of the range is not inclusive.


tea_description = "Aromatic and Bold"
print(f"First word: {tea_description[0:8]}") # First word: Aromatic


tea_description = "Aromatic and Bold"
print(f"First word: {tea_description[:8]}") # First word: Aromatic (it is not necessary to write 0 but the : is necesaary. Python itself assumes that the string starts with 0 in this case).


tea_description = "Aromatic and Bold"
print(f"First word: {tea_description[0:8:2]}") # Aoai 
# This :2 after 8 skips every 2nd element and give the remaining output. 


# Similarly
tea_description = "Aromatic and Bold"
print(f"Last word: {tea_description[12:]}") # Last word: Bold
# if we dont write the end index after :, Python itself assumes it as the last index of the string and prints till last.


tea_description = "Aromatic and Bold"
print(f"Last word: {tea_description[::-1]}") # Last word: dloB dna citamorA (Using ::-1 reverses the string)

# Encoding and Decoding of strings

lable_text = "Chai Spécial"
print(f"Non Encoded label: {lable_text}") # Non Encoded label: Chai Spécial

encoded_label = lable_text.encode("utf-8")
print(f"Encoded label: {encoded_label}") # Encoded label: b'Chai Sp\xc3\xa9cial' 

decoded_label = encoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}") # Decoded label: Chai Spécial






