from espn_api.football import League

league = League(
    league_id = 685383224,
    year = 2025,
    espn_s2 = 'AEBEtqpYpwGHFscMygmIIm%2BiswLkyYXcM7HAoapIB8ddqxAj%2Fa8IdBw01xZ1gFXEbYVrRWSMTFdovBTPqXq2knRQMJtSxJNcRwCjgCMrY%2B4GlqkAhVcnLVlSjzBLLB30ljA2WbMFBBH6e1CgEtlU64l4%2BSEhqxBvPdKNlx1VfYMCrQfE3TPLppL5REoxQ%2BhDdG44wxoaENd7o6AEmDbgp8oiGYUeAywCOpoBmCsNY0uA1g5cc%2BsCb6W2v1D4yo9WwgwqH1CDP1irMa0%2BPM2Gj4ErEo596SLuH%2Ft06a8JMt3rPw%3D%3D',
    swid = '{4BA4ECAA-1D82-48AD-945F-FAEC95D31075}')

for team in league.teams:
    print("Wins: " + team.team_abbrev)
    print("Record: " + str(team.wins) + " - " + str(team.losses))

settings = league.settings