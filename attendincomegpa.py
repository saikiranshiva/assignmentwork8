class AttdceShortgeException(Exception):
    def __init__(self):
        super().__init__()
def data(attendance,income,cgpa):
    if attendance<75 or income>500000 or cgpa<7:
        raise AttdceShortgeException
    else:
        print("you are eligible")
def main():
    try:
        attendance=int(input("please enter your attendance"))
        income=int(input("please enter your income "))
        cgpa=int(input("please enter cgpa"))
        data(attendance,income,cgpa)
    except AttdceShortgeException:
        print("you are not eligible")
main() 


