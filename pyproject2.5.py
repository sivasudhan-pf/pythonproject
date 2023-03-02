'''Total amount of points
Our football team has finished the championship.
Our team's match results are recorded in a collection of strings. Each match is represented by a
string in the format "x:y", where x is our team's score and y is our opponents score.
For example: ["3:1", "2:2", "0:1", ...]
Points are awarded for each match as follows:
if x > y: 3 points (win)
if x < y: 0 points (loss)
if x = y: 1 point (tie)
We need to write a function that takes this collection and returns the number of points our team
(x) got in the championship by the rules given above.
Notes:
our team always plays 10 matches in the championship
0 <= x <= 4
0 <= y <= 4'''

def total_points(matches):
    points = 0
    for match in matches:
        x, y = map(int, match.split(':'))
        if x > y:
            points += 3
        elif x == y:
            points += 1
    return points

matches = ["3:1", "2:2", "0:1", "4:4", "1:0", "0:2", "1:3", "2:1", "1:0", "0:1"]
print(total_points(matches)) 