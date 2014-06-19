    class School(object):
    
        def __init__(self, name, motto, mascot, students):

            self.name = name
            self.motto = motto
            self.mascot = mascot
            self.students = self.studgen(students)
            self.grademodel = self.gradegen()

        def studgen(self, text):

            """Add Students to the School."""

            studlist = []
            for student in text:
                studlist.append(Student(student, text[student]))
            return studlist

        def gradegen(self):

            """Creates a letter-grading model."""

            grades = 'ABCDF'
            grademodel = []
            max = 100
            min = 90
            plus = minus = False
            for grade in grades:
                grademodel.append(Grade(grade, max, min, plus, minus))
                if max == 100:
                    max = max - 11
                else:
                    max = max - 10   
                if min > 60:
                    min = min - 10
                    plus = max - 2
                    minus = min + 2
                else:
                    min = 0
                    plus = minus = False
            return grademodel

        def show_students(self):

            """Prints a list of Students in the School."""

            for student in self.students:
                print student.name

        def get_letters(self):

            """Prints all Students and their grades."""

            letter = ''
            for student in self.students:
                for grade in self.grademodel:
                    if student.avgscore() >= grade.min and student.avgscore() <= grade.max:
                        letter = grade.name
                        if student.avgscore() >= grade.plus:
                            letter += '+'
                        if student.avgscore() <= grade.minus:
                            letter += '-'
                print "%s: %s (%s%%) - Scores: %s" % (student.name, letter, \
                                                    student.avgscore(), \
                                                " ".join(map(str, student.scores)))
                letter = ''

    class InputText(object):

        def __init__(self, text):
            self.text = self.cleanup(text)

        def cleanup(self, text):

            """Turns raw text into a dictionary for
            easier parsing later on."""

            self.text = self.lines(text)
            key = ''
            value = []
            cleantext = {}
            for line in self.text:
                line = self.singlespace(line)
                for char in line:
                    key += char
                    try:
                        int(char)
                        key = self.name_parse(key[:-2])
                        cleantext[key] = line
                        key = ''
                    except ValueError:
                        pass
            del cleantext['']
            for line in cleantext:
                cleantext[line] = self.get_int(cleantext[line])
            return cleantext

        def lines(self, text):

            """Turns raw text into a list where each item
            is a single line."""

            line = ''
            lines = []
            for char in text:
                line += char
                if '\n' in line:
                    line = line.rstrip('\n')
                    lines.append(line)
                    line = ''
            return lines

        def singlespace(self, text):

            """Remove non-single spaces."""

            text = text.strip()
            text = text.replace(',', '')
            lastchar = ''
            for char in text:
                if char == ' ' and lastchar == ' ':
                    text = text.replace('  ', ' ')
                lastchar = char
            return text

        def name_parse(self, text):

            """Swap FirstName-LastName."""

            text = text.split(' ')
            text.reverse()
            if text[0]:
                text[0] = text[0] + ','
            text = ' '.join(text)
            return text

        def get_int(self, text):

            """Turns integers in a line into
            actual integers."""

            text = text.split()
            ints = []
            for word in text:
                try:
                    ints.append(int(word))
                except:
                    pass
            return ints 

    class Grade(object):

        def __init__(self, name, max, min, plus, minus):
            self.name = name
            self.max = max
            self.min = min
            self.plus = plus
            self.minus = minus

    class Student(object):

        def __init__(self, name, scores):
            self.name = name
            self.scores = sorted(scores)

        def avgscore(self):

            """Returns a student's average score."""

            totscore = 0
            n = 0
            for score in self.scores:
                totscore += score
                n += 1
            return totscore / n

    ###################################################################
    """Create a cleaned version of the input text on Reddit."""

    reddit = InputText("""Jennifer ,  Adams   100 70  85  86  79
    Bubba , Bo Bob  50  55  60  53  30
    Matt ,  Brown   72  82  92  88  79
    Ned ,   Bundy   73  75  80  79  88
    Alfred ,    Butler  80  90  70  100 60
    Sarah , Cortez  90  72  61  70  80
    William ,   Fence   88  86  83  70  79
    Casper ,    Ghost   80  85  87  89  90
    Opie ,  Griffith    90  90  90  90  90
    Tony ,  Hawk    60  60  60  72  72
    Kirstin ,   Hill    100 90  92  94  95
    Hodor , Hodor   40  50  53  62  33
    Clark , Kent    89  90  88  92  91
    Tyrion ,    Lannister   93  97  100 91  95
    Ken ,   Larson  70  80  85  73  79
    Stannis ,   Mannis  60  70  75  77  78
    Bob ,   Martinez    79  88  92  82  72
    Jean Luc ,  Picard  90  89  95  70  65
    Harry , Potter  73  75  77  69  73
    Jaina , Proudmoore  90  92  100 95  94
    Richie ,    Rich    88  90  87  91  86
    John ,  Smith   90  80  70  60  50
    Jon ,   Snow    70  70  70  70  72
    Arya ,  Stark   91  92  90  93  90
    Edwin , Van Clef    40  50  55  57  33
    Valerie ,   Vetter  79  81  78  83  80
    Katelyn ,   Weekes  90  95  92  93  97
    Wil  , Wheaton  70  80  75  71  77
    Steve , Wozniak 88  89  87  86  85
    Derek , Zoolander   80  81  85  88  90""")

    ###################################################################

    """Found the school and fill it with students."""
    greendale = School('Greendale', 'E Pluribus Anus', 'Human Being', reddit.text)

    """View each students' performance."""
    greendale.get_letters()