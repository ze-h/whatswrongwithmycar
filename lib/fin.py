
from Problems import VehicleIssues
V = VehicleIssues

def summarize_vehicle_issues(V):

    # Print end of program statement
    print("End of program. The top three vehicle issues with their probabilities are as follows:")

    # Sort the problems by their float values in descending order
    sorted_problems = sorted(V.problemlist.items(), key=lambda x: x[1], reverse=True)

    # Print the first three problems
    for problem, value in sorted_problems[:3]:
        print(f"{problem}: {value}")

summarize_vehicle_issues(V)
