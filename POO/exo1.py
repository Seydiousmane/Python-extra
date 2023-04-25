from itertools import count


def countered(phrase):
    counter = {}
    mots = phrase.lower().split(' ')
    for i in range(0, len(mots)):

        if mots[i] in counter:
            counter[mots[i]] += 1
        else:
            counter[mots[i]] = 1

    print(counter)   

countered('Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quidem dolor magni rerum. Illum molestiae odio alias magni corrupti exercitationem, cupiditate quae omnis at expedita laboriosam praesentium, obcaecati veniam ex possimus.')
