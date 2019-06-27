from models import Person
import numpy as np

def list_overlap(a, b):
    for item in a:
        if item in b:
            return True
    return False

# calculates the similarity vector for each employee
def set_vectors(desiredLoc, desiredLang, desiredTech, desiredLob, 
            employees, vectors, similarities):
    # for each employee
    for i in range(len(employees)):
        # retrieve employee attributes
        loc = employees[i].loc
        langList = employees[i].lang
        techList = employees[i].tech
        lob = employees[i].lob

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
        vectors[i] = [langFlag, techFlag, lobFlag]
        similarities[i] = round((0.4*langFlag + 0.4*techFlag + 0.2*lobFlag), 2)

    return vectors, similarities

# calculates the most similar employee to the user
def recommend(employees, similarities):
    most_sim_score = max(similarities)
    index = np.argmax(np.asarray(similarities))
    most_sim_employee = employees[index].fname
    
    return most_sim_employee

def main():
    # hard coded examples of every employee    
    employees = [Person('X183746' 'Kim', 'Stonehouse', 'Glasgow', ['Java', 'Python'], ['Front End'], 'CIB'),
                Person('B837492', 'Monika', 'Jotautaite', 'Glasgow', ['Python'], ['AI', 'ML', 'Blockchain'], 'CIB'),
                Person('K837203', 'Martin', 'Dimitrov', 'Glasgow', ['Python','Java'], ['AI', 'ML'], 'CIB'),
                Person('L728492', 'Simona', 'Paulauskaite', 'Glasgow', ['Python','PHP'], ['Blockchain'], 'CIB'), 
                Person('N877293', 'Lyubomir', 'Ivanov', 'Glasgow', ['Go','PHP'], ['API','Cybersecurity'], 'CIB'),
                Person('A288731', 'Ivelina', 'Doynova', 'Glasgow', ['Go','Java'], ['Webapp', 'API'], 'CIB'),
                Person('G332482', 'Corrina', 'Galetza', 'Glasgow', ['Java','PHP'], ['Blockchain', 'Cybersecurity'], 'CIB'), 
                Person('R829937', 'Adithya', 'Ajith', 'Glasgow', ['Python','PHP', 'Go'], ['Blockchain', 'Neural Networks'], 'CIB')]

    # all vectors and similarities begin as zero
    vectors = [[0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0]]
    similarities = [0, 0, 0, 0, 0, 0, 0, 0]

    # passed in from front end user input
    desiredLoc = ["Glasgow"]
    desiredLang = ["Java"]
    desiredTech = ["AI"]
    desiredLob = ["CIB"]

    # calculate the vectors
    (vectors, similarities) = set_vectors(desiredLoc, desiredLang, desiredTech, desiredLob, 
                        employees, vectors, similarities)

    # calculate the most similar employee
    most_sim_employee = recommend(employees, similarities)

    print(similarities)
    print(most_sim_employee)

if __name__ == "__main__":
    main()