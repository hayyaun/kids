def play_sound(file: str):
    try:
        from playsound import playsound
        print('Playing sound: ', file)
        playsound(file)
    except:
        print('Nemitunam seda play konam!')


def timer_sfx():
    return


def ref_whistle_sfx():
    return
