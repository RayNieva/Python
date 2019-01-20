#!/usr/bin/env python

def main():
    types_of_people=10 
    x=f"There {types_of_people} types of people."

    binary="binary"
    do_not="binary"
    y="Those know {binary} and those who {do_not}."

    print(x)
    print(y)

    print(f"I said: {x}")
    print(f"I also said: '{y}'")

    hilarious=False
    joke_evaluation="Isn't that joke so funny?! {}"
    print(joke_evaluation.format(hilarious))

    w="This is the left side of ..."
    e="a string with a right side."
    print(w+e)






if __name__ == '__main__':
    main()
