import random

def gen_random():
    """generates random"""
    decision = random.randint(0, 28000)
    print "decision: ", decision
    fsuffix = repr(random.randint(1000000, 9999999))
    print "fsuffix: ", fsuffix

random.seed()
gen_random()
