#positional arguments
def kidnames(*kids):
    print("the youngest child is " + kids[2])
kidnames("ravi", "Tabu", "samu")

#key value arguments piairs
def kidnames(**kids):
    print("first name " + kids["firstname"],"last name is " + kids["lastname"])
kidnames(firstname="ravi", lastname="kumar")