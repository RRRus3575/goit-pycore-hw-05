contacts = {}


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            print("Give me name and phone please.")
        except KeyError:
            print("Enter correct user name")
        except IndexError:
            print('Please provide a contact name')


    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        print("This name already exists")
    else:
        contacts[name] = phone    
        print("Contact added.") 

@input_error
def show_phone(args, contacts):        
    name = args[0]      
    print(contacts[name])             
    
        
@input_error
def change_contact(args, contacts):   
    name, phone = args     
    contacts[name] = phone           
    print("Contact update.") 
    
    

@input_error
def show_all(contacts):
    if  len(contacts) > 0:
        for key, value in contacts.items():
            print(key, ":", value)
    else:
        print("No contacts yet")
    



def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "add":
            add_contact(args, contacts)

        elif command == "phone":
            show_phone(args, contacts)

        elif command == "change":
            change_contact(args, contacts)

        elif command == "all":
            show_all(contacts)

        elif command == "hello":
            print("How can I help you?")

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()