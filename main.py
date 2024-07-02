def main():
    result = []
    while True:
        start = input('Enter the starting letter: ')
        end = input('Enter the starting letter: ')
        
        if not start.isalpha() or not end.isalpha():
            print('Must be an alphabet ')
            continue
        
        if ord(start) > ord(end):
            print('Start letter should be < end letter')
            continue
        
        for i in range(ord(start), ord(end) + 1):
            result.append(chr(i))
        print(*result)
        break
        

    """
    ########################################
    Code Your Program here
    ########################################
    """



    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
