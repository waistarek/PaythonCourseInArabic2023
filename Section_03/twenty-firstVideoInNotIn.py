animal = "Lion is the king of the jungle"

word = input(": ")

#if word in animal:
 #   print(f"{word} is in \"{animal}\"")
#else:
 #   print(f"{word} not found in {animal}.")

#if word in animal:
 #   print(f'{word} is in "{animal}".')
#else:
  #  print(f'{word} not found in "{animal}".')

if word not in animal:
    print(f'{word} is not in "{animal}".')
else:
    print(f'{word}  found in "{animal}".')