age_inp=int(input("Enter the age of yours:"))
if(age_inp<18):
    print("You are a minor.")
elif(age_inp>=18 and age_inp<=65):
    print("You are an Adult.")
else:
    print("You are a Senior.")