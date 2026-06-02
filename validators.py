def validate_password(password: str, password_repeat: str) -> list[str]:
    errors = []
    if password != password_repeat:
        errors.append('Пароли не совпадают')
    if len(password) < 8:
        errors.append('Пароль должен содержать не менее 8 символов')
    return errors

def validate_phone_numbers(phone_number: str) -> list[str]:
    errors = []

    phone_number = phone_number.replace(' ', '')
    phone_number = phone_number.replace('-', '')
    
    if phone_number.startswith('7') or phone_number.startswith('8'):
        phone_number = phone_number[1:]

    if ('+7' in phone_number) or ('+8' in phone_number):
        phone_number = phone_number[2:]

    if not (10 <= len(phone_number) <= 12):
        errors.append('Номер телефона слишком короткий')
    if phone_number[0] != '9':
        errors.append('Введите существующий номер телефона')
        
    return errors

def validate_registration_data(phone_number: str, password: str, password_repeat: str) -> list[str]:
    errors = []
    errors.extend(validate_password(password, password_repeat))
    errors.extend(validate_phone_numbers(phone_number))
    return errors