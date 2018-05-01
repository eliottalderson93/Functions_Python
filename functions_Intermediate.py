# Create beCheerful().  Within it, print string "good morning!" 98 times.

def beCheerful(name='', repeat=1):
    print("good morning!"*98)
	print(f"good morning {name}\n"*repeat)
beCheerful()
beCheerful(name="john")
beCheerful(name="michael", repeat=5)
beCheerful(repeat=5, name="kb")
beCheerful(name="aa")
# helpful tips for the next assignment
import random
def randInt(min=0,max=100):
    rand = min+round(random.random()*(max-min))
    return rand
print(randInt(max=50))
print(randInt(min=50))
print(randInt(min=50,max=500))
