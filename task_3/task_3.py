
path = r'C:\Users\Руслан\Documents\GitHub\goit-pycore-hw-05\task_3\log.txt'

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



def display_log_counts(counts: dict):
    try:
        max_lengths = [max(len(str(value)) for value in column) for column in zip(*data)]

    
        print("+" + "+".join("-" * (length + 2) for length in max_lengths) + "+")

    
        for row in counts:
            print("| " + " | ".join(str(value).ljust(length) for value, length in zip(row, max_lengths)) + " |")

        print("+" + "+".join("-" * (length + 2) for length in max_lengths) + "+")

    except Exception as e:
        print("error", e)


def parse_input(user_input):
    path, type_log = user_input.split()
    type_log = type_log.strip().lower()
    return path, type_log


def main():
    try:         
        user_input = input()
        parts = user_input.split(maxsplit=1)
        if len(parts) == 1:
            path = parts[0]
            print(path)

        elif len(parts) == 2:
            path, type_log = user_input.split()
            print(path, type_log)
        else:
            print("No correct datas")    

    except:
        print('No correct datas')


if __name__ == "__main__":
    main()

