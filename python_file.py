# demo try except
def calculate(a, b):
    try:
        return a/b
    except Exception as ex:
        print('Error:', ex)
        return None
    finally:
        print('Finally')


print(calculate(1, 1))
print('Finish')
