class VotingMachine(object):
    def __init__(self):
        self.democratVotes = 0
        self.republicanVotes = 0

    def voteClear(self):
        self.democratVotes = 0
        self.republicanVotes = 0
        print('clear')

    def voteDemocrat(self):
        self.democratVotes += 1

    def voteRepublican(self):
        self.republicanVotes += 1

    def getVote(self):
        print('Democrat Votes', self.democratVotes)
        print('Republican Votes', self.republicanVotes)

if __name__ == '__main__':
    vm = VotingMachine()
    vm.getVote()

    vm.voteDemocrat()
    vm.voteDemocrat()
    vm.voteDemocrat()
    vm.voteDemocrat()

    vm.voteRepublican()
    vm.voteRepublican()
    vm.voteRepublican()

    vm.getVote()
    vm.voteClear()
    vm.getVote()