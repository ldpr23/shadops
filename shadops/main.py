from shadopsapp.models import Person
import django

def list_overlap(a, b):
    for item in a:
        if item in b:
            return True
    return False


def main():
    print("Hello world")
    
    all_employees = [Person("Kim", "Stonehouse", "Glasgow", ["React", "Java"], ["Front End"], "CIB"),
                    Person("Monika", "J", "London", ["Python", "PHP"], ["Data Science"], "AWM")]

    employee_vectors = [[0,0,0], [0,0,0]]

    desiredLoc = ["Glasgow", "London"]
    desiredLang = ["Java"]
    desiredTech = ["AI"]
    desiredLob = ["CIB"]

    for i in range(len(all_employees)):
        # retrieve lists of employee's desires
        loc = all_employees[i].loc
        langList = all_employees[i].lang
        techList = all_employees[i].tech
        lob = all_employees[i].lob

        langFlag = 0
        techFlag = 0
        lobFlag = 0

        # if the location doesn't match any of the required locations,
        # the employee vector is left as [0, 0, 0]
        if loc in desiredLoc:
            
            if list_overlap(langList, desiredLang):
                langFlag = 1

            if list_overlap(techList, desiredTech):
                techFlag = 1

            if lob in desiredLob:
                lobFlag = 1

        employee_vectors[i] = [langFlag, techFlag, lobFlag]

if __name__ == "__main__":
    main()