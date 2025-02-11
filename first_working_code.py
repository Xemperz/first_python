age = int(input("Ge mig ålder:"))
height = int(input("Hur lång är du, bosse?:"))

MIN_AGE = 13
MIN_HEIGHT = 155

if(age < MIN_AGE and height > MIN_HEIGHT):
    print("du är tillräckligt lång men för ung")

elif(age > MIN_AGE and height < MIN_HEIGHT):
    print("du är gammal nog men inte tillräckligt lång!")

else:
    print("JA du får gå på!")
