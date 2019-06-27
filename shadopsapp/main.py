from models import Person
import numpy as np

def list_overlap(a, b):
    for item in a:
        if item in b:
            return True
    return False

def main():
    # this will be hard coded in examples    
    all_employees = [Person("Kim", "Stonehouse", "Glasgow", ["React", "Java"], ["Front End"], "CIB"),
                    Person("Monika", "J", "London", ["Python", "PHP"], ["Data Science"], "AWM")]

    employee_vectors = [[0,0,0], [0,0,0]]
    employee_similarities = [0, 0]

    # this will be passed in from front end user input
    desiredLoc = ["Glasgow"]
    desiredLang = ["Java"]
    desiredTech = ["AI"]
    desiredLob = ["CIB"]

    # sets the employee vectors
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

            # if any of the employee's languages match the desired languages,
            # set the vector entry to 1
            if list_overlap(langList, desiredLang):
                langFlag = 1

            if list_overlap(techList, desiredTech):
                techFlag = 1

            if lob in desiredLob:
                lobFlag = 1

        # sets the vector entry
        employee_vectors[i] = [langFlag, techFlag, lobFlag]
        employee_similarities[i] = 0.4*langFlag + 0.4*techFlag + 0.2*lobFlag

    most_similar_employee_score = max(employee_similarities)
    most_similar_employee = all_employees[np.argmax(np.asarray(employee_similarities))].fname

    print(employee_similarities)
    print(most_similar_employee)

if __name__ == "__main__":
    main()