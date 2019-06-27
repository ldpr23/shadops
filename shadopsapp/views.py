from django.shortcuts import render
from shadopsapp.models import Employee, DesiredInfo, Location, LineOfBusiness

# Create your views here.
def list_overlap(request, a, b):
    for item in a:
        if item in b:
            return True
    return False

# desired attributes
desiredLoc = ""
desiredLang = ""
desiredTech = ""
desiredLob = ""

similarities = []

# calculates the similarity vector for each employee
def recommend(request):
    # for each employee
    for employee in Employee.objects.all():
        # retrieve employee attributes
        loc = employee.location
        lang = employee.language
        tech = employee.technology
        lob = employee.lob

        langFlag = 0
        techFlag = 0
        lobFlag = 0

        # if the location doesn't match any of the required locations,
        # the employee vector is left as [0, 0, 0]
        if loc in desiredLoc:

            # if any of the employee's languages match the desired languages,
            # set the vector entry to 1
            if lang in desiredLang:
                langFlag = 1

            if tech in desiredTech:
                techFlag = 1

            if lob in desiredLob:
                lobFlag = 1

        # sets the similarity entry
        similarities.append(((0.4*langFlag + 0.4*techFlag + 0.2*lobFlag), 2))

    # calculates the most similar employee to the user
    most_sim_score = max(similarities)
    index = np.argmax(np.asarray(similarities))
    most_sim_employee = Employee.objects.all()[index].name
    
    return (render, 'shadopsapp/base.html')

def index(request):
    return render(request, 'shadopsapp/base.html')


def about(request):
    return render(request, 'shadopsapp/about.html')