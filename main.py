# Ask the user if they have played before
show_instructions = input ("Have you played this game "
                         "before? ") .lower ()

# If they say yes, output 'program continues'
if show_instructions == "yes" or show_instructions == "y":
    print ("program continues")

elif show_instructions == "no" or show_instructions == "n":
    print ("display instructions")
  
# If they say no, output 'display instructions'
else: 
  print ("Please answer yes / no")

print ("You chose {}".format(show_instructions))
#yhy7h khjhb