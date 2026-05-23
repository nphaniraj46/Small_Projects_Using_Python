def is_valid(email:str)->str:
    '''
        This fucntion is for checking constraints 
    '''
    return '@' in email and '.' in email

def cleanemail(email:str)->dict:
    '''
    This function cleans and removes any extra spaces and splits the result as well we can get this username and domain individually
    '''
    cleaned_email=email.strip().lower()
    username,domain=cleaned_email.split('@')
    return {'username':username,
            'domain':domain}


def write_log(message:str):
    '''
        This fucntion writes the message to the file
    '''
    with open('Email_logs','a') as file:
        file.write(message+'\n')

def process(email):
    '''
    This is the main function which calls the other fucntions
    '''
    write_log('Processing Started')
    if not is_valid(email):
        write_log(f'The email recived is invalid {email}')
    else:
        cleaned_email=cleanemail(email)
        write_log(f'Processed email {cleaned_email}')
    write_log('Processing Stopped')


email=input("Enter email id ")
process(email)


