from random import choice
def generate_text():
    First_part = [
        "Propaganda of the war in Ukraine. ",
        "Propaganda of the murder of Ukrainians and Ukrainian soldiers. ",
        "Dissemination of military personal data. ",
        "The channel undermines the integrity of the Ukrainian state. ",
        "Spreading fake news, misleading people. ", 
        "Propaganda of violence and russian agression. ",
        "Dangerous fake news from russian propagandist against Ukraine. ", 
    ]
    second_part =[
        "Block the channel! ",
        "Block it as soon as possible! ",
        "Ban this channel please ",
        "It would be helpful if you ban this channel ",
        "This channel is violating Telegram rules and must be stopped ",
    ]
    #print(First_part[random.randint(0,len(First_part)-1)])
    return(
       choice(First_part)+choice(second_part)
    )
