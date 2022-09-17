import csv


with open ("assessment_results.csv",newline='')as infile:
    reader = csv.reader(infile)
    for row in reader:
        print(row)
        # print(f"{'User id':<4} {'First':<15}{'last':<15}{'Assessment ID':<4}{'Assessment':<20}{'Description':<28}{'Score':<4}{'Competency':<20}{'Date Taken':<10})