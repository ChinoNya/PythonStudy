import subprocess


def csvlook(args=None, input=None):
    if input is not None:
        p = subprocess.run('csvlook', input=input, capture_output=True)
    else:
        p = subprocess.run(' '.join(['csvlook', ' '.join(args)]), capture_output=True)
    return p.stdout


def csvcut(args=None, input=None):
    if input is not None:
        p = subprocess.run('csvcut', input=input, capture_output=True)
    else:
        p = subprocess.run(' '.join(['csvcut', ' '.join(args)]), capture_output=True)
    return p.stdout


def in2csv(file, input=None):
    if input is not None:
        p = subprocess.run('in2csv', input=input, capture_output=True)
    else:
        p = subprocess.run('in2csv ' + file, capture_output=True)
    return p.stdout


def csvstat(args=None, input=None):
    if input is not None:
        p = subprocess.run('csvstat', input=input, capture_output=True)
    else:
        p = subprocess.run(' '.join(['csvstat', ' '.join(args)]), capture_output=True)
    return p.stdout


def main():
    file = 'data.csv'
    cmd = ['-c ', '2', '3', '6']
    args = [cmd[0] + ','.join(cmd[1:4]), file]
    print(args)
    # data = csvstat(input=csvcut(args=args))
    data = csvcut(input=csvcut(args=args))
    print(type(data))
    data = str(data, encoding='utf-8')
    print(data)
    # print(data)


if __name__ == "__main__":
    main()
