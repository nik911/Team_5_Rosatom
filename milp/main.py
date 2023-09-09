import csv
import json
def validate_ship_class(ship_class: str):
    if ship_class == 'No ice class' or ship_class == 'ice1' or ship_class == 'ice2' or ship_class == 'ice3':
        return {
            '0-3':'yourself',
            '4-6':'wiring',
            '7-10':'forbidden'
        }
    if ship_class == 'Arc4' or ship_class == 'Arc5' or ship_class == 'Arc6':
        return {
            '0-3':'yourself',
            '4-6':'yourself',
            '7-10':'wiring'
        }
    if ship_class == 'Arc7' or ship_class == 'Arc8' or ship_class == 'Arc9':
        return {
            '0-3':'yourself',
            '4-6':'yourself',
            '7-10':'yourself'
        }

def get_icebreakers():
    with open('../dataset/ice_ships.csv', 'r') as is_f:
        csv_reader = csv.reader(is_f, delimiter=',')
        row_counter = 0
        pocket = []
        for row in csv_reader:
            data = {}
            if row_counter == 0:
                pass
            else:
                data['name'] = str(row[0])
                data['IMO'] = str(row[1])
                pocket.append(data.copy())
            row_counter += 1
        return pocket

def get_all_requests():
    with open('../ai/requests.csv', 'r') as is_f:
        csv_reader = csv.reader(is_f, delimiter=',')
        row_counter = 0
        pocket = []
        for row in csv_reader:
            data = {}
            if row_counter != 0:
                data['name'] = row[0]
                data['IMO'] = row[1]
                data['ship_class'] = row[2]
                data['speed'] = row[3]
                data['start_point'] = row[4]
                data['end_point'] = row[5]
                data['start_time'] = row[6]
                data['end_time'] = row[7]
                pocket.append(data.copy())
            row_counter += 1
        with open('../dataset/req.json', 'w') as req_file:
            json.dump(pocket, req_file, ensure_ascii=False, indent=3)
            req_file.close()
        return pocket

def Cohesion_in_points():
    with open('../dataset/CIP.csv', 'r') as is_f:
        csv_reader = csv.reader(is_f, delimiter=',')
        row_counter = 0
        pocket = []
        for row in csv_reader:
            print(row)

print(Cohesion_in_points())
