from snake import Snake

class Python(Snake):

    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False

    def digest_large_prey(self):
        print("Ok, let me get the stretchy pants")

    def constrict(self):
        print("Squeeeeze")

    def climb(self):
        print("Up we go")

    def shed_skin(self):
        print("I'm growing out of this room ")

peter = Python()
peter.breathe()
peter.use_tounge_to_smell()
peter.hunt()
peter.shed_skin()




