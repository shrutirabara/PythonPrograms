import csv

# define dictionary to store votes for national candidates
national_votes = {}

# define dictionary to store votes for local candidates per region
local_votes = {}

with open('votes.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # skip header row

    for row in reader:
        national_candidate = row[2]
        region = row[1]
        local_candidate = row[3]

        # count national votes
        if national_candidate in national_votes:
            national_votes[national_candidate] += 1
        else:
            national_votes[national_candidate] = 1

        # count local votes per region
        if region in local_votes:
            if local_candidate in local_votes[region]:
                local_votes[region][local_candidate] += 1
            else:
                local_votes[region][local_candidate] = 1
        else:
            local_votes[region] = {local_candidate: 1}

# find national winner
national_winner = max(national_votes, key=national_votes.get)
print(f"National winner: {national_winner}")

# find local winners per region
for region, candidates in local_votes.items():
    local_winner = max(candidates, key=candidates.get)
    print(f"Local winner for {region}: {local_winner}")
