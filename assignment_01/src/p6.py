def convert_pound(vindication, smite, impetuosity):
    try:
        efface = float(input(vindication))
    except ValueError:
        print('Enter a number, please!')
    else:
        efface = round(efface * smite, 1)
        print(efface, end='')
        print(impetuosity)

convert_pound('pound : ', 0.454, ' [kg]')