# GATES OGORK 
# SPRING 2021 FINAL PROJECT
# IS 3220
# PASSWORD GENERATOR
# MAY 2, 2021

def reverse(app_name):
    # this function reverses whatever word the user inputs
    app_name = app_name.lower()
    return app_name[::-1]

def a_replace(name):
    # this function replaces every "a" with "@" 
    return name.replace("a", "@")

def o_replace(name):
    # this function replaces every "o" with "0" 
    return name.replace("o", "0")

def fifth_replace(name):
    # this function replaces every fifth character with "#"
    name = list(name)
    name[4] = "#"
    name = "".join(name)
    return name

def duplicate(name):
    # this function duplicates the generated password if it does not meet the users desired length
    duplicate = ""
    for letter in name:
        duplicate += letter
    return name+duplicate

def password_match(name, length):
    # this function returns a password that matches the length requested by the user
    # if the length of generated pssword > desired password length, we return portion of generated password(until desired length)
    if len(name) > length:
        return name[0:length]
    # if length of genrated password is < desired password, we add 0 until desired length
    while len(name) < length:
        name += "0"
    return name

def password_gen(app_name, input_length):
    # this function returns a password created from an app name
    app_name = reverse(app_name)
    app_name = app_name.capitalize()
    app_name = a_replace(app_name)
    app_name = o_replace(app_name)
    if len(app_name) < 8:
        app_name = duplicate(app_name)
    app_name = fifth_replace(app_name)
    if len(app_name) != input_length:
        app_name = password_match(app_name, input_length)
    return app_name

print("*************************************************************************************************")
print("*  Welcome to Gates' password generator                                                         *")
print("*  This app will generate a password for you based on the input provided                        *")
print("*************************************************************************************************")
print("*                                                                                               *")
app_name = input("*  What software application is this password for? (facebook, instagram, twitter...): ")
print("*                                                                                               *")
input_length = int(input("*  How long do you want your password to be? "))
print("*                                                                                               *")
print("*  Your password is: ", password_gen(app_name, input_length))
print("*                                                                                               *")
print("*                                                                                               *")
print("*************************************************************************************************")
