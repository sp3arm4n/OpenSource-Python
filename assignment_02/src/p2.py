class Letter:
    def __init__(self, letterfrom, letterto):
        self.letterfrom = letterfrom
        self.letterto = letterto
        self.text = ''
    
    def addLine(self, line):
        self.text += '{}\n'.format(line)

    def get_text(self):
        return 'Deer {}:\n\n{}\nSincerely,\n\n{}'.format(self.letterfrom, self.text, self.letterto)

if __name__ == '__main__':
    letter = Letter('Dankook', 'Dooly')
    letter.addLine('Everyone in our school always do the best.')
    letter.addLine('They have their own plan for the future')

    print(letter.get_text())