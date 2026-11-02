# PART 1: User Input
name = input("Enter your real name: ") #str -> Text/String

# PART 2: String Operations
# String Slicing Operation based on index(position)
# String Concatenation Operation
code_name = name[0:1] + "007" # str -> Text/String

# PART 3: Different Data Types
id = 7 #int -> Integer
rating = 9.5 #float -> Decimal
is_active = True #bool -> True/False

# PART 4: Typecasting values to String
id_text = str(id) #str -> Text/String
rating_text = str(rating) #str -> Text/String
is_active_text = str(is_active) #str -> Text/String

# PART 4: Print the complete secret agent badge
print("======== SECRET AGENT BADGE ========")
print("AGENT NAME: " + name)  
print("AGENT ID: " + id_text)  
print("AGENT CODE: " + code_name)
print("AGENT ACTIVE: " + is_active_text)  
print("AGENT RATING: " + rating_text)
print("====================================")
