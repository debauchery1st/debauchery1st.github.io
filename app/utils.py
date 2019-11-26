
def avatar_robohash(seed, set=1):
    return "https://robohash.org/{seed}.png?set=set{set}".format(seed=seed, set=set)

def avatar_dicebear(sprite, seed, mood=None):
    valid_sprites = [
        "male", "female", "human", "identicon", 
        "initials", "bottts", "avataaars", "jdenticon", "gridy"]
    valid_moods = ["happy", "sad", "surprised"]
    if sprite not in valid_sprites:
        return "SPRITE MUST BE ONE OF : {}".format(", ".join(valid_sprites))
    if (mood is not None) and (mood in valid_moods):        
        return "https://avatars.dicebear.com/v2/{sprites}/{seed}.svg?options[mood][]={mood}".format(sprites=sprite, seed=seed, mood=mood)
    return "https://avatars.dicebear.com/v2/{sprites}/{seed}.svg".format(sprites=sprite, seed=seed)
