


def parse_log_line(line: str) -> dict:
    try:
        data, time, log_level, message = line.split(maxsplit=3)
        dict_message = {
             'data': data,
             'time': time,
             'log_level': log_level,
             'message': message
        }
        return dict_message


    except Exception as e:
        print("error", e)


def load_logs(file_path: str) -> list:
    try:    
        with open(file_path, 'r+') as file:         
            list_logs = []        
            for line in file:            
                list_logs.append(parse_log_line(line.strip()))        
            return list_logs
            
    except Exception as e:
        print("error", e)

def filter_logs_by_level(logs: list, level: str) -> list:
    try:    
        filtered_logs = filter(lambda log: log['log_level'] == level, logs)    
        return list(filtered_logs)
    
    except Exception as e:
        print("error", e)





def count_logs_by_level(logs: list) -> dict:
    try:
        count = {}

        count['ERROR'] = len(filter_logs_by_level(logs, 'ERROR'))
        count['WARNING'] = len(filter_logs_by_level(logs, 'WARNING'))
        count['INFO'] = len(filter_logs_by_level(logs, 'INFO'))
        count['DEBUG'] = len(filter_logs_by_level(logs, 'DEBUG'))

        return count
    
    except Exception as e:
        print("error", e)



def display_log_counts(dictionary: dict):
    try:
        max_key_length = max(len(key) for key in dictionary)
        max_value_length = max(len(str(value)) for value in dictionary.values())
        total_width = max(max_key_length, max_value_length) + 4  # Додатковий простір для вирівнювання

        print("-" * (total_width * 2 + 3))
        print("| {:^{total_width}} | {:^{total_width}} |".format("Тип логу", "Кількість", total_width=total_width))
        print("-" * (total_width * 2 + 3))

        for key, value in dictionary.items():
            print("| {:^{width}} | {:^{width}} |".format(key, value, width=total_width))

        print("-" * (total_width * 2 + 3))

    except Exception as e:
        print("error", e)

def display_type_error(type_log, list_of_dicts:list):
        try:
            print(f"Деталі логів для рівня '{type_log}':")
            for dictionary in list_of_dicts:
                print(dictionary['data'], dictionary['time'], dictionary['log_level'], '-', dictionary['message'])

        except Exception as e:
            print("error", e)


path = r'C:\Users\Руслан\Documents\GitHub\goit-pycore-hw-05\task_3\log.txt'

def main():
    try:         
        user_input = input()
        parts = user_input.split(maxsplit=1)
        if len(parts) == 1:
            path = parts[0]
            
            file_logs_list = load_logs(path)
            count_logs = count_logs_by_level(file_logs_list)
            
            display_log_counts(count_logs)

        elif len(parts) == 2:
            path, type_log = parts
            type_log = type_log.strip().upper()

            file_logs_list = load_logs(path)
            count_logs = count_logs_by_level(file_logs_list)
            list_logs = filter_logs_by_level(file_logs_list, type_log)
            
            display_log_counts(count_logs)
            display_type_error(type_log, list_logs)
            
            
        else:
            print("No correct datas")    

    except Exception as e:
        print("error", e)


if __name__ == "__main__":
    main()

