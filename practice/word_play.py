# coding: utf-8

import requests

result_list = []

toUp = {'ァ':'ア', 'ィ':'イ', 'ゥ':'ウ', 'ェ':'エ', 'ォ':'オ', 'ッ':'ツ', 'ャ':'ヤ', 'ュ':'ユ', 'ョ':'ヨ'}

while True:

    # Input
    input_line = input("あなたの番です(カタカナで入力してね) >> ")

    if input_line[-1] == 'ー':
        input_line = input_line[:-1]

    for input_item, input_up in toUp.items():
        if input_line[:-1] == input_item:
            input_line[:-1] = input_up

    result_list.append(input_line)

    # Output
    response = requests.post('https://shiritori-server.herokuapp.com/', data={'word': input_line})
    output_line = response.text[9:-2]

    if output_line[-1] == 'ー':
        output_line = output_line[:-1]

    for output_item, output_up in toUp.items():
        if output_line[:-1] == output_item:
            output_line[:-1] = output_up

    result_list.append(output_line)

    print("あいて: " + output_line)

    if input_line[-1] == 'ン':
        print("あなたの負けです")
        for i in result_list:
            print(i + " => ", end="")
        break

    elif output_line[-1] == 'ン':
        print("あなたの勝利です")
        for j in result_list:
            print(j + " => ", end="")
        break

    elif result_list.count(input_line) >= 2:
        print("あなたの負けです")
        for k in result_list:
            print(k + " => ", end="")
        break

    elif result_list.count(output_line) >= 2:
        print("あなたの勝利です")
        for l in result_list:
            print(l + " => ", end="")
        break
