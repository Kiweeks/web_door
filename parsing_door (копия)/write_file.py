def write_data_file(link_door, name, array_specifications, text_door):
    file = open('door/data.txt', 'w+', encoding="utf8")
    enter = '\n\n'

    file.write(link_door)
    file.write(enter)
    file.write(name)
    file.write(enter)
    file.write('Характеристики')
    file.write('\n')

    for i in array_specifications:
        label = i.find("label").text
        span = i.find("span").text
        file.write(f'{label}: {span}\n')

    file.write(enter)
    file.write(text_door)


    file.close()