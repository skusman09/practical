import aiml
kernel=aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("LOAD AIML B")

while True:
    input_text=input(">Human: ")
    response=kernel.respond(input_text)
    print(">Bot: "+response )
    